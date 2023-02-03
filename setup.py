from setuptools import setup 
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="Topsis_Pranav_102003432",version="0.13",
description="This is a topsis package of version 0.13",
long_description=long_description,
    long_description_content_type="text/markdown",
author="Pranav Singh",
author_email="psingh2_be20@thapar.edu",
packages=['Topsis_Pranav_102003432'],
install_requires=['pandas'],
include_package_data=True,
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Pranav_102003432.Pranav_102003432:main",
        ]
    }
)

