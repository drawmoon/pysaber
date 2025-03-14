# <img src="./docs/logo.svg" height="35" width="35" align="left"> pysaber

English | [中文](./README_zh.md)

Receiving query models that generate DSL source code, saber also includes DAO, interception and database behavior logging capabilities.

The features include:

- Model-based DSL source code generator
- Generate different DSL source code using a standardized computational function syntax
- DAOs
- Dynamically manage multiple DataSources
- Fetch interception and database behavior logging capabilities
- Support for
  - MySQL
  - MariaDB
  - PostgreSQL
  - GreenPlum
  - GaussDB
  - Oracle
  - Dameng
  - MSSQL

For function syntax in Saber, [see this](./docs/functions_in_saber.md).

## introduction

```json
{
    "q": ["$1", "$2"],
    "aggregated": "sum",
    "f": {
        "$filter": {
            "input": "$2",
            "as": "a",
            "cond": {"gt": ["$$a", 100]}
        }
    }
}
```

## License

Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
