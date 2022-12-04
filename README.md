# Remote Method Call using python and an example application

## Setup and Running

There are at least two servers that need to be running before running the front end applications.\
First you need to run the registery which accepts connections from other applications and allows you to add
an entry for any object, or retrieve the address of a remote object that has previously been registered

To run the registery open up a terminal and run the following command:

```
$ python manage.py registery
```

The default address and port of the registery is `localhost:7894`(The instruction to run the registery on a different port is provided).\
The `manage.py` file is the main entry from which all the servers and application are run. the argument `registery`
will determine which application it should run.\
As you walkthrough this file you will see other command used with
the `manage.py` file.

After running the registery you need to run the server which contains the remote object. In another terminal run the following command:

```
$ python manage.py runserver
```

`runsverer` will invoke our application server which holds the remote object and automatically registers it with the registery.
If the registery is not running, then this command will fail.

Now everything is setup and you can run the example application front-ends. Two front-end applications are available which you can run.\
Our example app is a Conference Booking App, one of the application is used by the admins which they can add Conferences, and the other application is the application which the user books tickets for the conferences.

To run the `user` application run the following command:

```
$ python manage.py runuser
```

To run the `admin` application run the following command:

```
$ pythion manage.py runadmin
```
