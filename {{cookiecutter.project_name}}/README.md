{% set is_open_source = 'Not open source' not in cookiecutter.open_source_license -%}
# {{ cookiecutter.project_name }} #

{% if is_open_source -%}
{%- if cookiecutter.pypi == 'yes' -%}
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }})
{% endif -%}
[![travis](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?label=travis)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
[![readthedocs](https://readthedocs.org/projects/{{cookiecutter.distribution_name }}/badge/?version=latest)](https://{{cookiecutter.distribution_name }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}

{{ cookiecutter.short_description }}

## Index ##

* [Introduction](#introduction)
* [Features](#features)
* [Getting started](#getting-started)
{%- if cookiecutter.pypi == 'yes' %}
    * [Get from pypi](#get-from-pypi)
{% endif -%}
* [Tutorial](#tutorial)
{%- if is_open_source %}
* [Contributing](#contributing)
{% endif -%}
* [Examples](#examples)
    * [Hello world](#hello-word)

## Features ##

* Prints hello world
{%- if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{%- endif %}

## Getting started ##

{% if cookiecutter.pypi == 'yes' %}
### Get from pypi ###

```pip install {{ cookiecutter.distribution_name }}```
{% endif %}

## Tutorial ##

{% if is_open_source %}
## Contributing ##

We welcome all kinds of contributions, including code, bug reports, issues,
feature requests, and documentation.
{% endif %}

## Examples ##

### Hello world ###

```python3
    print('Hello world')
```
