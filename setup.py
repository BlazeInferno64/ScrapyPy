from setuptools import setup
from src.app import app_description

setup(
    name = "ScrapyPy",
    version = "1.0.0",
    description = app_description,
    author = "BlazeInferno64",
    url = "https://github.com/blazeinferno64/ScrapyPy",
    license = "MIT",
    requires = ['requests', 'tabulate', 'bs4']
)