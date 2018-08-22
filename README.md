# Test automation Boilerplate

Python + unittest + selenium = `<3`

## Prerequisites

- Python 3
- Selenium (already in requrements.txt)
- Virtualenvironment

## Setup

1. Install `python3` 
2. Install `virtualenv` 
```bash
$ pip3 install virtualenv
```

3. Create a new virtualenv
```bash
$ virtualenv -p python3 your_env_name # env name can be anything
```

4. Start the environment
```bash
$ source your_env_name/bin/activate
```

5. Install dependencies in requirements.txt
```bash
$ pip install -r requirements.txt
```
6. You're done!

## Run the tests!

All you need to do is:
```bash
python -m unittest
```

The unittest module can also be used from the command line to run single or multiple tests.

```bash
python -m unittest test1
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```

## Docker

TBD

### Troubleshooting

#### Common error #1


`ImportError: Import by filename is not supported.`
 is caused by not using python3, most systems come pre-bundled with python2
You can make sure you have the right python version with
```bash
$ python --version
```
You might need to run commands using `python3` try:
```bash
$ which python3
```
and it should have a path to your virtualenv python installation.

#### Common error #2

`ModuleNotFoundError: No module named 'selenium'`

You don't have not installed selenium dependency in your virtualenv or your system.
Make sure you follow the setup guide.
