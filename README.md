[![CI](https://github.com/ikappaki/basilisp-kernel/actions/workflows/test.yml/badge.svg)](https://github.com/ikappaki/basilisp-kernel/actions/workflows/test.yml)

# Basilisp Kernel for Jupyter

Welcome to the Basilisp Kernel for Jupyter! This kernel allows you to run Basilisp code directly in your Jupyter notebooks.

[Basilisp](https://github.com/basilisp-lang/basilisp) is a Python-based Lisp implementation that offers broad compatibility with Clojure.

## Features

- Full integration with Jupyter Notebook and JupyterLab
- Enhanced autocompletion features
- Seamless interoperability with Python libraries

## Installation

Ensure you have Jupyter installed. If not, install it using pip:

```shell
pip install jupyter

```

To install the Basilisp Kernel, run:

```shell
pip install basilisp-kernel
```

## Usage

Start your Jupyter notebook server:

```shell
jupyter notebook
```

In the Jupyter interface, select the Basilisp kernel when creating a new notebook.


## Documentation

For full documentation on Basilisp, visit [Basilisp Documentation](https://basilisp.readthedocs.io/en/latest/).

## Examples

This project includes a series of Jupyter notebooks that demonstrate various features and capabilities. You can find these notebooks in the [notebooks](notebooks) directory of this repository.

![notebook plotting example](notebooks/nb-plot.png)

## Acknowledgments

This kernel was developed based on the [echo_kernel](https://github.com/jupyter/echo_kernel) as a starting point.

