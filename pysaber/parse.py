from __future__ import annotations
from typing import Any, Dict
from .expr import Expr, FilterExpr

op_mappings = {"$filter": FilterExpr}


def parse_expr(expr_json: Dict[str, Any]) -> Expr: ...
