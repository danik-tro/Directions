# Directions

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-commit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat)](https://github.com/pre-commit/pre-commit)

## [Turn with a Compass](https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python)
You have an 8-wind compass, like this:

![](https://image.shutterstock.com/image-vector/compass-rose-eight-abbreviated-initials-260nw-1453270079.jpg)

You receive the direction you are **facing** (one of the 8 directions: **N, NE, E, SE, S, SW, W, NW**) and a certain degree to **turn** (a multiple of 45, between -1080 and 1080); positive means clockwise, and negative means counter-clockwise.

Return the direction you will face after the turn.


### Examples
```
"S",  180  -->  "N"
"SE", -45  -->  "E"
"W",  495  -->  "NE"
```

## Setup
Init virtualenv, install requirements, install pre-commit hooks
> make setup


## Useful commands

Run app
> make run

Run Tests
> make test

Run tests with coverage
> make coverage

Clean cache
> make clean

Mypy
> make mypy

Flake8
> make lint

Isort && Black
> make black
