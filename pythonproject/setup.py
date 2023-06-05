from setuptools import setup

setup(
    name='IMviz',
    version='0.1',
    author='Yingjie Bian, Din Hida, Florian Lang',
    description='This application provides a back-end for getting step-by-step information of inductive miner algorithms using pm4py',
    install_requires=[
        'numpy>=1.24.1',
        'pandas>=1.5.2', 
        'networkx>=3.0',
        'lxml>=4.9.2',
        'graphviz>=0.20.1',
        'Flask>=2.2.2',
        'Flask-Cors>=3.0.1',
        'gunicorn>=20.1.0',
        'requests',
        'pm4py @ git+https://github.com/badrecursionbrb/pm4py-core.git#egg=pm4py'
    ],
    packages=['IMviz']
)