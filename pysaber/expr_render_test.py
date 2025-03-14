from unittest import TestCase
from .expr import count


class ExprRenderTest(TestCase):
    def test_render_count_expr(self):
        expr = count("$abc")

        expr
