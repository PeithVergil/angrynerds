from distutils.core import setup

import py2exe

includes = []
excludes = []
packages = []

setup(
	options = {
		'py2exe': {
			'optimize'     : 2,
			'includes'     : includes,
			'excludes'     : excludes,
			'packages'     : packages,
			'compressed'   : 2,
			'bundle_files' : 1,
		}
	},
	windows = [
		'main.py'
	],
	zipfile = None
)