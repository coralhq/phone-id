# Phone Number Generator - Indonesia

This library generates Indonesian phone number. Numbers may or may not be valid.

## Generating Phone Numbers

```python
import phoneid

# Any operator
phone_number = phoneid.anything(length=8
                                international_prefix=False)

# Axis
phone_number = phoneid.axis(length=8
                            international_prefix=False)

# Byru
phone_number = phoneid.byru(length=8
                            international_prefix=False)

# Indosat
phone_number = phoneid.indosat(length=8
                               international_prefix=False)

# Lippo
phone_number = phoneid.lippo(length=8
                             international_prefix=False)

# Sampoerna
phone_number = phoneid.sampoerna(length=8
                                 international_prefix=False)

# Smartfren
phone_number = phoneid.smartfren(length=8
                                 international_prefix=False)

# Telkomsel
phone_number = phoneid.telkomsel(length=8
                                 international_prefix=False)

# Three
phone_number = phoneid.three(length=8
                             international_prefix=False)

# XL
phone_number = phoneid.xl(length=8
                          international_prefix=False)
```

`length` - The length after the international prefix and operator code

`international_prefix` - If set to `True` will prefix with `+62` else it will prefix with `0`.

## Validating

This library comes with [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) as its dependency. Quoted from its Github page:

>This is a Python port of [Google's libphonenumber library](https://github.com/googlei18n/libphonenumber) It supports Python 2.5-2.7 and Python 3.x (in the same codebase, with no 2to3 conversion needed).

A thin wrapper is available with the example below:

```python
import phoneid

number = phoneid.anything(length=8,
                          international_prefix=True)

number_is_valid = phoneid.is_valid_number(number)
```

## Using

Add this in your `requirements.txt`:

```
phoneid
```

## License

Please see `LICENSE.txt`.
