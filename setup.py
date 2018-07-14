from setuptools import setup, find_packages
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []

if use_cython:
    ext_modules.append(Extension("joblist.trees_cython", ['joblist/trees_cython.pyx']))
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules.append(Extension("joblist.trees_cython", ['joblist/trees_cython.c']))


#ext_modules.append(Extension('joblist', ['joblist/Lookup_data_new_v2.pickle']))
setup(name='joblist',
      version='0.2',
      description="A Python implementation of pydepth",
      long_description="A Python implementation of JobList (Data Extraction with Partial Tree Alignment)",
      author="Sellamani",
      author_email="mail2.sella@gmail.com",
      install_requires=['w3lib'],
      packages=find_packages(),
      include_package_data=True,
      cmdclass=cmdclass,
      ext_modules=ext_modules
)
