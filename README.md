[![PyPI](https://img.shields.io/pypi/v/basilisp-kernel.svg?style=flat-square)](https://pypi.org/project/basilisp-kernel/) [![CI](https://github.com/ikappaki/basilisp-kernel/actions/workflows/test.yml/badge.svg)](https://github.com/ikappaki/basilisp-kernel/actions/workflows/test.yml)

# Basilisp Kernel for Jupyter

[Basilisp](https://github.com/basilisp-lang/basilisp) is a Python-based Lisp implementation that offers broad compatibility with Clojure. Refer to [documentation](https://basilisp.readthedocs.io/en/latest/index.html) to get started.


# Overview

The Basilisp Kernel enables running Basilisp Clojure code directly within Jupyter notebooks.

## Features

- Full integration with Jupyter Notebook and JupyterLab.
- Enhanced autocompletion features using the `Tab` key.
- Seamless interoperability with Python libraries.
- Interactive development with your preferred editor, powered by the nREPL server running inside the notebook.

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

In the Jupyter interface, select the `Basilisp` Kernel when creating a new notebook.

## Examples

This project includes a series of Jupyter notebooks that demonstrate various features and capabilities. You can find these notebooks in the [notebooks](notebooks) directory of this repository.

![notebook plotting example](notebooks/nb-plot.png)

## nREPL support

See [API.md](API.md).

The Basilisp Kernel includes an nREPL server, allowing remote interaction with notebooks using Clojure-Enabled Editors like Emacs (via [CIDER](https://docs.cider.mx/cider/platforms/basilisp.html)) and VS code (via [Calva](https://calva.io/basilisp/)). For detailed use cases, visit the [Connecting Your Editor to the nREPL Server](https://github.com/ikappaki/basilisp-kernel/wiki/Connecting-Your-Editor-to-the-nREPL-Server) page.

### Starting the nREPL Server

Start the nREPL in your notebook by running:
```clojure
(require '[basilisp-kernel.nrepl-server :refer [server-start server-shut]])
(def server (server-start))
=> nREPL server started on port 58966 on host 127.0.0.1 - nrepl://127.0.0.1:58966
=> #'user/server
```

For additional configuration options, such as specifying a port with `:port` or directory for the `.nrepl-port` file with `:dir`, consult the [server-start](API.md#basilisp-kernel.nrepl-server/server-start) documentation.

### Stopping the nREPL Server

```clojure
(server-shut server)
=> :shut
```

## Getting Started with Basilisp Notebooks Development

Below are various methods to help you start writing Basilisp code that can be loaded in a Basilisp notebook.

### 🔋 Batteries Included Project: `basilex-notebook`

The [Basilisp Example Notebook](https://github.com/ikappaki/basilex-notebook) repository, is an excellent resource for exploring Basilisp notebooks. It includes Jupyter, the Basilisp kernel, a skeleton Basilisp library, and a development notebook to help you get started.

1. Install [Poetry](https://python-poetry.org/docs/) for dependency management.

2. Clone the repository, install dependencies, activate the environment and start Jupyter:

```shell
$ git clone https://github.com/ikappaki/basilex-notebook.git
$ cd basilex-notebook
$ poetry install
$ poetry shell
(<env>) $ jupyter notebook
```

3. Open the `tutorial.ipynb` notebook from the Jupyter interface. Refer to the [basilex-notebook documentation](https://github.com/ikappaki/basilex-notebook) for more details.

***
### 💾 Local Basilisp Files

You can seamlessly write and use Basilisp `.lpy` files in the same directory as your Notebook. These files can be required in the Notebook just like standard Basilisp namespaces.

For example, if you create a file named `dev.lpy` with the following content

`./dev.lpy`
```clojure
(ns dev)

(defn hello []
  :hi)
```

You can load and use it in your Notebook as follows

```Clojure
[n]:   (require 'dev)
[n+1]: (dev/hello)
:hi
```

#### nREPL development

You can start an nREPL server directly within a Notebook and connect to it using a Clojure-enabled editor.

In a notebook cell:

1. Load the nREPL server namespace:
```clojure
[n]: (require '[basilisp-kernel.nrepl-server :as nrepl-server])
```
2. Start the nREPL server at a random port
```Clojure
[n]: (def server (nrepl-server/server-start))
nREPL server started on port 59498 on host 127.0.0.1 - nrepl://127.0.0.1:59498
#'user/server
```

To connect your editor to the nREPL server create a `basilisp.edn` file in the same directory as your Notebook.

Open your Clojure-enabled editor and use its nREPL connection commands. The server generated a `.nrepl-port file` in the directory, which helps the editor locate the port.

Both [Emacs/CIDER](https://docs.cider.mx/cider/platforms/basilisp.html) and [VSCode/Calva](https://calva.io/basilisp/) offer explicit support for Basilisp.

#### CIDER (Emacs)

1. Run `M-x cider-connect-clj`.
2. Select `localhost`.
3. Select the `<project-dir>:<port number>` option.

#### Calva (VSCode)
1. Press `Ctrl-Alt-P` to open the Command Palette.
2. Select `Calva: Connect to a Running REPL Server, in your project`>`basilisp`.
3. The editor will automatically find the port using `.nrepl-port`.

The Editor should now connect seamlessly to the nREPL server.

***
### 📚 Basilisp Example Library Project: `basilex-basilib`

The [Basilisp Example Library](https://github.com/ikappaki/basilex-basilib) repository provides a starting point for setting up an external Basilisp library that can be integrated with your notebooks.

The instructions below assume you are working in a virtual environment where the Basilisp Notebooks will be launched (e.g. the `basiliex-notebook` setup above). This is indicated by the environment name prefix in your command prompt, such as `<venv>` in the examples below.

#### Setup

Clone the repository and install the `basilib` library as an editable package in in the same virtual environment as your Basilisp notebooks:

```shell
(<env>) $ git clone https://github.com/ikappaki/basilex-basilib.git
(<env>) $ cd basilex-basilib
# install example library in virtual environment as editable package
(<env>) $ pip install -e .
```

#### Usage

Load and interact with the library in your notebooks:

```clojure
[n]:   (require '[basilib.core :as bc])
[n+1]: (bc/time-now)
=> '2024-11-30 14:53:00'
```

#### nREPL development

For interactive coding, you can connect your preferred Clojure-Enabled Editor to a running nREPL server in your Basilisp Notebook.

In a notebook cell:

1. Load the nREPL server namespace:
```clojure
[n]: (require '[basilisp-kernel.nrepl-server :as nrepl-server])
```
2. Start the nREPL server on a fixed port:
```Clojure
[n]: (def server (server-start {:port 9998}))
nREPL server started on port 9998 on host 127.0.0.1 - nrepl://127.0.0.1:9998
#'user/server
```

In your code Editor, open the `basilisp.edn` file located in your project root directory (e.g. in `basilex-notebook`, `basilex-basilib` or your own Basilisp Project) to enable Clojure-specific features in your editor. Then, use your editor's commands to connect to the nREPL server.

Both [Emacs/CIDER](https://docs.cider.mx/cider/platforms/basilisp.html) and [VSCode/Calva](https://calva.io/basilisp/) offer explicit support for Basilisp.

###### Connecting via CIDER (Emacs)

1. Run `M-x cider-connect-clj`
2. Select `localhost`.
3. Enter the port number from the nREPL server output.

###### Connecting Calva (VSCode)

1. Press `Ctrl-Shift-P` to open the Command Palette.
2. Select `Calva: Connect to a Running REPL Server, not in your project`>`basilisp`.
3. Enter the port number from the nREPL server output.

## Acknowledgments

This kernel was developed using the [echo_kernel](https://github.com/jupyter/echo_kernel) as a starting point.

