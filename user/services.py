import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """
    Validates a phone number using a regular expression.

    Args:
        value (str): The phone number to be validated.

    Raises:
        ValidationError: If the phone number is not in the format "+37012345678" or if it contains spaces, parentheses, or hyphens.

    Returns:
        str: The validated
    """
    
    phone_regex = re.compile(r'^\+?1?\d{11}$')
    
    # Delete spaces, parentheses, hyphens
    phonen = value.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
    
    if not phone_regex.match(phonen):
        raise ValidationError(
            'Phone number must be entered in the format: +37012345678. Up to 11 digits allowed.'
        )
    
    if not phonen.startswith('+370'):
        raise ValidationError(
            'Phone number must start with "+370".'
        )