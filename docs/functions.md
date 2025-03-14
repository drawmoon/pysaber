# Functions

- [Function](#function)
  - [Avg](#avg)
  - [Count](#count)
  - [Sum](#sum)
  - [Max](#max)
  - [Min](#min)
  - [Median](#median)
  - [Percentile](#percentile)
  - [Round](#round)
  - [Convert](#convert)
  - [ToChar](#tochar)
  - [Rpad](#rpad)
  - [Now](#now)
  - [Date](#date)
  - [DateAdd](#dateadd)
  - [DateSub](#datesub)
  - [DateTrunc](#datetrunc)
  - [DateFormat](#dateformat)
  - [Extract](#extract)
  - [RawSql](#rawsql)
  - [User](#user)
- [Expression](#expression)
  - [Column](#column)
  - [Comparison](#comparison)
  - [Logical](#logical)
  - [Not](#not)
  - [In](#in)
  - [IsNull](#isnull)
  - [Like](#like)
  - [Between](#between)
  - [CaseWhen](#casewhen)
  - [Empty](#empty)

## Function

### Avg

- Syntax

```
{
    "operator": "avg",
    "expr": <expr>
    [, "all" | "distinct": true]
}
```

- Arguments

| Name | Description |
| --- | --- |
| expr | The expression to be calculated. |

- Examples

```json
{
    "operator": "avg",
    "expr": "$abc"
}
```

Results

```sql
AVG(abc)
```

### Count

- Syntax

```
{
    "operator": "count",
    "expr": <expr>
    [, "all" | "distinct": true]
}
```

- Arguments

| Name | Description |
| --- | --- |
| expr | The expression to be calculated. |

### Median

- Syntax

```
{
    "operator": "median",
    "expr": <expr>
}
```

- Arguments

| Name | Description |
| --- | --- |
| expr | The expression to be calculated. |

- Examples

```json
{
    "operator": "median",
    "expr": "$abc"
}
```

Results

```sql
# Postgres
percentile_cont(0.5) within group (order by abc)
```
