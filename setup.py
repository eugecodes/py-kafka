from setuptools import find_packages, setup

setup(
    name='lifecycle',
    packages=find_packages(include=['lifecycle']),
    version='0.1.0',
    description='Lifecycle Lib',
    author='',
    license='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
