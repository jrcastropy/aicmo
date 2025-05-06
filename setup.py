from setuptools import setup, find_packages

VERSION = '0.0.1'
# Read the contents of requirements.txt and make it a list
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Setting up
setup(
    name="aicmo_clients",
    version=VERSION,
    author="Jayr Castro",
    author_email="jayrcastro.py@gmail.com",
    description="A package for using aicmo functions and tools",
    long_description_content_type="text/markdown",
    long_description='A package for using aicmo functions and tools, includes scraping, openai with an options where you can use it in a serverless application such as AWS Lambda and GCP Cloud Function',
    packages=find_packages(),
    install_requires=requirements,
    keywords=[
        'aicmo'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)