from setuptools import (
    setup,
    find_packages,
)


setup(name='FuberTaxi',
      version='0.1',
      description='Fuber Taxi',
      long_description='Solution to Fuber Taxi problem',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='taxi modelling problem',
      author='Himani Agrawal',
      author_email='himani93@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'falcon',
          'gunicorn',
      ],
      tests_require=['pytest'],
      setup_require=['pytest-runner'],
      include_package_data=True,
      entry_points={
          'console_scripts': ['fubertaxi=gunicorn fuber.app:api --reload --log-file logs.log'],
      },
      zip_safe=False)
