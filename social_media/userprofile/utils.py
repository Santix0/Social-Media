from django.core.exceptions import ValidationError

from enum import Enum


def validation_of_number(number: int) -> None:
    if number < 0 and number != 11:
        raise ValidationError(
            f'{number} is not valid',
            params={'number': number},
        )
