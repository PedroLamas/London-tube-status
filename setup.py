from setuptools import setup, find_packages

VERSION = "0.2"

REQUIRES = ["requests"]

setup(
    name="london-tube-status",
    version=VERSION,
    url="https://github.com/robmarkcole/London-tube-status",
    author="Robin Cole",
    author_email="robmarkcole@gmail.com",
    description="Parse London tube data into a dictionary",
    install_requires=REQUIRES,
    packages=find_packages(),
    license="Apache License, Version 2.0",
    python_requires=">=3.5",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
