#!/usr/bin/env node
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const PACKAGE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PAYLOAD_ROOT = path.join(PACKAGE_ROOT, '.claude');
const MANIFEST_REL = '.claude/product-mvp/.install-manifest.json';
const MANIFEST_VERSION = 1;
const OWNED = [
  '.claude/agents/product-mvp-strategist.md',
  '.claude/agents/feature-cartographer.md',
  '.claude/agents/business-core-analyst.md',
  '.claude/agents/market-value-researcher.md',
  '.claude/agents/feature-scope-strategist.md',
  '.claude/agents/unit-economics-reviewer.md',
];

function fail(message) { throw new Error(message); }
function sha256(content) { return crypto.createHash('sha256').update(content).digest('hex'); }
function listFiles(dir, prefix) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a,b) => a.name.localeCompare(b.name))) {
    if (entry.name.startsWith('.') && entry.name !== '.claude') continue;
    const full = path.join(dir, entry.name);
    const relative = `${prefix}/${entry.name}`;
    if (entry.isSymbolicLink()) fail(`Enlace simbólico no permitido en el paquete: ${relative}`);
    if (entry.isDirectory()) files.push(...listFiles(full, relative));
    else if (entry.isFile() && !(/__pycache__|\.pyc$/.test(relative))) files.push(relative.replaceAll('\\','/'));
  }
  return files;
}
const PACKAGE_FILES = [
  ...OWNED,
  ...listFiles(path.join(PAYLOAD_ROOT, 'skills'), '.claude/skills'),
  ...listFiles(path.join(PAYLOAD_ROOT, 'product-mvp'), '.claude/product-mvp')
]; 
// Paths are only generated from a fixed, audited payload. Never follow symlinks in a target.
function checkNoSymlinks(root, rel) {
  let current = root;
  if (fs.existsSync(current) && fs.lstatSync(current).isSymbolicLink()) fail(`Target es un symlink: ${current}`);
  for (const part of rel.split('/')) {
    current = path.join(current, part);
    try {
      const info = fs.lstatSync(current);
      if (info.isSymbolicLink()) fail(`No se sigue un enlace simbólico: ${current}`);
    } catch (err) { if (err.code !== 'ENOENT') throw err; }
  }
}
function readManifest(target) {
  const file = path.join(target, MANIFEST_REL);
  checkNoSymlinks(target, MANIFEST_REL);
  if (!fs.existsSync(file)) return null;
  let data;
  try { data = JSON.parse(fs.readFileSync(file, 'utf8')); }
  catch { fail(`Manifest ilegible: ${file}`); }
  if (data.schema !== MANIFEST_VERSION || !data.files || typeof data.files !== 'object' || Array.isArray(data.files)) fail('Manifest incompatible');
  for (const [name, checksum] of Object.entries(data.files)) {
    if (!PACKAGE_FILES.includes(name) || !/^[a-f0-9]{64}$/.test(checksum)) fail(`Manifest no confiable: ${name}`);
  }
  return data;
}
function args(argv) {
  const config = { action: 'init', target: process.cwd(), dryRun: false, force: false, global: false };
  const queue = [...argv];
  if (queue[0] && !queue[0].startsWith('-')) config.action = queue.shift();
  if (!['init','update','uninstall','doctor','help','version'].includes(config.action)) fail(`Acción desconocida: ${config.action}`);
  while (queue.length) {
    const a = queue.shift();
    if (a === '--target' || a === '-C') { if (!queue.length) fail(`Falta valor para ${a}`); config.target = path.resolve(queue.shift()); }
    else if (a === '--global' || a === '-g') config.global = true;
    else if (a === '--dry-run') config.dryRun = true;
    else if (a === '--force') config.force = true;
    else if (a === '--help' || a === '-h') config.action = 'help';
    else if (a === '--version' || a === '-v') config.action = 'version';
    else fail(`Opción desconocida: ${a}`);
  }
  if (config.global) config.target = os.homedir();
  return config;
}
function pkgVersion() { return JSON.parse(fs.readFileSync(path.join(PACKAGE_ROOT, 'package.json'),'utf8')).version; }
function help() { console.log(`Product MVP Strategist ${pkgVersion()} — Claude Code\n\nUso:\n  product-mvp-strategist [init|update|doctor|uninstall] [opciones]\n\nOpciones:\n  --target, -C <directorio>  Instalar en el proyecto indicado (por defecto: directorio actual)\n  --global, -g             Instalar en ~/.claude (para todos tus proyectos)\n  --dry-run                Mostrar operaciones sin escribir archivos\n  --force                  Respaldar archivos modificados antes de sobrescribir o retirar\n  --help, -h               Ayuda\n  --version, -v            Versión\n\nNo sobreescribe ficheros ajenos. No modifica CLAUDE.md ni settings.json.\nLuego ejecuta /product-mvp-audit en Claude Code.`); }
function readFileDigest(file) { return sha256(fs.readFileSync(file)); }
function backupTarget(target, rel) {
  const stamp = new Date().toISOString().replace(/[.:]/g, '-');
  const dest = path.join(target, '.claude', 'product-mvp-user-backups', `${stamp}-${crypto.randomBytes(3).toString('hex')}`, rel);
  checkNoSymlinks(target, path.relative(target, dest).replaceAll('\\','/'));
  fs.mkdirSync(path.dirname(dest), {recursive:true});
  fs.copyFileSync(path.join(target, rel), dest, fs.constants.COPYFILE_EXCL);
  return path.relative(target,dest);
}
function writeManifest(target, entries, dryRun) {
  if (dryRun) return;
  const file = path.join(target, MANIFEST_REL);
  checkNoSymlinks(target, MANIFEST_REL);
  fs.mkdirSync(path.dirname(file), {recursive:true});
  const tmp = `${file}.${process.pid}.tmp`;
  const data = {schema: MANIFEST_VERSION, package: 'product-mvp-strategist', version: pkgVersion(), files: entries};
  fs.writeFileSync(tmp, JSON.stringify(data,null,2)+'\n',{flag:'wx'});
  fs.renameSync(tmp,file);
}
function install({target,force,dryRun,action}) {
  if(!fs.existsSync(target)||!fs.statSync(target).isDirectory()) fail(`Directorio destino inexistente: ${target}`);
  const previous = readManifest(target);
  const changes=[]; const collisions=[];
  const newEntries={};
  for(const rel of PACKAGE_FILES){
    checkNoSymlinks(target,rel);
    const source=path.join(PACKAGE_ROOT,rel);
    const destination=path.join(target,rel);
    const next=readFileDigest(source);
    newEntries[rel]=next;
    if(!fs.existsSync(destination)){changes.push({rel,kind:'add'});continue;}
    if(!fs.lstatSync(destination).isFile()) fail(`No es archivo regular: ${rel}`);
    const actual=readFileDigest(destination);
    if (actual===next) {changes.push({rel,kind:'identical'});continue;}
    const old=previous?.files[rel];
    if (old && old===actual) {changes.push({rel,kind:'update'});continue;}
    if (force) changes.push({rel,kind:'backup+replace'});
    else collisions.push(rel);
  }
  if (collisions.length){
    console.error(`Conflictos (${collisions.length}). No se modificó nada. Usa --force para respaldar y reemplazar:`);
    for(const rel of collisions) console.error(`  - ${rel}`);
    process.exitCode=2;return;
  }
  for (const {rel,kind} of changes) {
    if(kind==='identical') continue;
    console.log(`${dryRun?'[dry-run] ':''}${kind}: ${rel}`);
    if(dryRun) continue;
    if(kind==='backup+replace') console.log(`  respaldo: ${backupTarget(target,rel)}`);
    const file=path.join(target,rel);
    fs.mkdirSync(path.dirname(file),{recursive:true});
    fs.copyFileSync(path.join(PACKAGE_ROOT,rel),file);
  }
  // Remove stale previously-installed files only if unchanged. Never remove user edits during upgrades.
  for (const [rel,old] of Object.entries(previous?.files||{})) {
    if (newEntries[rel]) continue;
    checkNoSymlinks(target,rel);
    const file=path.join(target,rel);
    if (!fs.existsSync(file) || !fs.lstatSync(file).isFile()) continue;
    if (readFileDigest(file)!==old) {console.log(`Se conserva archivo editado: ${rel}`);continue;}
    console.log(`${dryRun?'[dry-run] ':''}obsolete-remove: ${rel}`);
    if (!dryRun) fs.rmSync(file);
  }
  writeManifest(target,newEntries,dryRun);
  console.log(`${dryRun?'Vista previa':'Instalación'} completada (${changes.length} archivos). Reinicia Claude Code y ejecuta /product-mvp-audit.`);
}
function doctor({target}){
  const manifest=readManifest(target);
  if(!manifest) {console.log('No instalado en '+target);process.exitCode=1;return;}
  let errors=0;
  for(const [rel,sha] of Object.entries(manifest.files)){
    checkNoSymlinks(target,rel);
    const file=path.join(target,rel);
    if(!fs.existsSync(file)||!fs.lstatSync(file).isFile()){ console.log(`FALTA ${rel}`);errors++; }
    else if(readFileDigest(file)!==sha){console.log(`MODIFICADO ${rel}`);errors++;}
  }
  console.log(errors?`Doctor: ${errors} problema(s) detectado(s).`:`Doctor: OK (${Object.keys(manifest.files).length} archivos íntegros).`);
  process.exitCode=errors?1:0;
}
function uninstall({target,force,dryRun}){
  const previous=readManifest(target);
  if(!previous) {console.log('No hay instalación registrada. No se borró nada.');return;}
  const conflicts=[];
  const removals=[];
  for(const [rel,sha] of Object.entries(previous.files)){
    checkNoSymlinks(target,rel);
    const file=path.join(target,rel);
    if(!fs.existsSync(file))continue;
    if(!fs.lstatSync(file).isFile())fail(`No es archivo regular: ${rel}`);
    if(readFileDigest(file)!==sha&&!force)conflicts.push(rel);
    removals.push({rel,modified:readFileDigest(file)!==sha});
  }
  if(conflicts.length){console.error('Desinstalación detenida: hay cambios locales. --force los respalda.');for(const p of conflicts) console.error(' - '+p);process.exitCode=2;return;}
  for(const {rel,modified} of removals){
    console.log(`${dryRun?'[dry-run] ':''}remove: ${rel}`);
    if(dryRun)continue;
    if(modified)console.log(`  respaldo: ${backupTarget(target,rel)}`);
    fs.rmSync(path.join(target,rel));
  }
  if(!dryRun)fs.rmSync(path.join(target,MANIFEST_REL));
  console.log(dryRun?'Vista previa de desinstalación completada.':'Desinstalado. No se tocaron archivos ajenos ni directorios de usuario.');
}
try{
  const config=args(process.argv.slice(2));
  if(config.action==='help') help();
  else if(config.action==='version')console.log(pkgVersion());
  else if(config.action==='doctor')doctor(config);
  else if(config.action==='uninstall')uninstall(config);
  else install(config);
} catch(err){ console.error('Error: '+err.message);process.exitCode=1; }
