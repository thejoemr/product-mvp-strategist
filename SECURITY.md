# Security Policy

## Reporting a vulnerability

Please **do not open public issues or pull requests** with exploit details, tokens, or private data. Use GitHub's **Report a vulnerability** (Private vulnerability reporting) if enabled, or privately contact the repository owner using an existing, verified communication channel. Do not publish a proof of concept before coordinating a fix.

## Scope

This tool installs local Claude Code agents and skills. It should never upload private repository content to public services, execute application migrations, or change product code during an audit. Report installer file-overwrite risks, unsafe paths, prompt injection, and credential disclosure.

Users should inspect changes and only run `npx` from a trusted tag or commit. Installing from `@main` executes code from the branch at that time.
