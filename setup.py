from distutils.core import setup

setup(
    name='masks',
    version='0.1.2',
    author='Nigel Cleland',
    author_email='nigel.cleland@gmail.com',
    packages=['masks'],
    scripts=[],
    url='http://pypi.python.org/pypi/masks/',
    license='LICENSE.txt',
    description='Syntactic sugar for data filtering with pandas.',
    long_description=open('README.rst').read(),
    install_requires=[
        "pandas >= 0.11.0",
        "numpy >= 1.7.1",
    ],
)
