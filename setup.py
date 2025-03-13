from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as readme:
    _readme_c = readme.read()

if __name__ == "__main__":
    setup(
        name="pysaber",
        version="0.0.1",
        description="Receiving query models for generating DSL source code, saber also includes DAO, interception and database behavior logging capabilities.",
        long_description=_readme_c,
        long_description_content_type="text/markdown",
        author="drash",
        author_email="drawmoonsh@outlook.com",
        url="https://github.com/drawmoon/pysaber",
        package_dir={"": "pysaber"},
        packages=find_packages(where="pysaber"),
        license="Apache License",
        python_requires=">=3.8",
        install_requires=[],
    )
