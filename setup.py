try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pymakec import __version__

config = {
    'name': 'pymakec',
    'author': 'Garrett Berg',
    'author_email': 'garrett@cloudformdesign.com',
    'version': __version__,
    'pymodules': ['pymakec'],
    'license': 'MIT',
    'install_requires': [
        'six',
    ],
    'extras_require': {
    },
    'description': "Create makefiles using python (2 or 3)",
    'url': "https://github.com/cloudformdesign/pymakec",
    'classifiers': [
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**config)
