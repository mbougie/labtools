"""

Install {package}.

"""



def main():

	try:

		from setuptools import setup

	except ImportError:

		from distutils.core import setup



	config = {

		'description': 'tools for processing lab data',

		'author': 'Matt Bougie',

		'download_url': 'https://github.com/mbougie/labtools.git',

		'author_email': '{author_email}',

		'version': '0.1',

		'install_requires': [],

		'packages': ['labtools'],

		'scripts': ['bin/hello_world.py'],

		'entry_points': {

		    'console_scripts': [],

		},

		'name': 'labtools',

	}



	setup(**config)	



if __name__ == '__main__':

	main()


