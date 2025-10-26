from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    description="A sample Python project",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        'requests',          # Add required dependencies here
        'numpy',
    ],
    extras_require={         # Optional: Specify additional groups of dependencies
        'dev': [
            'pytest',        # Dependencies for development and testing
            'flake8',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_project=usecases.main:main_function',
        ],
    },
    test_suite='tests',      # Automatically discover tests
)
