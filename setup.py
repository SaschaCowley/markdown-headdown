import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="markdown-headdown",
    version="0.1.3",
    author="Sascha Cowley",
    description="A Python-Markdown extension to downgrade headings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaschaCowley/Markdown-Headdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules ",
            "Topic :: Text Processing :: Filters ",
            "Topic :: Text Processing :: Markup :: HTML ",
    ],
    install_requires=['markdown>=3'],
    keywords="markdown headings downgrade demote lower",
)