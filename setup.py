import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-colorconverter',
    version='0.0.1',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="CPAL-1.0",
    url="https://mindpowered.dev/",
    description="ColorConverter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['colorconverter'],
    packages=['mindpowered_colorconverter'],
    package_dir={'mindpowered_colorconverter': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
