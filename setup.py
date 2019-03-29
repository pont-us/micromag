"""Setup script for anisoms"""

import os.path
from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.md")) as fh:
    long_desc = fh.read()

setup(
    name="micromag",
    version="0.0.0",
    author="Pontus Lurcock",
    author_email="pont@talvi.net",
    description="Read data from Micromag magnetometers",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/pont-us/micromag",
    classifiers=[
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
    ],
    packages=["micromag"],
    install_requires=[
        "numpy", "matplotlib"
    ],
    entry_points={"console_scripts":
                    ["micromag-plot=micromag.micromag:main"]
                  },
)
