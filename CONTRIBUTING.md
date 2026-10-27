# Contributing

Thanks for contributing. Fork the project, make changes on a feature branch, and open a Pull Request against `main`. Direct edits to `main` are not the contribution path.

Before opening your PR, run:

```bash
npm test
npm run validate
npm run validate:plugin
npm pack --dry-run
```

Describe what changed, why it improves the product-analysis results, and how you tested it. Do not introduce network calls to private codebases or install-time telemetry. Agents and skills analyze the host product in read-only mode and return text in the conversation. Do not add report-file requirements, write tools, or forked execution to the conversational entrypoint. Maintainers may request changes or decline merges; opening a PR does not grant merge permission.

The canonical agents and skills live under plugins/product-mvp-strategist/. Keep plugin, marketplace and package versions aligned. The legacy installer translates plugin paths and names; do not maintain a second copy of the prompts.
