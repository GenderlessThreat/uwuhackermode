from setuptools import setup, find_packages

setup(
    name='your_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your_project=your_project.cli:cli',
        ],
    },
)
