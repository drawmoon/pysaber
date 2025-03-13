from unittest import TestCase
from pydantic import TypeAdapter
from .expr import AggExpr, Expr, MedianExpr


class ExprParseTest(TestCase):
    def test_parse_count_expr(self):
        expr_json = """
        {
            "operator": "count",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_max_expr(self):
        expr_json = """
        {
            "operator": "max",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_min_expr(self):
        expr_json = """
        {
            "operator": "min",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_sum_expr(self):
        expr_json = """
        {
            "operator": "sum",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_avg_expr(self):
        expr_json = """
        {
            "operator": "avg",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_round_expr(self):
        expr_json = """
        {
            "operator": "round",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, AggExpr)

    def test_parse_median_expr(self):
        expr_json = """
        {
            "operator": "median",
            "expr": "$abc"
        }"""
        expr = TypeAdapter(Expr).validate_json(expr_json)
        self.assertIsInstance(expr, MedianExpr)
