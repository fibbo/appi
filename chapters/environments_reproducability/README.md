# Environments and Reproducability

The Python language is a vast ecosystem of libraries that can be installed with a simple command and made readily available for your code.
With bigger projects it will be more and more likely that you will depend on external libraries.

These packages are maintained by other people/organizations and it lies outside of the user's control how a package will develop inthe future. Such packages sometimes contain bugs that need to be fixed or the receive new features/improvements that make the package better - or in other cases they will deprecate functions.

While such changes are normally a good thing they can also to changes in how some of the code can be used (e.g. the function signature changes).

## Scenario

Imagine you depend on library `foo` and when you initially developed your program you installed version `1.0.0` of the `foo` library:

```bash
pip install foo
# pip installs the latest version of foo (aka 1.0.0)
```

and you have following Python program:

```python
import foo

foo.do_something()
```

Now imagine the maintainer of `foo` decides to change the function signature and it now accepts `0` parameters.

If someone at a later point also installs the `foo` library he will get the newer version of this library and if this person then tries to run the code above following will happen:

```bash
TypeError: test() missing 1 required positional argument: 'test'
```

The code that still works for you doesn't work for someone else!


## `requirements.txt`

Introducing `requirements.txt`: This file is usually found in the root of a project and it will contain all the libraries that it will need for your code to run.

So if we want to make sure that our project also works for someone who installs it at a later date, we can fix the version of the libraries we use:

```python
# Contents of requirement.txt
foo==1.0.0
```

### How to use this file

All that is left to do now for a new user of your code is to install the dependencies according to the `requirements.txt` and this is done by following command

```bash
pip install -r requirements.txt
```