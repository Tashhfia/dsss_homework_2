from distutils.core import setup
from setuptools import find_packages


setup(
    name="math_quiz",
    version="1.1.0",
    author="Tashfia",
    description="A Python package for generating random math problems and quizzes.",
    packages=find_packages(),
    python_requires=">=3.6",
)