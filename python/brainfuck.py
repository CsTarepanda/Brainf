#!/usr/bin/python3
from ply_util import *
from yacc_util import *
import sys

memory = [0]
target = 0
input_string = ""
def add():
    memory[target] += 1


def sub():
    memory[target] -= 1


def rshift():
    global target
    target += 1
    if len(memory) <= target: memory.append(0)


def lshift():
    global target
    target -= 1
    if target < 0: target = len(memory) - 1


def inp():
    global input_string
    if not input_string: input_string += input()
    memory[target] = ord(input_string[0])
    input_string = input_string[1:]


def out():
    sys.stdout.write(chr(memory[target]))


def loop(brainfuck):
    def inner():
        while memory[target]:
            for b in brainfuck: b()
    return inner


def execute(brainfuck):
    for b in brainfuck: b()


define(bf_add=add, bf_sub=sub,
       bf_rshift=rshift, bf_lshift=lshift,
       bf_inp=inp, bf_out=out,
       bf_loop=loop, bf_exec=execute)
lex_add(brainfuck=r"bf>>")


@yacc_rule
def expression(p):
    """brainfuck
        : bf_operator brainfuck
            %p[0] = [p[1]] + p[2]
        | bf_operator
            %p[0] = [p[1]]
        | BRAINFUCK brainfuck
            %bf_exec(p[2])
            """


@yacc_rule
def expression(p):
    """bf_operator
        : PLUS %p[0] = bf_add
        | MINUS %p[0] = bf_sub
        | R_ANG_BRAC %p[0] = bf_rshift
        | L_ANG_BRAC %p[0] = bf_lshift
        | COMMA %p[0] = bf_inp
        | DOT %p[0] = bf_out
        | L_BOX_BRAC brainfuck R_BOX_BRAC %p[0] = bf_loop(p[2])
        """
