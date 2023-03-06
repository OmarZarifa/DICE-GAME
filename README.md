DICE GAME PIG
==========================

This is a Python implementation of the classic Pig Dice game, which can be played by one or two players. The game is written in Python 3 and provides a command-line interface for playing the game

The objective of the game is to be the first player to reach a score of 50. Players take turns rolling a single die as many times as they wish, with the goal of accumulating as many points as possible without rolling a 1. 


Getting started 
--------------------------
To get started with the Pig Dice Game, follow these steps:
### 1. Check version of Python
To get started with the game, you'll need to have Python 3.6 or later installed on your system. You can check your Python version by following these steps:
1. Open the command prompt.
2. Type the following command and hit Enter:
```
python --version
```
3. The output will display the Python version installed on your machine.


If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/


### 2. Cloning the Repository
To download the Pig Dice game code, you can clone the repository from GitHub:
```bash
git clone https://github.com/OmarZarifa/DICE-GAME.git
```
After cloning, you can navigate to the cloned file using:
```bash
cd DICE-GAME
```

### 3. Setting up a Virtual Environment
It's recommended to use a virtual environment to isolate the dependencies required for this project. To create a new virtual environment, do the following:
###### 1. create a new virtual environment by running:
```bash
make venv
```
This will create a new virtual environment in the venv directory.

###### 2. Activate the virtual environment by running:

On Windows:
```bash
. .venv/Scripts/activate
```
On Linux/Mac:
```bash
. .venv/bin/activate
```

###### 3. Installing Dependencies 
Next, you'll need to install the required dependencies listed in requirements.txt. To do this, run:
```bash
make install
```
This will install the dependencies in your virtual environment.

To check what dependecies are installed, run:
```bash
make installed
```

###### 4. Deactivate the venv (Only when you are done!)
When you are done you can leave the venv using the command:
```bash
deactivate
```

Read more on [Python venv](https://docs.python.org/3/library/venv.html).
Read more on [Python PIP](https://pypi.org/project/pip/).





### Run the code

The example program can be started like this.

```
# Execute the main program
python guess/main.py
```

All code is stored below the directory `guess/`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `guess/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



Optional targets
--------------------------

These targets might be helpful when running your project.


More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.
