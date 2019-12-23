from distutils.core import setup

# noinspection PyUnresolvedReferences
import setuptools

setup(
    name='Google Colab Transfer',
    packages=['colab_transfer'],
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    version='0.1.3',
    description='Transfer data between Colab and Drive.',
    long_description='Transfer data between Colab and Drive.',
    long_description_content_type='text/x-rst',
    author='Wok',
    author_email='wok@tuta.io',
    url='https://github.com/woctezuma/google-colab-transfer',
    download_url='https://github.com/woctezuma/google-colab-transfer/archive/0.1.3.tar.gz',
    keywords=['google-colab', 'google-colaboratory', 'google-drive'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

