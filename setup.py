from setuptools import setup, find_packages

setup(
    name="datascience",
    version="0.0.1",
    author="Darius",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
