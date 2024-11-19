from setuptools import setup

setup(
    name='GODE_pkg',
    version='0.0.1',
    description='GODE_pkg pip install',
    url='https://github.com/seoyeonc/GODE_pkg.git',
    author='seoyeonchoi',
    author_email='chltjdus1212@gmail.com',
    license='seoyeonc',
    packages=['GODE_pkg'],
    zip_safe=False,
    install_requires=[
        'torch==2.0.1',
        'scipy==1.10.1',
        'statsmodels==0.14.0']
)