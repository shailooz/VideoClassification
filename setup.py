# run pip install setup.py to getting essential libraries for running this project 

from setuptools import setup, find_packages
setup(name='Action-Classifier',
      version='1.0',
      description='3D cnn action classifier',
      author='Shailesh Sivan',
      author_email='shaileshsivan@gmail.com',
      install_requires=['numpy==1.19.0', 'numpydoc==0.9.1', 'keras==2.3.1', 'keras-applications==1.0.8', 'keras-preprocessing==1.1.0', 'scikit-learn==0.21.3', 'cloudpickle==1.2.2', 'pickleshare==0.7.5', 'matplotlib==3.2.1', 'opencv-contrib-python==4.2.0.34', 'cvlib==0.2.5', 'json5==0.8.5', 'jsonschema==3.0.2', 'pandas==0.25.1',  'youtube-dl==2020.7.28', 'opencv-python==4.1.2.30'],
     )
