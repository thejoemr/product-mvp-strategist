# Contributing

Thanks for contributing. Fork the project, make changes on a feature branch, and open a Pull Request against `main`. Direct edits to `main` are not the contribution path.

Before opening your PR, run:

```bash
npm test
npm run validate
npm pack --dry-run
```

Describe what changed, why it improves the product-analysis results, and how you tested it. Do not introduce network calls to private codebases or install-time telemetry. Agent files are read-only with respect to the host product except for the single approved Markdown report. Maintainers may request changes or decline merges; opening a PR does not grant merge permission.
