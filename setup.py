from setuptools import setup, find_packages

setup(
    name="redis_helper_kit",  # Name of your package
    version="0.1.0",  # Initial version number
    description="A helper library for Redis CRUD operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Use markdown for README if applicable
    author="Abhishek Prakash",
    author_email="abhishekprakash47@gmail.com",
    url="https://github.com/abhishekprakash256/redis_helper_kit",  # Optional, your project URL
    packages=find_packages(exclude=["tests*"]),  # Finds all packages in your project except tests
    install_requires=[
        "redis>=4.0.0",  # Specify dependencies; adjust the version as needed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version
)
