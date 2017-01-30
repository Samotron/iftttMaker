from distutils.core import setup

setup(name='iftttMaker',
      version='0.1',
      description ='super simple ifttt maker channel',
      url='http://github.com/samotron/iftttmaker',
      author= 'Sam Rogers',
      author_email='jasarogers@gmail.com',
      license='none',
      packages=['iftttmaker'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
