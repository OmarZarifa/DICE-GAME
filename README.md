DICE GAME PIG
==========================

This is a Python implementation of the classic Pig Dice game, which can be played by one or two players. The game is written in Python 3 and provides a command-line interface for playing the game

The objective of the game is to be the first player to reach a score of 50. Players take turns rolling a single die as many times as they wish, with the goal of accumulating as many points as possible without rolling a 1. 


Getting started 
--------------------------
To get started with the Pig Dice Game, you must follow the steps listed below. Please notice, that you need only to do steps 1 - 4 if you want just to play the game. All the steps, starting from step 5 (Testing), are optional steps that you might use for developing purposes.
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
#### 3.1  Create a new virtual environment by running:
```bash
make venv
```
This will create a new virtual environment in the venv directory.

#### 3.2  Activate the virtual environment by running:

On Windows:
```bash
. .venv/Scripts/activate
```
On Linux/Mac:
```bash
. .venv/bin/activate
```

#### 3.3  Installing Dependencies 
Next, you'll need to install the required dependencies listed in 'requirements.txt'. To do this, run:
```bash
make install
```
This will install the dependencies in your virtual environment.

To check what dependecies are installed, run:
```bash
make installed
```

#### 3.4  Deactivate the venv (Only when you are done!)
When you are done, you can leave the venv using the command:
```bash
deactivate
```

Read more on [Python venv](https://docs.python.org/3/library/venv.html).
Read more on [Python PIP](https://pypi.org/project/pip/).

### 4. Running the Game

To start the game, you have two ways: 

1. Run the command from the 'Makefile':
```bash
make run
```

2. Alternatively, you can run it using the command:
```bash
python main.py
```

After running the game successfully, follow the prompts to play the game.

### 5. Testing
This project includes unittests. The testfiles are stored in the `tests/` directory.
#### 5.1 Run the unittests
To run the unittest, run the following command:
```bash
make test
```
This will run the unit tests and output the results.

Read more on [unittest](https://docs.python.org/3/library/unittest.html)

#### 5.2 Measuring Code Coverage
To measure code coverage, run the following command:
```bash
make coverage
```
This will run the unittests and generate a code coverage report in the htmlcov directory. Open htmlcov/index.html in your web browser to view the report.

Read more on [coverage](https://coverage.readthedocs.io/)

### 5.3 Run parts of the testsuite
If you don't want to run the whole unittest, then you can run only parts of it. For examples files or methods in files.

* You can run all tests from a testfile by running:

```bash
python -m unittest test.test_game
```

* You can also run a single testcase from a file. For example, Run a test method, in a class, in a testfile using:

```bash
python -m unittest test.test_game.TestGameClass.test_init_default_object
```

### 6. Code Validators
This project includes static code validators to help ensure code quality and improve code style.
#### 6.1 Checking for PEP 8 Compliance
Check code style using make flake8:
```bash
make flake8
```
This will check the code for style issues using the Flake8 linter.

Read more on [flake8](https://flake8.pycqa.org/en/latest/)

#### 6.2 Checking for pylint Compliance
Check code quality using make pylint:
```bash
make pylint
```
This will check the code for quality issues using the pylint linter.

Read more on [pylint](https://pylint.org/)


###### Important notes:
* To check for the PEP 8 Compliance & the pylint compliance at the same time, run:
```bash
make lint
```
* The runned validators check the sourcecode and exclude the testcode.

* You might need to update the Makefile if you change the name of the source directory currently named `app/`.

### 7. Generating Documentation
This project includes several tools to generate documentation for the code.

#### 7.1 pdoc
To generate HTML documentation using pdoc, run the following command:
```bash
make pdoc
```
This will generate HTML documentation in the html directory. Open 'html/index.html' in your web browser to view the documentation.

#### 7.2 pydoc
To generate HTML documentation using pydoc, run the following command:
```bash
make pydoc
```
This will generate HTML documentation in the html directory. Open 'html/index.html' in your web browser to view the documentation.


### 8. Generating a UML Diagram
To generate a UML diagram of the code using pyreverse, run the following command:
```bash
make pyreverse
```
This will generate a UML diagram for the Pig Dice Game using the pyreverse tool


### 9. Remove generated files
In this project, you can remove generated and installed files.
* To remove files generated for tests or caching, run:
```bash
make clean
```
* To remove files generated for documentation and UML, run:
```bash
make clean-doc
```
* To remove files generated from, tests, caching, documentation and UML, run:
```bash
make clean-doc
```
This command combines the two commands: 'make clean' and 'make clean-doc'

