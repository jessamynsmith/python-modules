from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name="adobe-python-modules",
    version=version,
    author="Adobe",
    url="https://github.com/jessamynsmith/python-modules",
    description="Adobe utilities for fonts. These utilities are used and required by some of the"
                "Python scripts available in the other repositories.",
    long_description=open('README.md').read(),
    keywords=['font', 'adobe'],

    install_requires=[],
    tests_require=[],

    packages=['.'],

    entry_points={},

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development",
        "Topic :: Utilities",
    ])
