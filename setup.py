from setuptools import setup
import os

print(
    os.path.join(os.getcwd(), "requirements.txt"),
    os.listdir(),
    "requirements.txt" in os.listdir(),
)

with open(os.path.join(os.getcwd(), "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(os.path.join(os.getcwd(), "requirements.txt")) as f:
    required = f.read().splitlines()

setup(
    name="pydal-rqlite",
    version="0.1.0",
    description="Custom pyDAL adapter for rqlite (distributed SQLite)",
    url="https://github.com/educationwarehouse/edwh-ghost",
    author="Education Warehouse",
    author_email="robin.vdn@educationwarehouse.nl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["pydal_rqlite"],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=required,
    # extras_require={"dev": dev_required},
)
