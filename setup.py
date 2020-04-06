import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-Jwilson1172",
    version="0.0.2",
    author="Joseph Wilson",
    author_email="jw59615@gmail.com",
    description="A package with some simple ds tools for practicing twine syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jwilson1172/lambdata_Jwilson1172",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)