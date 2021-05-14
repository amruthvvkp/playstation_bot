import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Playstation Bot",
    version="0.0.1",
    author="Amruth VVKP, Varshith VVS",
    author_email="amruthvvkp@gmail.com, svvarsham@gmail.com",
    description=("Bot to scrap websites looking for PS5 stock."),
    url="https://github.com/amruthvvkp/playstation_bot",
    packages=["src", "tests"],
    long_description=read("README"),
)
