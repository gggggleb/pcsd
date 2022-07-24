from setuptools import setup

setup(
    name='pcsd',
    version='2.3',
    description='Pcsd server',
    url='https://git.glebmail.xyz/PythonPrograms/pcsd',
    author='gleb',
    packages=['pcsd'],
    author_email='gleb@glebmail.xyz',
    license='GNU GPL 3',
    scripts=['bin/pcsd'],
    install_requires=[
        'pyyaml',
    ],
)
