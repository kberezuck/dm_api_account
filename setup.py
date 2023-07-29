from setuptools import setup

REQUIRES = [
    'requests',
    'git+https://github.com/kberezuck/restclient.git',
    'pydantic',
    'structlog',
    'allure-pytest',

]
setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/kberezuck/dm_api_account.git',
    license='MIT',
    author='Ksenia_Berezuck',
    author_email='',
    install_requires=REQUIRES,
    description='dm_api_account with allure and login'
)
