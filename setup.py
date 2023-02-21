"""
dokumentasi setup tools : https://packaging.python.org/en/latest/tutorials/packaging-projects/
dokumentasi markdown : https://www.markdownguide.org/cheat-sheet/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latest_indonesia_earthquake",
    version="0.1",
    author="Yudha N. Alfian",
    author_email="yudhanurulalfian@gmail.com",
    description="this package will get the latest earthquake from BMKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yudha-nurul/latest-indonesia-earthquake",
    project_url={
        "Website": "https://yudhanurulalfian.wordpress.com",
    },
    classifiers=[
        "Programming Language ::Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)


"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author.@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_url={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issue",
    },
    classifiers=[
        "Programming Language ::Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
"""
