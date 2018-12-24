import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read('README.md') if os.path.isfile("README.md") else ""

setup(
    name='bitcoin-etl',
    version='1.0.0',
    author='Evgeny Medvedev',
    author_email='evge.medvedev@gmail.com',
    description='Tools for exporting Bitcoin blockchain data to JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blockchain-etl/bitcoin-etl',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='bitcoin',
    python_requires='>=3.5.3,<3.8.0',
    install_requires=[
        'lru-dict==1.1.6',
        'requests==2.20.0',
        'python-dateutil==2.7.0',
        'click==7.0',
        'bitcoin==1.1.42',
    ],
    extras_require={
        'dev': [
            'pytest~=3.2.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'bitcoinetl=bitcoinetl.cli:cli',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/blockchain-etl/bitcoin-etl/issues',
        'Chat': 'https://gitter.im/ethereum-etl/Lobby',
        'Source': 'https://github.com/blockchain-etl/bitcoin-etl',
    },
)
