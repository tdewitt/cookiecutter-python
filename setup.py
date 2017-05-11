import setuptools

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: System Administrators',
    ],
)
