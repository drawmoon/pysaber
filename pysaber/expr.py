from __future__ import annotations
from typing import Callable, List, Literal, Optional, Union, overload
from pydantic import BaseModel, Field
from .proto import RubikCube
from .dialect import Dialect


class _Context: ...


FieldExpr = str


class LogicalExpr(BaseModel):
    """A logical expression.
    Combine this condition with another condition using the specified operator.
    """

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
    operator: Literal["count", "max", "min", "sum", "avg", "round"]
    expr: Expr
    alias: Optional[str] = Field(default=None, alias="as")
    is_all: Optional[bool] = Field(default=None, alias="all")
    is_distinct: Optional[bool] = Field(default=None, alias="distinct")

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...


class MedianExpr(BaseModel):
    operator: Literal["median"]
    expr: Expr
    alias: Optional[str] = Field(default=None, alias="as")

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...


Expr = Union[FieldExpr, LogicalExpr, FilterExpr, AggExpr, MedianExpr]


def count(expr: Expr) -> AggExpr:
    return AggExpr(expr=expr, operator="count")


@overload
def render(expr: Expr, dialect: Dialect) -> str: ...
@overload
def render(expr: Expr, rubikcube: RubikCube) -> str: ...
def render(expr: Expr, arg: Union[Dialect, RubikCube]) -> str:
    """Renders the expression and returns the result.

    Args:
        expr (Expr): the expression object to be rendered.
        dialect (Dialect): the dialect to render the expression.
        rubikcube (DialectRubikCube): the rubikcube to render the expression.

    Returns:
        str: the rendered result.
    """

    if isinstance(arg, Dialect):
        return _render_by_dialect(expr, arg)
    return _render_by_rubikcube(expr, arg)


def _render_by_dialect(expr: Expr, dialect: Dialect) -> str: ...


def _render_by_rubikcube(expr: Expr, rubikcube: RubikCube) -> str: ...
