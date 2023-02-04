from setuptools import setup, find_packages
import re

with open("requirements.txt", encoding="utf-8") as r:
    requirements = [i.strip() for i in r]

with open("WhatsaPy/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="WhatsaPy",
    version=version,
    description="Unofficial python Wrapper for Whatsapp Businness API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rahulps100/WhatsAppPy",
    author="Rahul P S",
    author_email="rahulps1000@gmail.com",
    license="GPLv3",
    keywords="whatsapp api python businnes cloud unoffcial",
    python_requires="~=3.7",
    py_modules=["WhatsaPy"],
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requirements
)