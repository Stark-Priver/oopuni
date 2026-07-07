from setuptools import setup, find_packages

setup(
    name="oop-uni",
    version="1.0.0",
    description="OOP UNI: The Journey Through MUST - A Story-Driven Educational Adventure Game",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Enock Stanslaus",
    author_email="enockstanslaus26@gmail.com",
    url="https://github.com/Stark-Priver/oopuni",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "pygame-ce>=2.5.0",
    ],
    entry_points={
        "console_scripts": [
            "oop-uni=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: Games/Entertainment :: Simulation",
    ],
)
