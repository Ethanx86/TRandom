import random
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='TRandom',  
     version='0.1',
     scripts=['random'] ,
     author="Ethan Eyob",
     author_email="ethaneyob15@gmail.com",
     description="A pseudo-random number generator based on time",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Ethanx86/TRandom",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )