from setuptools import setup

setup(
    name="pyls",
    version="1.0",
    py_modules=["pyls"],
    entry_points={
        "console_scripts": [
            "pyls = pyls:main",
        ],
    },
)