from setuptools import setup, find_packages

setup(
    name = 'tmon',
    version = '0.1.0',
    packages = find_packages(exclude=[]),
    install_requires=[
        "click==7.1.2",
        "cycler==0.10.0",
        "kiwisolver==1.3.1",
        "matplotlib==3.3.3",
        "numpy==1.19.4",
        "pandas==1.1.4",
        "Pillow==8.0.1",
        "pyparsing==2.4.7",
        "pyserial==3.5",
        "python-dateutil==2.8.1",
        "pytz==2020.4",
        "six==1.15.0",
    ],
    entry_points = {
        'console_scripts': [
            'tmon = tmon.main:cli'
        ]
    })
