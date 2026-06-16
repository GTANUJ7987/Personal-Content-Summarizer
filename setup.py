import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.1.0"

REPO_NAME = "Content-Summarizer"
AUTHOR_USER_NAME = "GTANUJ7987"
SRC_REPO = "ContentSummarizer"    
AUTHOR_EMAIL = "g.srinivasrao60@gmail.com"
DESCRIPTION = "A Python package to interact with Azure DevOps REST API."
LONG_DESCRIPTION = long_description
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
URL = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language <IP_ADDRESS> Python <IP_ADDRESS> 3",
        "License <IP_ADDRESS> OSI Approved <IP_ADDRESS> MIT License",
        "Operating System <IP_ADDRESS> OS Independent",
    ],
    install_requires=[line.strip() for line in open('requirements.txt').readlines() if line.strip() and not line.startswith('#') and not line.startswith('-e .')],
)  