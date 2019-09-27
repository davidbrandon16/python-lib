from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bigquery-custom-davidbrandon16",
    version="0.0.1",
    author="David Brandon Wilando",
    author_email="david.wilando4@gmail.com",
    description="custom bigquery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidbrandon/python-lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
              'google-cloud-bigquery',
          ]
)