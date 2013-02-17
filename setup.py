from distutils.core import setup

import py2exe

includes = []
excludes = ['email']
packages = []

dll_excludes = []

setup(
	name = 'Angry Nerds',
	author = 'Peith Vergil',
	version = '0.0.1',
	options = {
		'py2exe': {
			'optimize'     : 2,
			'includes'     : includes,
			'excludes'     : excludes,
			'packages'     : packages,
			'compressed'   : 2,
			'bundle_files' : 1,
			'dll_excludes' : dll_excludes,
		}
	},
	windows = [{
		'script': 'main.py', 'icon_resources': [(1, 'icon.ico')]
	}],
	zipfile = None
)