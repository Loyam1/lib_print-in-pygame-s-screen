from setuptools import setup, find_packages

setup(
    name='print_in_screen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pygame>=2.0.0',  # Version minimale recommandée
    ],
    author='Loyam',
    author_email='mayol.picard@gmx.fr',
    description='A library for displaying text more easily in PyGame',
    long_description_content_type='text/markdown',
    url='https://github.com/Loyam1/lib_print-in-pygame-s-screen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=3.8',
)