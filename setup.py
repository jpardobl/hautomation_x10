import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='hautomation_x10',
    version='0.11',
    packages=['hautomation_x10'],
    include_package_data=True,
    license='BSD License',
    description='Mochad wrapper to help issuing X10 commands',
    long_description=README,
#TODO set the project's home page
    url='http://blog.digitalhigh.es',
    author='Javier Pardo Blasco(jpardobl)',
    author_email='jpardo@digitalhigh.es',
    install_requires = (
      #"simplejson==2.6.2",
    ),
    test_suite='hautomation_x10.tests.main',
    #tests_require=("selenium", "requests"),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Home Automation',
    ],
    entry_points={
        "tdd": [
            "run_tests = hautomation_x10.tests.main",
        ],
        "cmds": [
            "pl_switch = hautomation_x10.cmds:pl_switch",
            "pl_dim = hautomation_x10.cmds:pl_dim",
            "pl_bri = hautomation_x10.cmds:pl_bri",
        ],
        "console_scripts": [
            "populate_x10_db = hautomation_x10.deploy:populate_db",
                    ]
    }
)
