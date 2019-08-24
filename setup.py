# import os
from setuptools import setup, find_packages

setup(
    name='my_pip_app',
    version='0.5.0',
    description='For building a python project',
    author='S3RF',
    author_email='hanse.fjeld@gmail.com',
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['scipy', 'numpy', 'matplotlib', 'flask', 'werkzeug', 'Serial' , 'ino'],
    include_package_data=True,
    package_data={
        'app.static': ['*'],
        'app.templates': ['*.html'],
    },
    entry_points={
        'console_scripts': [
            'my_pip_app=app.main:main'
        ],
    }
)
