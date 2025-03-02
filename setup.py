from setuptools import setup, find_packages

setup(
    name="archivyx",
    version="0.1",
    author="Cyber",
    description="A powerful collection of utilities for terminal applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CyberBeast1/archivyx",
    packages=find_packages(),
    package_data={"archivyx": ["assets/archivyx.svg"]},
    install_requires=[
        "rich",
        "keyboard",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
