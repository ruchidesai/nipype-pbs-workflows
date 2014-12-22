from distutils.core import setup
setup(name='nipype-pbs-workflows',
      version='1.0',
      description='Neuroimaging workflows writtten in nipype with a focus on PBS job scheduler',
      py_modules=['bedpostx', 'dcm2niiconverter'],
      )