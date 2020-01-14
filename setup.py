import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlk_cloud",
    version="0.0.1",
    author="Francis Josue De la Cruz",
    author_email="francis.delacruz@hundred.com.pe",
    description="A small AWS example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1311543/belc-dlk-archetype-aws.git",
    packages=setuptools.find_packages(),
    classifiers=[
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        #'Programming Language :: Python :: 3.6',
        #'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'request',
        'botocore>1.13.30',
        'awscli>1.16',
        'boto3>1'
    ],
    python_requires='>=3.*, <4'
)
