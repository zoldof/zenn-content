```yml
name: Call Inject Snippet

on:
  push:
    paths:
      - 'snippets/*.py'
  workflow_dispatch:

jobs:
  inject:
    uses: zoldof/zenn-content/.github/workflows/Injext-snippet.yml@main
```
