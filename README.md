# Remote Method Call using python and an example application

## Table of Contents

1. [Setup And Running](#setup)
2. [Quick Start](#quickstart)

---

## Setup and Running<a name="setup"></a>

There are at least two servers that need to be running before running the front end applications.\
First, you need to run the registery which accepts connections from other applications and allows you to add
entries for remote objects, or retrieve the address of a remote object that has been previously registered.

To run the registery open up a terminal and run the following command:

```bash
$ python manage.py registery
```

The default address and port of the registery is `localhost:7894`. but you can run the registery on your desired address. To do so follow the instruction below

```bash
$ python manage.py registery <desired_host> <desired_port>
```

The `manage.py` file is the main entry from which all the servers and applications are run. the specified argument determines what application the `manage.py` should run, which in this case is the `registery`.\
As you walkthrough this file you will see other command used with
the `manage.py` file.

After running the registery you need to run the server which contains the remote object. In another terminal run the following command:

```bash
$ python manage.py runserver
```

`runsverer` will invoke our application server which the remote object resides on, and automatically registers it with the registery.
If the registery is not running, then this command will fail.

Now everything is setup and you can run the example application front-ends. Two front-end applications are available. Our example app is a Conference Booking App.\
One of the applications is used by the admins to add, remove and manage Conferences, and the other one is for the normal users to book tickets for the available conferences.\

To run the `user` application run the following command:

```bash
$ python manage.py runuser
```

To run the `admin` application run the following command:

```bash
$ python manage.py runadmin
```

---

## Quick Start <a name="quickstart" id="quickstart"></a>

Remote method Invocation (RMI) allows an application to call a method on a remote object with full transparency. A client/server architecture is used, and the connection is synchronous and transient.\
In order to provide full transparency on the `client` side, a `stub` is implemented which acts as a proxy object. On the server side, however, the method call requests are recieved by a `skeleton` entity which unwraps the request and calls the actual method on the actual object and returns the result, which the stub is then going to deserialize and return to the client code as if the method invocation was performed locally.\
In order to ensure that the proxy object follows the same API as the real one, it is suggested to firstly, define the Interface of the object, which the client side and the server side can implement seperately, while keeping the object's API indentical. In python, interfaces are defined through the `Protocol` class.\
The RMI package provides `StubMixin` for `stub` implementation. After you defined the Interface of the object, you have to write a concrete class for the implementation and add the `StubMixin` at the end of the inheritance list to add `stub` functionality.

```python
#interfaces.py

class ObjectInterface(Protocol):
    # method definitions
    #...
```

```python
# stub.py

from interfaces import ObjectInterface
from RMI.client import StubMixin

class ConcreteObject(ObjectInterface, StubMixin):
    pass
    # method implementation
```

The `StubMixin` adds a `proxy` method which hides out the implementation detail of connecting to server and making the actual request and getting the response. the response. In order for the `proxy` method to work, the `_registery_host` and `_registery_port`attributes need to be defined on the concrete class.\

For skeleton implementation, you can subclass the `Skeleton` class and assign the `obj_class` attribute to the concrete implementation of the interface. If you need to pass any arguments to the class's `__init__` function you can do so through the `extra_kwargs` attribute which accepts a `dict`. Please note that the concrete implementation of the object should be a singleton.

```python
# skeleton.py

from RMI.server import Skeleton
from .server import ObjectConcreteImplementation

class ObjectSkeleton(Skeleton):
    obj_class = ObjectConcreteImplementation
    extra_kwargs = None
```
