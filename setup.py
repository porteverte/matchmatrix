from setuptools import setup 

with open("README.md", 'r') as f:
    long_description = f.read()

setup( 
    name='matchmatrix', 
    version='2.0.2', 
    description='Customisable class to produce a matrix of match scores across multiple dimensions',
    author='Porte Verte', 
    author_email='porte_verte@outlook.com', 
    url='https://github.com/porteverte/matchmatrix',
    packages=['matchmatrix'],
    package_dir={'':'src'},
    python_requires=">=3.8",
    install_requires=['rapidfuzz==1.9.1', 'unidecode==1.2.0', 'pandas==1.3.5','numpy==1.20.3'],
)