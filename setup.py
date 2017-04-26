from setuptools import setup

setup(
  name = 'phoneid',
  packages = ['phoneid'],
  version = '0.1',
  description = 'A library to generate Indonesian phone numbers',
  author = 'Batista Harahap',
  author_email = 'batista@bango29.com',
  url = 'https://github.com/coralhq/phone-id',
  download_url = 'hhttps://github.com/coralhq/phone-id/archive/0.1.tar.gz',
  keywords = ['phone', 'number', 'indonesia', 'telco'],
  install_requires = [
    'phonenumbers'
  ],
  classifiers = [],
)