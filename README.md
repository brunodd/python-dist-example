# Python basic distribution example

## Build wheel
```bash
python setup.py bdist_wheel
```

## Use

Install wheel
```bash
export PATH_TO_WHEEL=$(pwd)/dist/dist_example-0.0.3-py3-none-any.whl
pip install $PATH_TO_WHEEL
```

Use package
```python
>>> import dist_example.main
>>> dist_example.main.print_hi("Jane Doe")
Hi, Jane Doe
```

Verify availability of required packages (in this example: `numpy`)
```python
>>> import numpy
```
