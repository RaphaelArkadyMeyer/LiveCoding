from setuptools import setup

setup(
    name='testcl-click',
    version='1.0',
    py_modules=['testcl'],
    include_package_data=True,
    install_requires=[
        'click',
        # Colorama is only required for Windows.
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        testcl=testcl:cli
    ''',
)