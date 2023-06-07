from setuptools import setup, find_packages

setup(
    name="taceconomics",
    version="0.2",
    description="Python client library for TAC ECONOMICS API",
    author="TAC ECONOMICS",
    author_email="info@taceconomics.com",
    url="https://github.com/taceconomics/taceconomics-python",
    install_requires=["requests", "pandas"],
    packages=find_packages()
)
