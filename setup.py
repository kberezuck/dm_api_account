from setuptools import setup

# REQUIRES = [
#     'requests',
#     'pydantic',
#     'structlog',
#     'allure-pytest',
#
# ]
setup(
    name='dm_api_account',
    version='0.0.2',
    packages=['dm_api_account', 'models', 'apis'],
    url='https://github.com/kberezuck/dm_api_account.git',
    license='MIT',
    author='Ksenia_Berezuck',
    author_email='',
    # install_requires=REQUIRES,
    description='dm_api_account with allure and login'
)
