from unittest import TestCase
from pydantic import TypeAdapter
from .expr import AggExpr, Expr


class ExprTest(TestCase):
    def test_parse_count_expr(self):
        expr_json = """
        {
            "operator": "count",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)
