import setuptools

with open('README.MD','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "CNN_Classifier"
AUTHOR_USER_NAME = "Monish-Nallagondalla"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "nsmonish@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Monish-Nallagondalla/CNN_Classifier.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Monish-Nallagondalla/CNN_Classifier/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)