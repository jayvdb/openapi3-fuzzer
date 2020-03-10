from distutils.core import setup
import setuptools

setup(
    name='openapi3-fuzzer',
    packages=setuptools.find_packages(),
    version='0.1',
    license='gpl-3.0',
    description='Openapi3 fuzzer',
    author='VolkerWessels Telecom',
    author_email='opensource@vwt.digital',
    url='https://github.com/vwt-digital/openapi3-fuzzer/tree/master',
    keywords=['Openapi3', 'fuzzer', 'vwt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'adal==1.2.2',
        'attrs==19.3.0',
        'certifi==2019.11.28',
        'cffi==1.13.2',
        'chardet==3.0.4',
        'cryptography==2.8',
        'idna==2.8',
        'importlib-metadata==1.3.0',
        'jsonschema==3.2.0',
        'more-itertools==8.0.2',
        'openapi-spec-validator==0.2.8',
        'prance==0.17.0',
        'pycparser==2.19',
        'PyJWT==1.7.1',
        'pyrsistent==0.15.6',
        'python-dateutil==2.8.1',
        'PyYAML==5.2',
        'requests==2.22.0',
        'semver==2.9.0',
        'six==1.13.0',
        'urllib3==1.25.7',
        'zipp==0.6.0'
    ],
    python_requires='>=3.6',
)
