import setuptools
from distutils.core import setup, Extension

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="joblist",
    version="1.0.3",
    author="sellamani",
    author_email="mail2.sella@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    include_package_data=True,
    packages=setuptools.find_packages(),
##    ext_modules=[Extension('joblist', ['joblist/trees_cython.pyd','joblist/Lookup_data_new_v2.pickle'])],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

