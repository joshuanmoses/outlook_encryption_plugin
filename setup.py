from setuptools import setup

setup(
    name="OutlookEncryptionPlugin",
    version="1.0",
    description="Outlook plugin for RSA-4096 email encryption",
    author="Your Name",
    packages=["plugin"],
    install_requires=[
        "pywin32",
        "pycryptodome",
        "pyqt5"
    ],
)
