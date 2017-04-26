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

## License

Copyright 2017 Batista Harahap

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
