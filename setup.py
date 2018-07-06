import os
from setuptools import setup, Command, find_packages


class CleanCommand(Command):

    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./htmlcov ./spark-warehouse')


setup(
  name='spk_sample',
  version='1.0.0',
  description='Sample Spark app',
  url='https://github.com/viessmann/spk_sample',
  author='chtn',
  author_email='chtn@viessmann.com',
  packages=find_packages(),
  zip_safe=False,
  py_modules=['spk_sample.__main__:main'],
  cmdclass={
    'clean': CleanCommand
    }
  )
