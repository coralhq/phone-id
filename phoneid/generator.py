from .axis import PREFIXES as AXIS_PREFIXES
from .byru import PREFIXES as BYRU_PREFIXES
from .indosat import PREFIXES as INDOSAT_PREFIXES
from .lippo import PREFIXES as LIPPO_PREFIXES
from .sampoerna import PREFIXES as SAMPOERNA_PREFIXES
from .smartfren import PREFIXES as SMARTFREN_PREFIXES
from .telkomsel import PREFIXES as TELKOMSEL_PREFIXES
from .three import PREFIXES as THREE_PREFIXES
from .xl import PREFIXES as XL_PREFIXES
import random


def anything(length=8, international_prefix=False):
    prefixes = AXIS_PREFIXES + BYRU_PREFIXES + INDOSAT_PREFIXES + LIPPO_PREFIXES + SAMPOERNA_PREFIXES + SMARTFREN_PREFIXES + TELKOMSEL_PREFIXES + THREE_PREFIXES + XL_PREFIXES
    
    return generate_random_number(prefixes=prefixes,
                                  length=length,
                                  international_prefix=international_prefix)

def axis(length=8, international_prefix=False):
    return generate_random_number(prefixes=AXIS_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def byru(length=8, international_prefix=False):
    return generate_random_number(prefixes=BYRU_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def indosat(length=8, international_prefix=False):
    return generate_random_number(prefixes=INDOSAT_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def lippo(length=8, international_prefix=False):
    return generate_random_number(prefixes=LIPPO_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def sampoerna(length=8, international_prefix=False):
    return generate_random_number(prefixes=SAMPOERNA_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def smartfren(length=8, international_prefix=False):
    return generate_random_number(prefixes=SMARTFREN_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def telkomsel(length=8, international_prefix=False):
    return generate_random_number(prefixes=TELKOMSEL_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def three(length=8, international_prefix=False):
    return generate_random_number(prefixes=THREE_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def xl(length=8, international_prefix=False):
    return generate_random_number(prefixes=XL_PREFIXES,
                                  length=length,
                                  international_prefix=international_prefix)

def generate_random_number(prefixes, length=8, international_prefix=False):
    prefix = str(random.choice(prefixes))

    range_start = 10 ** (length - 1)
    range_end = (10 ** length) - 1

    number = str(random.randint(range_start, range_end))

    intl = '+62' if international_prefix else '0'

    return intl + prefix + number

def is_valid_number(number):
    import phonenumbers
    
    try:
        number = phonenumbers.parse(number, 'ID')
    except:
        return False

    return phonenumbers.is_possible_number(number)
