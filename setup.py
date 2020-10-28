import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Google Colab Transfer',
    version='0.1.6',
    author='Wok',
    author_email='wok@tuta.io',
    description='Transfer data between Colab and Drive.',
    keywords=['google-colab', 'google-colaboratory', 'google-drive'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woctezuma/google-colab-transfer',
    download_url='https://github.com/woctezuma/google-colab-transfer/archive/0.1.6.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
