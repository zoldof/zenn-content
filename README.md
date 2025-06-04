```yml
name: Call Inject Snippet

on:
  push:
    paths:
      - 'snippets/*.py'
  workflow_dispatch:

jobs:
  inject:
    uses: zoldof/zenn-content/.github/workflows/injext-snippet.yml@main
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
