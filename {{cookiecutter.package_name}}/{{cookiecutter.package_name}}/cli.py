#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''{{ cookiecutter.package_name }}

Usage:
  {{ cookiecutter.package_name }} ship new <name>...
  {{ cookiecutter.package_name }} ship <name> move <x> <y> [--speed=<kn>]
  {{ cookiecutter.package_name }} ship shoot <x> <y>
  {{ cookiecutter.package_name }} mine (set|remove) <x> <y> [--moored|--drifting]
  {{ cookiecutter.package_name }} -h | --help
  {{ cookiecutter.package_name }} --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.full_name }}"


def main():
    '''Main entry point for the {{ cookiecutter.package_name }} CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()
