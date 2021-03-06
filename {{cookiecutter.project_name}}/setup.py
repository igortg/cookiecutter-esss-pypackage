import setuptools

import io

with io.open("README.rst", encoding="UTF-8") as readme_file:
    readme = readme_file.read()

with io.open("CHANGELOG.rst", encoding="UTF-8") as changelog_file:
    history = changelog_file.read()

requirements = []
extras_require = {
    "docs": ["sphinx >= 1.4", "sphinx_rtd_theme", "sphinx-autodoc-typehints"],
    "testing": ["codecov", "pytest", "pytest-cov", "pytest-mock", "pre-commit", "tox"],
}
setuptools.setup(
    author='ESSS',
    author_email='foss@esss.co',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="{{ cookiecutter.package_description }}",
    extras_require=extras_require,
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    python_requires=">=3.6",
    keywords="{{ cookiecutter.package_name }}",
    name="{{ cookiecutter.project_name }}",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    url="http://github.com/ESSS/{{ cookiecutter.project_name }}",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    zip_safe=False,
)
