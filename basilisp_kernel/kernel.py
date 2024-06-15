from ipykernel.ipkernel import IPythonKernel

from basilisp import cli
from basilisp import main as basilisp
from basilisp.lang import compiler as compiler
from basilisp.lang import reader as reader
from basilisp.lang import runtime as runtime
from basilisp.lang import symbol as sym

import re
from typing import Any, Callable, Optional, Sequence, Type
import sys

opts = {}
basilisp.init(opts)
ctx = compiler.CompilerContext(filename="basilisp-kernel", opts=opts)
eof = object()

user_ns = runtime.Namespace.get_or_create(sym.symbol("user"))
core_ns = runtime.Namespace.get(runtime.CORE_NS_SYM)
cli.eval_str("(ns user (:require clojure.core))", ctx, core_ns, eof)

_DELIMITED_WORD_PATTERN = re.compile(r"[\[\](){\}\s]+")

def do_execute(code):
    with runtime.bindings({
            runtime.Var.find_safe(sym.symbol("*out*", ns=runtime.CORE_NS)) : sys.stdout,
            runtime.Var.find_safe(sym.symbol("*err*", ns=runtime.CORE_NS)) : sys.stderr
    }):
        return cli.eval_str(code, ctx, user_ns, eof)


class BasilispKernel(IPythonKernel):
    implementation = 'basilisp-kernel'
    implementation_version = '1.0'
    language_info = {
        'name': 'clojure',
        'mimetype': 'text/x-clojure',
        'file_extension': '.lpy',
    }
    banner = "Basilisp: a Clojure-compatible(-ish) Lisp dialect in Python"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.imported = False

    def do_complete(self, acode, cursor_pos):
        code = acode[:cursor_pos]
        words = re.split(_DELIMITED_WORD_PATTERN, code)

        last_word = words[-1]
        completions = list(runtime.repl_completions(last_word)) or ()

        return {"status" : "ok",
                "matches" : completions,
                "cursor_start" : cursor_pos-len(last_word),
                "cursor_end" : cursor_pos,
                "metadata" : dict()
                }

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        bas_code = f'basilisp_kernel.kernel.do_execute({repr(code)})'
        if not self.imported:
            bas_code = f'import basilisp_kernel\n{bas_code}'
            self.imported = True
        return super().do_execute(code=bas_code, silent=silent, store_history=store_history,
                                  user_expressions=user_expressions, allow_stdin=allow_stdin)
    
