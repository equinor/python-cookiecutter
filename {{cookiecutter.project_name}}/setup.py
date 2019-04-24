#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name = '{{ cookiecutter.distribution_name }}',
    description = '{{ cookiecutter.short_description }}',

    author = 'Equinor',
    author_email = '{{ cookiecutter.email }}',
    url = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',

    project_urls = {
        'Documentation': 'https://{{ cookiecutter.distribution_name }}.readthedocs.io/',
        'Issue Tracker': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
    },
    keywords = [
    ],

    license = '{{ cookiecutter.open_source_license }}',

    packages = [
        '{{ cookiecutter.package_name }}',
    ],
    platforms = 'any',

    install_requires = [
{%- if cookiecutter.command_line_interface == 'click' %}
        'click',
{% endif %}
    ],

    setup_requires = [
        'setuptools >=28',
        'setuptools_scm',
        'pytest-runner'
    ],

    tests_require = [
        'pytest',
    ],

{% if cookiecutter.command_line_interface != 'None' -%}
    entry_points = {
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:main',
        ],
    },
{%- endif %}

    use_scm_version = {
        'write_to': '{{ cookiecutter.package_name }}/version.py',
    },
)
