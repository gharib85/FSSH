from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(name='fssh',
    version='0.6',
    description='Quantum-Classical Mudslides',
    packages=['fssh'],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'fssh = fssh.__main__:main',
            'surface = fssh.surface:main'
        ]
    },
    zip_safe=False
)

