# <img src="./docs/logo.svg" height="35" width="35" align="left"> pysaber

[English](./README.md) | 中文

Saber 可接收生成 DSL 源代码的查询模型，还包括 DAO、拦截和数据库行为记录功能。

其功能包括：

- 基于模型的 DSL 源代码生成器
- 使用标准化计算函数语法，生成不同的 DSL 源代码
- DAOs
- 动态管理多个数据源
- 查询拦截和数据库行为记录
- 对以下数据库支持
  - MySQL
  - PostgreSQL

pysaber 中过滤器的语法与 MongoDB 相似，请参阅 [MongoDB 聚合操作符]((https://www.mongodb.com/zh-cn/docs/manual/reference/operator/aggregation/))。

## 简介

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

## 开源声明

Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
