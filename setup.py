import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mykoreanromanizer", 
    version="1.0.1",
    author="Teresa Garcia",
    author_email="teresagar181@gmail.com",
    description="Korean romanizer based on the Revised Romanization of Korean",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teresagarcia/my-korean-romanizer",
    keywords = ['Korean', 'Romanizer'],  
    install_requires=[
        'jamo'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
