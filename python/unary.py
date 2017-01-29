#!/usr/bin/python3
from ply_util import *
from yacc_util import *


@yacc_rule
def expression(p):
    "unary : unary_operator value %unary_op"


@yacc_rule
@yacc_addable
def expression(p):
    "unary_operator : PLUS | MINUS"
    to(p)
