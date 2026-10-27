#!/usr/bin/env node
// Maintenance commands use the installed Python without depending on Windows Store aliases.
import { spawnSync } from 'node:child_process';

const candidates = process.platform === 'win32'
  ? [['python', []], ['py', ['-3']], ['python3', []]]
  : [['python3', []], ['python', []]];

let found = false;
for (const [command, prefix] of candidates) {
  const probe = spawnSync(command, [...prefix, '--version'], { stdio: 'ignore', timeout: 5000 });
  if (probe.error || probe.status !== 0) continue;
  found = true;
  const result = spawnSync(command, [...prefix, ...process.argv.slice(2)], { stdio: 'inherit' });
  if (result.error) console.error(result.error.message);
  process.exitCode = result.status ?? 1;
  break;
}
if (!found) {
  console.error('Python 3.10+ es necesario para verificar el paquete; no para instalarlo.');
  process.exitCode = 1;
}
