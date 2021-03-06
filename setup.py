import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-colorconverter',
    version='0.0.6',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Converter to convert between various color systems such as RGB, CIELAB, CMYK, HEX, RGB, and XYZ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['colorconverter'],
    packages=['mindpowered_colorconverter'],
    package_dir={'mindpowered_colorconverter': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
