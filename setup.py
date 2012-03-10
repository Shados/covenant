from setuptools import setup

setup(name='covenant',
      version='0.1.0',
      description='Code contracts for Python 3',
      author='Kamil Kisiel',
      author_email='kamil@kamilkisiel.net',
      url='http://pypi.python.org/pypi/covenant',
      license="BSD License",
      packages=["covenant"],
      keywords="contract",
      platforms=["All"],
      install_requires=["decorator"],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'],
     )