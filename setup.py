import setuptools

name = "Disha"
author = "ItzSjDude"
author_email = "Support@ItzSjDude.in"
description = "A Secure and Optimized Python Based Library."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/ItzSjDude/Disha"
setuptools.setup(
    name=name,
    version="v1.0",
    author=author,
    author_email=author_email,
    description=description,
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
