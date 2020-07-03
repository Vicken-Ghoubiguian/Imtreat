from setuptools import setup

with open("README.md", "r") as fh:
	readme_description = fh.read()

setup(name='imtreat',
version='0.1',
description='Python package to make images treatment easily to deploy on the PyPi platform',
long_description=readme_description,
long_description_content_type="text/markdown",
url='#',
author='Wicken',
author_email='eric.ghoubiguian@imerir.com',
license='MIT',
packages=['imtreat'],
install_requires=['opencv-contrib-python', 'pyttsx3'],
zip_safe=False,
python_requires='>=3.8.2')
