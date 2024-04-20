"""
Example use of jupyter_kernel_test, with tests for the default python3 kernel
(IPyKernel). This includes all the currently available tests.
"""

import unittest

import jupyter_kernel_test as jkt


class BasilispKernelTests(jkt.KernelTests):

    # REQUIRED

    # the kernel to be tested
    # this is the normally the name of the directory containing the
    # kernel.json file - you should be able to do
    # `jupyter console --kernel KERNEL_NAME`
    kernel_name = "basilisp"

    # Everything else is OPTIONAL

    # the name of the language the kernel executes
    # checked against language_info.name in kernel_info_reply
    language_name = "clojure"

    # the normal file extension (including the leading dot) for this language
    # checked against language_info.file_extension in kernel_info_reply
    file_extension = ".lpy"

    # code which should write the exact string `hello, world` to STDOUT
    code_hello_world = "(println \"hello, world\")"

    # code which should cause (any) text to be written to STDERR
    code_stderr = "(binding [*out* *err*] (println \"hi\"))"

    # samples for the autocompletion functionality
    # for each dictionary, `text` is the input to try and complete, and
    # `matches` the list of all complete matching strings which should be found
    completion_samples = [
        {
            "text": "[abc print",
            "matches": {"printf", "println", "println-str", "print", "print-str"},
        },
        {
            "text": "(import sys)\n(sys/int",
            "matches": {"sys/intern", "sys/int_info"},
        },

    ]

    # code which should generate a (user-level) error in the kernel, and send
    # a traceback to the client
    code_generate_error = "(throw (Exception. \"based\"))"

    # a statement or block of code which generates a result (which is shown
    # as Out[n] instead of just something printed to stdout)
    # running each `code` should cause `result` to be displayed (note that the
    # result here will always be a string representation of whatever the actual
    # result type is - be careful of string formatting)
    code_execute_result = [
        {"code": "(+ 1 2 3)", "result": "6"},
        {"code": "(map #(* % %) (range 1 4))", "result": "(1 4 9)"},
    ]

    # code which generates some sort of rich output
    # for each `code` input a single rich display object with the specified
    # `mime` type should be sent to the frontend
    # note that this expects a `display_data` message rather than
    # `execute_result`; this test might be a little too inflexible in some cases
    # code_display_data = [
    #     {
    #         "code": "(import [IPython.display :as d]) (println (d/display (d/HTML \"<b>A</b>\")))",
    #         # "code": "from IPython.display import HTML, display; display(HTML('<b>test</b>'))",
    #         "mime": "text/html",
    #     },
        # {
        #     "code": "from IPython.display import Math, display; display(Math('\\frac{1}{2}'))",
        #     "mime": "text/latex",
        # },
    # ]


if __name__ == "__main__":
    unittest.main()
