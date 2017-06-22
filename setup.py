from setuptools import setup

setup(name='random_pass_generator',
      version = '1.0',
      description = 'Generate secure passwords / passphrases',
      author = 'Loic Reisdoerfer',
      author_email = 'reisdoerferloic@protonmail.com',
      packages = ['random_pass_gen'],
      zip_safe = False,
      install_requires=['tqdm']
      )
