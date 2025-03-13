from typing import Union, overload
from .dialect import Dialect
from .expr import Expr
from .proto import RubikCube


@overload
def render(expr: Expr, dialect: Dialect) -> str: ...
@overload
def render(expr: Expr, rubikcube: RubikCube) -> str: ...
def render(expr: Expr, arg: Union[Dialect, RubikCube]) -> str:
    """Renders the expression and returns the result.

    Args:
        expr (Expr): the expression object to be rendered.
        dialect (Dialect): the dialect to render the expression.
        rubikcube (RubikCube): the rubikcube to render the expression.

    Returns:
        str: the rendered result.
    """

    def render_by_dialect(expr: Expr, dialect: Dialect) -> str: ...

    def render_by_rubikcube(expr: Expr, rubikcube: RubikCube) -> str: ...

    if isinstance(arg, Dialect):
        return render_by_dialect(expr, arg)
    return render_by_rubikcube(expr, arg)
