import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mykoreanromanizer", 
    version="0.1.5",
    author="Teresa Garcia",
    author_email="teresagar181@gmail.com",
    description="Custom Korean romanizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teresagarcia/my-korean-romanizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)