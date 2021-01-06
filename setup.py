import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YOUR PACKAGE NAME", # It should be unique name
    version="0.0.1",
    author="Name of Author",
    author_email="author@email.com",
    description="A small title of the package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mysite.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
install_requires=[
        "numpy==1.18.1",
        "pandas==1.1.5",
    ],

    python_requires='>=3.6',


)
