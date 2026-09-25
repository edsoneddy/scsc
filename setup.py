from setuptools import setup, find_packages

setup(
    name="scsc",
    version="1.3.1",
    packages=find_packages(),
    install_requires=[
        "pygments==2.19.2",
        "zss==1.2.0",
        "csim==3.3.0"
    ],
    author="Eddy Lecoña",
    author_email="crew0eddy@gmail.com",
    description="Source Code Similarity Checker is tool for analyzing code snippets and detecting similarities.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/EdsonEddy/scsc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    keywords="code analysis, similarity detection, plagiarism detection, code snippets, code comparison",
    project_urls={
        "Bug Tracker": "https://github.com/EdsonEddy/scsc/issues",
        "Documentation": "https://github.com/EdsonEddy/scsc/wiki",
        "Source Code": "https://github.com/EdsonEddy/scsc",
    },
    python_requires='>=3.9',
    platforms=["All"],
    entry_points={
        'console_scripts': [
            'scsc=scsc.main:main',
        ],
    },
    license="MIT",
)