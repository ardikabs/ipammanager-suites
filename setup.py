from ipammanager import (
    __version__,
    __author__,
    __email__,
    __url__,
    __description__
)
from setuptools import setup, find_packages
setup(
    name='ipammanager',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url=__url__,
    description=__description__,
    py_modules=['ipammanager'],
    install_requires=["click", "click_configfile", "requests"],
    packages=find_packages(),
    entry_points = '''
        [console_scripts]
        ipammanager=ipammanager.scripts.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)