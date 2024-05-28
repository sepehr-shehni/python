#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to 'concert.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concert.settings')
    
    try:
        # Try to import execute_from_command_line function from django.core.management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or not available, raise ImportError with explanation
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command line arguments using Django's management utility
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If the script is executed as the main program, call the main function
    main()
