# PythonCLIScripts

A collection of Python Command Line Interface (CLI) scripts that I have found useful.

## Getting Started

To run the scripts, you will need the [Click](https://click.palletsprojects.com/en/7.x/) Python package, which can be installed with

```
pip install click
```
## Usage

To use each script, simply run

```
python CLIScript.py arg1 arg2 arg3 arg_etc
```

If you find that you often want to run a given script in various different directories, you can make an alias to the script so that you don't always need to include the full script path. This can be done by adding the following line to your `.bash_aliases` file:

```
alias script='python path/to/script/CLIScript.py'
```

where `script` can be changed to whatever you want to name the shortcut. To run the script simply do:

```
script arg1 arg2 arg3
```

after running `source ~/.bash_aliases`

## Documentation

Each script is self-documented using the documentation functionality of Click. To see script functionality and required arguments, run

```
python CLIScript.py --help
```

## Brief description of script functionalities:
`fbconvert`: Convert Fitbit json data into csv for easier parsing and plotting.
