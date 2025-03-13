# <img src="./docs/logo.svg" height="35" width="35" align="left"> pysaber

中文 | [English](./README_en.md)

### 概述

本项目是一个多数据库兼容的查询中间件，通过标准化接口实现跨数据库SQL生成与执行。

核心能力包括：  
- JSON 驱动的 SQL 生成：通过声明式 JSON 模型定义查询逻辑，自动转换为各数据库原生 SQL 语法。
- 数据库兼容支持：
  - PostgreSQL
  - MySQL
- 统一函数抽象层：封装数据库特有函数差异（如字符串处理、日期计算、聚合逻辑），提供标准化函数接口。
- 操作审计追踪：完整记录 SQL 执行上下文（执行人、时间、原始模型、生成 SQL、执行耗时）。

```json

```

## License

Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
