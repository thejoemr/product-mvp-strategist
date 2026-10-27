import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CLI = path.join(ROOT, 'bin/cli.js');
const MARK = '.claude/product-mvp/.install-manifest.json';
const AGENT = '.claude/agents/product-mvp-strategist.md';
const skill = '.claude/skills/product-mvp-audit/SKILL.md';

function sandbox(t) {
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'product-mvp-install-test-'));
  t.after(()=>fs.rmSync(dir,{recursive:true,force:true}));
  return dir;
}
function run(target,...params) {
  return spawnSync(process.execPath,[CLI,...params,'--target',target],{encoding:'utf8'});
}
function installedFile(target,rel) { return path.join(target, rel); }

 test('init installs all agents and skills; update idempotent; doctor and uninstall',t=>{
   const dir=sandbox(t);
   fs.mkdirSync(path.join(dir,'.claude'),{recursive:true});
   fs.writeFileSync(path.join(dir,'.claude','settings.json'),'KEEP');
   fs.writeFileSync(path.join(dir,'CLAUDE.md'),'KEEP');
   let r=run(dir,'init'); assert.equal(r.status,0,r.stderr);
   assert.ok(fs.existsSync(installedFile(dir,AGENT)));
   assert.ok(fs.existsSync(installedFile(dir,skill)));
   assert.ok(fs.existsSync(installedFile(dir,MARK)));
   assert.equal(JSON.parse(fs.readFileSync(installedFile(dir,MARK))).version,JSON.parse(fs.readFileSync(path.join(ROOT,'package.json'))).version);
   r=run(dir,'doctor');assert.equal(r.status,0,r.stdout+r.stderr);
   r=run(dir,'update');assert.equal(r.status,0,r.stdout+r.stderr);
   r=run(dir,'uninstall');assert.equal(r.status,0,r.stdout+r.stderr);
   assert.ok(!fs.existsSync(installedFile(dir,AGENT)));
   assert.ok(!fs.existsSync(installedFile(dir,MARK)));
   assert.equal(fs.readFileSync(path.join(dir,'.claude','settings.json'),'utf8'),'KEEP');
   assert.equal(fs.readFileSync(path.join(dir,'CLAUDE.md'),'utf8'),'KEEP');
 });

test('dry run makes no writes and conflicts abort entire installation',t=>{
  const dir=sandbox(t);
  assert.equal(run(dir,'init','--dry-run').status,0);
  assert.deepEqual(fs.readdirSync(dir),[]);
  fs.mkdirSync(path.dirname(installedFile(dir,AGENT)),{recursive:true});
  fs.writeFileSync(installedFile(dir,AGENT),'customized');
  const res=run(dir,'init');
  assert.equal(res.status,2);
  assert.equal(fs.readFileSync(installedFile(dir,AGENT),'utf8'),'customized');
  assert.equal(fs.existsSync(installedFile(dir,skill)),false);
  assert.equal(fs.existsSync(installedFile(dir,MARK)),false);
});

test('force backs up conflicts and never discards modified files without backup',t=>{
  const dir=sandbox(t);
  fs.mkdirSync(path.dirname(installedFile(dir,AGENT)),{recursive:true});
  fs.writeFileSync(installedFile(dir,AGENT),'MY CUSTOM AGENT');
  const r=run(dir,'init','--force');assert.equal(r.status,0,r.stderr);
  const backupRoot=path.join(dir,'.claude','product-mvp-user-backups');
  const folders=fs.readdirSync(backupRoot);
  assert.ok(folders.length>0);
  assert.equal(fs.readFileSync(path.join(backupRoot,folders[0],AGENT),'utf8'),'MY CUSTOM AGENT');
  fs.writeFileSync(installedFile(dir,AGENT),'MY EDIT TO INSTALLED AGENT');
  assert.equal(run(dir,'doctor').status,1);
  const fail=run(dir,'uninstall');assert.equal(fail.status,2);
  assert.ok(fs.existsSync(installedFile(dir,skill)));
  const ok=run(dir,'uninstall','--force');assert.equal(ok.status,0,ok.stderr);
  const all=fs.readdirSync(backupRoot);
  assert.ok(all.some(folder=>fs.existsSync(path.join(backupRoot,folder,AGENT)) && fs.readFileSync(path.join(backupRoot,folder,AGENT),'utf8')==='MY EDIT TO INSTALLED AGENT'));
  assert.equal(fs.existsSync(installedFile(dir,MARK)),false);
});

test('injection defenses refuse symlink target paths',t=>{
  const dir=sandbox(t);const other=sandbox(t);
  fs.mkdirSync(path.join(dir,'.claude'),{recursive:true});
  fs.symlinkSync(other,path.join(dir,'.claude','skills'),'dir');
  const r=run(dir,'init');
  assert.equal(r.status,1);
  assert.match(r.stderr,/simbólico|symlink/);
  assert.equal(fs.readdirSync(other).length,0);
});

test('global mode writes to HOME without affecting cwd',t=>{
  const dir=sandbox(t);
  const home=path.join(dir,'home');fs.mkdirSync(home);
  const r=spawnSync(process.execPath,[CLI,'init','--global'],{encoding:'utf8',cwd:dir,env:{...process.env,HOME:home,USERPROFILE:home}});
  assert.equal(r.status,0,r.stderr);
  assert.ok(fs.existsSync(installedFile(home,skill)));
  assert.equal(fs.existsSync(installedFile(dir,skill)),false);
});

test('help, version and missing target validation',t=>{
  const dir=sandbox(t);
  assert.equal(run(dir,'--version').stdout.trim(),JSON.parse(fs.readFileSync(path.join(ROOT,'package.json'))).version);
  assert.match(run(dir,'--help').stdout,/product-mvp-audit/);
  assert.equal(run(path.join(dir,'nonexistent'),'init').status,1);
});
