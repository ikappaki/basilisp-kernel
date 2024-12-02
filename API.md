# Table of contents
-  [`basilisp-kernel.nrepl-server`](#basilisp-kernel.nrepl-server) 
    -  [`server-shut`](#basilisp-kernel.nrepl-server/server-shut) - Convenience function to shutdown the <code>SERVER</code>.
    -  [`server-start`](#basilisp-kernel.nrepl-server/server-start) - Starts the nrepl-server in async mode according to <code>OPTS</code>, using a asyncio task to schedule any pending client work every 100ms.

-----
# <a name="basilisp-kernel.nrepl-server">basilisp-kernel.nrepl-server</a>






## <a name="basilisp-kernel.nrepl-server/server-shut">`server-shut`</a><a name="basilisp-kernel.nrepl-server/server-shut"></a>
``` clojure

(server-shut server)
```
Function.

Convenience function to shutdown the `SERVER`.
<p><sub><a href="https://github.com/ikappaki/basilisp-kernel/blob/master/basilisp_kernel/nrepl_server.lpy#L87-L90">Source</a></sub></p>

## <a name="basilisp-kernel.nrepl-server/server-start">`server-start`</a><a name="basilisp-kernel.nrepl-server/server-start"></a>
``` clojure

(server-start)
(server-start {:keys [host port dir interval-sec], :as opts, :or {port 0, interval-sec 0.1}})
```
Function.

Starts the nrepl-server in async mode according to `OPTS`, using a
  asyncio task to schedule any pending client work every 100ms.

  `OPTS` is a map that can have the following keys. It defaults to {}.

  `:dir` The directory where the `.nrepl-port` file should be created
  at. It defaults to the current working directory if not given or
  empty.

  `:host` The interface address the server should be bound to. It
  defaults to 127.0.0.1 if not given or empty.

  `:port` The port number the server should listen to. It defaults to
  0, which indicates a random available port number.

  It return the `server`, which is a map with the following keys

  `:host` The host interface to which the server is bound.

  `:nrepl-port-file` The path to the `.nrepl-port` file created by the
  server.

  `:port` The port on the host interface the server listens for client
  connections.

  `:shutdown!` A function to shutdown the server.
<p><sub><a href="https://github.com/ikappaki/basilisp-kernel/blob/master/basilisp_kernel/nrepl_server.lpy#L25-L85">Source</a></sub></p>
