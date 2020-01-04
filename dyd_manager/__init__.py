import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dyd",
    version="0.0.1",
    author='Ebrima Tunkara',
    author_email="ebrimatunkara@gmail.com",
    description="Dynamic data-driven framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tunks/dyd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)