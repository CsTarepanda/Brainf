#!/usr/bin/python3
from ply_util import *
from yacc_util import *


@yacc_rule
def expression(p):
    "equation : value eq_operator equation | value %to"
    print_expr(p)


@yacc_rule
@yacc_addable
def expression(p):
    "eq_operator : PLUS | MINUS"
    to(p)
