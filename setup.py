from setuptools import find_packages, setup

setup(
    name="itakello_logging",
    version="0.2.1.7",
    author="Itakello",
    author_email="maxste000@gmail.com",
    description="A custom logging library by Itakello",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Itakello/itakello_logging",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    extras_require={
        "dev": [
            "mypy",  # Type checker
            "pytest",  # Testing framework
            "black", # Code formatter
            "flake8", # Code linter
            "setuptools", # Packaging tool
        ],
    },
    python_requires=">=3.10",
)
