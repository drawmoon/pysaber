[private]
default:
  @just --list

# install dependencies
install:
  @uv sync --locked --all-groups

# check the code cleanliness
check:
  @ruff check
  @ruff format --check

# format the code
format:
  @ruff format

# run tests
test:
  @pytest
  @echo "Tests passed"

# generate pip lockfile
lock:
  @uv lock

# package as wheel
package:
  rm -rf dist
  python setup.py check
  python -m build

# publish package to pypi
publish: package
  python -m twine upload --repository pypi dist/*
