from setuptools import setup, find_packages

setup(
    name='tags-generator',
    version='0.2.0',
    author='nigohiroki',
    author_email='nigohiroki@teit-inc.com',
    description='A library to generate tags list from a text using OpenAI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nigohiroki/tags-generator',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'openai',
    ],
)

