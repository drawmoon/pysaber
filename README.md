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
  - PostgreSQL

The syntax of filters in pysaber is similar to MongoDB, see [MongoDB Aggregation Operators](https://www.mongodb.com/zh-cn/docs/manual/reference/operator/aggregation/).

## introduction

```json
{
    "q": ["$1", "$2"],
    "aggregated": "sum",
    "f": {
        "input": "$2",
        "as": "a",
        "cond": {
            "operator": "gt",
            "value": ["$$a", 100]
        }
    }
}
```

## License

Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
