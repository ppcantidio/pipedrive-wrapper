from setuptools import find_packages, setup

setup(
    name="pipedrive.py",
    version="1.0.0",
    author="Pedro Cantidio",
    author_email="ppcantidio@gmail.com",
    description="A Python wrapper for the Pipedrive API",
    long_description="A Python wrapper that simplifies interaction with the Pipedrive API",
    url="https://github.com/ppcantidio/pipedrive.py",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "requests",
    ],
)
