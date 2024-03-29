import setuptools, os, sys, re
from grtoolkit.File import name, filesInFolder
from grtoolkit.Storage import search, regexList

packageName = "$package-name$"

with open("README.md", "r") as fh:
    long_description = fh.read()

CLSfilesearch = search(f"{packageName}/",depth=1,lastValue=True)[1] # Seach for all files in packagename folder
CLSfilesearch = regexList(CLSfilesearch,r"CLS_.*.py")               # Filter list for Command Line Scripts
CLS_List = [f"{name(file)[4:]} = {packageName}.{name(file)}:main" for file in CLSfilesearch]    #Create entry-points formatted list

# NOTE: PATHS CALCULATED IN SETUP.PY NEED UNIX STYLE PATH REFERENCES WITH DIFFERENT SLASHES

setuptools.setup(
    name=packageName,
    version="19.07.0",
    author="$author$",
    author_email="$email$",
    description="$description$",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="$url$",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[f'cmdline\\{file}' for file in search('cmdline/', depth=1, lastValue=True)[1]],
    entry_points={'console_scripts': CLS_List},
    install_requires=['grtoolkit'],                                                        # Add package dependencies (e.g. 'numpy')
    include_package_data=True,
)