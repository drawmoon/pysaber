from __future__ import annotations
from typing import Any, Callable, List, Optional, Union
from pydantic import BaseModel, Field


class Expr(BaseModel):
    """The common base type for all operate objects.

    This interface represents an expression that can be enumerated, serialized, cloned, and
    visited. It provides methods to replace expressions, accept visitors, serialize, deserialize,
    collect elements, convert to a list, and perform deep copies of the expression.

    Key features of this interface include:
    - Defining common behaviors for expressions
    - Supporting traversal and transformation of expression trees
    - Providing serialization and deserialization capabilities
    - Enabling deep copying to ensure independent instances of expressions
    """

    def replace(c: Callable[[Expr], Expr]) -> Expr:
        """Replaces the current expression with another expression using the provided replacement
        function.

        Args:
            c (Callable[[Expr], Expr]): The function used to generate a new expression instance

        Returns:
            Expr: A new expression instance
        """
        ...

    def accept(ctx: _Context) -> None:
        """Accepts a visitor and performs operations based on the visitor's behavior.

        This method implements the visitor pattern, allowing external logic (such as interpreters or
        transformers) to traverse the expression tree and perform specific operations.

        Args:
            ctx (_Context): The context object
        """
        ...


class _Context: ...


class FilterExpr(Expr):
    input: Optional[List[Any]] = None
    alias: Optional[str] = Field(default=None, alias="as")
    cond: Expr
    limit: Optional[Union[int, Expr]] = None

    def replace(c: Callable[[Expr], Expr]) -> Expr: ...

    def accept(ctx: _Context) -> None: ...
