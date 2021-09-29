#!/usr/bin/env python
import sys
from dotenv import read_dotenv
from os import getenv


def main():
    # Enviroment
    if getenv('DJANGO_ENVIROMENT') == 'development':
        read_dotenv(dotenv='.env')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Couldnt import Django. Are you sure its installed and '
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
