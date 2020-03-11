from setuptools import setup

setup(
    name="TableGen",
    version='0.1',
    py_modules=["main", "tableParser"],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tableGen=main:main
    ''',
)