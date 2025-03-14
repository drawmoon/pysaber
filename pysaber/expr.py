from __future__ import annotations
from typing import Callable, List, Literal, Optional, Union
from pydantic import BaseModel, Field
from .context import _Context


FieldExpr = str
"""Represents a field reference expression in string form.

Used to identify fields/columns in query expressions, typically corresponding
to actual field names in a dataset or database schema.

Examples::

    "user_id"        # Direct reference to a field named 'user_id'
    "orders.total"   # Qualified field name using dot notation
    "$123"           # Parameterized field reference using ID notation
"""


class LogicalExpr(BaseModel):
    """A logical expression combining multiple conditions.

    Fields:
        operator (Literal["and", "or"]): Logical operator to combine expressions
        expr (List[Expr]): List of child expressions to be combined
    """

    operator: Literal["and", "or"]
    expr: List[Expr]

    def replace(c: Callable[[Expr], Expr]) -> Expr:
        """Returns a new expression with sub-expressions transformed by callback c"""
        ...

    def accept(ctx: _Context) -> None:
        """Visitor pattern entry point for context processing"""
        ...


class FilterExpr(BaseModel):
    """Represents a filtering expression with optional constraints.

    Fields:
        input (Union[str, int]): Input identifier or index
        alias (Optional[str], alias="as"): Optional alias name
        cond (Optional[Union[Expr, Literal["every"]]]): Filter condition or "every" marker
        limit (Optional[Union[int, Expr]]): Result limitation count or expression
    """

    input: Union[str, int]
    alias: Optional[str] = Field(default=None, alias="as")
    cond: Optional[Union[Expr, Literal["every"]]] = None
    limit: Optional[Union[int, Expr]] = None

    def replace(c: Callable[[Expr], Expr]) -> Expr:
        """Returns a new expression with sub-expressions transformed by callback c"""
        ...

    def accept(ctx: _Context) -> None:
        """Visitor pattern entry point for context processing"""
        ...


class AggExpr(BaseModel):
    """Aggregation operation expression.

    Fields:
        operator (Literal["count", "max", "min", "sum", "avg", "round"]): Aggregation type
        expr (Expr): Target expression to aggregate
        alias (Optional[str], alias="as"): Output alias
        is_all (Optional[bool], alias="all"): Whether to aggregate all values
        is_distinct (Optional[bool], alias="distinct"): Whether to use distinct aggregation
    """

    operator: Literal["count", "max", "min", "sum", "avg", "round"]
    expr: Expr
    alias: Optional[str] = Field(default=None, alias="as")
    is_all: Optional[bool] = Field(default=None, alias="all")
    is_distinct: Optional[bool] = Field(default=None, alias="distinct")

    def replace(c: Callable[[Expr], Expr]) -> Expr:
        """Returns a new expression with sub-expressions transformed by callback c"""
        ...

    def accept(ctx: _Context) -> None:
        """Visitor pattern entry point for context processing"""
        ...


class MedianExpr(BaseModel):
    """Specialized expression for median calculation."""

    operator: Literal["median"]
    expr: Expr
    alias: Optional[str] = Field(default=None, alias="as")

    def replace(c: Callable[[Expr], Expr]) -> Expr:
        """Returns a new expression with sub-expressions transformed by callback c"""
        ...

    def accept(ctx: _Context) -> None:
        """Visitor pattern entry point for context processing"""
        ...


Expr = Union[FieldExpr, LogicalExpr, FilterExpr, AggExpr, MedianExpr]
"""Union type representing all possible expression variants.
"""
