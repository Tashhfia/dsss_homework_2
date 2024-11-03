from setuptools import setup

setup(
    name="math_quiz",
    version="0.1.0",
    description="A Python package for generating random math problems and quizzes.",
    python_requires=">=3.6",
        entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz'
        ],}
)