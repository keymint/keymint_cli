from setuptools import find_packages
from setuptools import setup

setup(
    name='keymint_cli',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    extras_require={
        'completion': ['argcomplete'],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', [
            'resource/keymint_cli',
        ]),
        ('share/keymint_cli', [
            'resource/local_setup.bash',
            'resource/local_setup.zsh',
        ]),
        ('share/keymint_cli/environment', [
            'completion/keymint-argcomplete.bash',
            'completion/keymint-argcomplete.zsh'
        ]),
    ],
    author='Ruffin White',
    author_email='ruffin@osrfoundation.org',
    maintainer='Ruffin White',
    maintainer_email='ruffin@osrfoundation.org',
    url='https://github.com/keymint/keymint_cli/tree/master/keymint_cli',
    download_url='https://github.com/keymint/keymint_cli/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='Framework for keymint command line tools.',
    long_description="""\
The framework provides a single command line script which can be extended with
commands and verbs.""",
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'keymint_cli.command': [
            'extension_points ='
            ' keymint_cli.command.extension_points:ExtensionPointsCommand',
            'extensions = keymint_cli.command.extensions:ExtensionsCommand',
        ],
        'keymint_cli.extension_point': [
            'keymint_cli.command = keymint_cli.command:CommandExtension',
        ],
        'console_scripts': [
            'keymint = keymint_cli.cli:main',
        ],
    }
)
