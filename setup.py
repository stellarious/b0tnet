import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='botnet',
    version='0.1.0',
    packages=[
        'botnet',
        'botnet.modules',
        'botnet.modules.builtin',
        'botnet.modules.builtin.mumble',
        'botnet.modules.lib'
    ],
    long_description=read('README.md'),
    install_requires=[
        'blinker',
        'Click',
        'requests',
        'xmltodict',
        'protobuf>=3.0.0b2',
    ],
    entry_points='''
        [console_scripts]
        botnet=botnet.cli:cli
    ''',
)
