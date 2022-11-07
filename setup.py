import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="recapitulate",
    version="0.0.1",
    description="Python library to quickly summarize data in an Excel spreadsheet",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dancornell/recapitulate",
    author="Dan Cornell",
    author_email="dan@malicious.enterprises",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["recapitulate, recapitulate.utils"],
    include_package_data=True,
    install_requires=["pandas"],
)
