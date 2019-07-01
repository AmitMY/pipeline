from distutils.core import setup

setup(
    name='pipeline',
    packages=['cached-pipeline'],
    version='0.1',
    license='MIT',
    description='This class manages your runtime components in terms of order and caching.',
    author='Amit Moryossef',
    author_email='amitmoryossef@gmail.com',
    url='https://github.com/AmitMY/cached-pipeline',
    download_url='https://github.com/AmitMY/cached-pipeline/archive/v_01.tar.gz',
    keywords=['pipeline'],  # Keywords that define your package best
    install_requires=[
        'numpy',
        'Pillow',
    ]
)