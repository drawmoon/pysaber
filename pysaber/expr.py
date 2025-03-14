from __future__ import annotations
from typing import Callable, List, Literal, Optional, Union
from pydantic import BaseModel, Field


class _Context: ...


FieldExpr = str


class LogicalExpr(BaseModel):
    operator: Literal["and", "or"]
    expr: List[Expr]

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...


class FilterExpr(BaseModel):
    input: Union[str, int]
    alias: Optional[str] = Field(default=None, alias="as")
    cond: Optional[Union[Expr, Literal["every"]]] = None
    limit: Optional[Union[int, Expr]] = None

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...


class AggExpr(BaseModel):
    operator: Literal["count", "max", "min", "sum", "avg", "round", "median"]
    expr: Expr
    alias: Optional[str] = Field(default=None, alias="as")
    is_all: Optional[bool] = Field(default=None, alias="all")
    is_distinct: Optional[bool] = Field(default=None, alias="distinct")

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...


Expr = Union[FieldExpr, LogicalExpr, FilterExpr, AggExpr]
