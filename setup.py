# Copyright (C) 2010 Florian Ledermann ledermann@ims.tuwien.ac.at

from setuptools import setup, find_packages
 
setup(
    name='python-flyingsaucer',
    version='0.1',
    description='A Python wrapper for generating PDFs using the Flying Saucer Java library.',
    author='Flo Ledermann',
    author_email='ledermann@ims.tuwien.ac.at',
    url='http://bitbucket.org/floledermann/pdfgen/',
    package_dir = {'': 'src/python'},
    packages=['flyingpython'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    # include_package_data=True,
    # zip_safe=False,
    # Tells setuptools to download setuptools_hg before running setup.py so
    # it can find the data files under Hg version control.
    # setup_requires=['setuptools_hg'],
)
