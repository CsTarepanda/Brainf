#!/usr/bin/python3
# def----------------------------------------------------
import itertools
import re
from ply import lex, yacc
import yacc_util
count = itertools.count(1)
tokens = []


def def_token(name, pattern):
    name = name.upper()
    tokens.append(name)
    globals().__setitem__("t_{}".format(name), pattern)


def def_tokens(**defs):
    for k, v in defs.items():
        def_token(k, v)

        
def lex_add(**targets):
    for k, v in targets.items():
        if k in tokens:
            print("{} already exists in tokens.".format(k))
            continue
        else:
            def_token(k, v)


def lex_rule(f):
    def_token(f.__name__, f)


yacc_addables = {}


def yacc_addable(f):
    target = f.__doc__.split(":")[0].strip()
    yacc_addables[target] = f
    return f


def yacc_add(**targets):
    for k, v in targets.items():
        yacc_add_rule(yacc_addables[k], k, v)


yacc_rule_count = itertools.count(0)


def _hook(x):
    if re.match("^[ \t]*[a-zA-Z_][a-zA-Z_0-9]*[ \t]*$", x):
        return "yacc_util.%s(p)" % re.sub("[ \t]", "", x)
    return x


def yacc_add_rule(f, head, contents):
    for expr in contents:
        procedures = expr.split("%")
        doc = "{head} : {content}".format(head=head, content=procedures[0])
        procedures = [
                compile(_hook(x.replace("@@", ":")), "<string>", "exec") for x in procedures[1:]
                ]

        def create_expr(procedures):
            def expr(p):
                if procedures:
                    for procedure in procedures:
                        exec(procedure)
                else:
                    f(p)
            return expr
        expr = create_expr(procedures)
        setattr(expr, "__doc__", doc)
        globals().__setitem__(
                "p_%s%d" % (expr.__name__, next(yacc_rule_count)), expr)

def yacc_rule(f):
    doc = re.sub("\n", "", f.__doc__)
    head, content = doc.split(":")
    yacc_add_rule(f, head, content.split("|"))


# auto define
t_ignore = " \t\n"


def t_error(t):
    print(t)


def p_error(p):
    if p: print("syntax error...", p)
# -----------


def execute(code):
    lex.lex()
    yacc.yacc(debug=0, write_tables=0)
    return yacc.parse(code)


def define(**defines):
    for k, v in defines.items():
        globals().__setitem__(k, v)


class value:
    def __init__(self, v):
        self.v = v
