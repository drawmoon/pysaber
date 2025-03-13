from .expr import AggExpr, Expr


def count(expr: Expr) -> AggExpr:
    return AggExpr(expr=expr, operator="count")
