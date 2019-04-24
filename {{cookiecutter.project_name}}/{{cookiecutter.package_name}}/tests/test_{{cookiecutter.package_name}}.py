import pytest  # noqa: F401
{% if cookiecutter.command_line_interface != 'None' -%}
from .. import cli

def test_main():
    _ = cli.main([])
{% else %}
def test_assert():
    assert True
{%- endif %}
