from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='toml_config',
    version='0.1.2',
    packages=['toml_config'],
    install_requires=['toml',],
    url='https://github.com/SemenovAV/toml_config',
    license='MIT',
    author='SemenovAV',
    author_email='7.on.off@bk.ru',
    description='Python library that simplifies parsing and creating Toml configuration files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
