# toml_config
Python library that simplifies parsing and creating Toml configuration files.
Wrapper on [toml](https://github.com/uiri/toml)

## Installation

To install a module run the command:

```pip install toml_config```

## Using

To get started, import the module. Create an instance of the Config class
by passing as a parameter the path to an existing file or the path where this file
will be created.And then you can read parameters from the file and write parameters to the file.

Example.
Creating a file and writing values.

```main.py```:
```python
from toml_config.core import Config

my_config = Config('app.config.toml')
my_config.add_section('app').set(key='value',other_key=[1,2,3])
```



```app.config.toml```:
```toml
[app]
key = "value"
other_key = [ 1, 2, 3,]
```
