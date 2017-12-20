from setuptools import setup, find_packages

setup(
    name='data-collectors',
    version='0.1.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=['Private :: Do Not Upload'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
