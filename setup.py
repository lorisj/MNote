from setuptools import setup, find_packages
setup(
    name='mnote',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'lark-parser'
    ],
    author='Loris Jauatakas',
    author_email='lorisj@umich.edu',
    description='Parser and interpreter for .mnote files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lorisj/MNoteParser',
)