# mkdocs-submodule-edit-uri
[![Build Status](https://img.shields.io/github/workflow/status/sondregronas/mkdocs-submodule-edit-uri/CI)](https://github.com/sondregronas/mkdocs-submodule-edit-uri/)
[![GitHub latest commit](https://img.shields.io/github/last-commit/sondregronas/mkdocs-submodule-edit-uri)](https://github.com/sondregronas/mkdocs-submodule-edit-uri/commit/)
[![PyPi](https://img.shields.io/pypi/v/mkdocs-submodule-edit-uri)](https://pypi.org/project/mkdocs-submodule-edit-uri/)
[![AGPLv3 license](https://img.shields.io/github/license/sondregronas/mkdocs-submodule-edit-uri)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![codecov](https://codecov.io/gh/sondregronas/mkdocs-submodule-edit-uri/branch/main/graph/badge.svg?token=N5IDI7Q4NZ)](https://codecov.io/gh/sondregronas/mkdocs-submodule-edit-uri)
[![Buymeacoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/u92RMis)

A super simple plugin to convert the edit_uri to match in GitHub submodules, allowing you to store parts of your docs on different repositories

Install using `pip install mkdocs-submodule-edit-uri`

Replaces a given `old` string to a `new` string wherever possible on mkdocs page content.

## Usage
```yaml
repo_url: https://github.com/user/repo
edit_uri: edit/main/docs/

plugins:
  - search
  - submodule-edit-uri:
      modules:
      - test:
          old: https://github.com/user/repo/edit/main/docs/SUBMODULE
          new: https://github.com/user/repo-SUBMODULE/edit/main
      - whatever-name-doesntmatter:
          old: https://github.com/user/repo/edit/main/docs/SUBMODULE2
          new: https://github.com/user/repo-SUBMODULE2/edit/main
```
> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

Note: please have the `old` variable be as specific as possible, as to not accidentally replace any other strings that might match the `old` value.
