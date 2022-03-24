import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dist_example",
    version="0.0.1",
    author="Bruno De Deken",
    author_email="dedekenbruno@gmail.com",
    description="Example repository regarding python distributions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy>=1.22.3"
    ],
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
)
