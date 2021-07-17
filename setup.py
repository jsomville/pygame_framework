from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Framework for pygame'
LONG_DESCRIPTION = 'A framework to better handle scenes and menu for pygame'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="jsbmath", 
        version=VERSION,
        author="JSB",
        author_email="email@domain.com",
        url="https://github.com/jsomville/pygame_framework",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'singleton3',
            'pygame'],
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
) 
