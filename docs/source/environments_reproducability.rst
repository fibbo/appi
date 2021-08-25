Environments and Reproducability
==================================

An important aspect of programming and scientific programming in particular is the rerproducability of results, that means that no matter where and when I execute some code (and this doesn't just concern Python but every programming language) I expect to be able to get the same results anywhere.

Example
-------

Consider you have a program that depends on a 3rd party library called ``X`` (i.e. it doesn't come with your Python installation). Let's assume that you tested your code with version 1.0 of ``X``. Furthermore, you use a particular function of ``X`` called ``do_something()``.

The creator of this 3rd party library doesn't know about you using his library and also doesn't really care. This creator now decides to change his library slightly, e.g. he changes the signature of function ``do_something(bool)`` and publishes a new version 2.0 of his library.

If you now provide your program to someone else and inform this person, that your program depends on library X this person will simply install this library via the ``pip`` installer but since the newest version is 2.0 it will install the newest version. Your program will now fail to run because your code calls the function ``do_something()`` without any arguments but since version 2.0 this function expects a boolean and thus your code will crash.

Versioning your dependencies will prevent this.

Versioning tools
----------------

Depending on the programming language there a different tools at your disposal to ensure that everyone can reproduce the same result across time and platforms.

.. note::
    The only reason why the outcome should be different, is when the other person uses a different version of your program.

Python offers different approaches to deal with this problem and in this course we look at the Python own approach called ``venv``.
