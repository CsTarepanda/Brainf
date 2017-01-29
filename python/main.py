#!/usr/bin/python3
from ply_util import *
from yacc_util import *
# import equation
# import unary
import brainfuck


def_tokens(
        # equal=r"=",
        plus=r"\+",
        minus=r"-",
        # id=r"[a-zA-Z_][a-zA-Z_0-9]*",
        # num=r"\d+\.?\d*",
        r_ang_brac=r">",
        l_ang_brac=r"<",
        r_box_brac=r"\]",
        l_box_brac=r"\[",
        comma=r",",
        dot=r"\.",
        )


# @yacc_rule
# def expression(p):
#     "value : ID | NUM | unary"
#     to(p)
#
#
# yacc_add(
# execute("""bf>>
# +++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.
# ------------.<++++++++.--------.+++.------.--------.>+.
# ,.>,.>,.>,.>,.>,.
# """)
while True:
    execute(input())
