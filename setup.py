import setuptools

setuptools.setup(
    name='destiny',
    version='1.0',
    author="@phor3nsic",
    author_email="phorensic@pm.me",
    description="The tool of recon in domains",
    scripts=['destiny.py'],
    packages=setuptools.find_packages(),
    install_requires=['aiodns'],
    entry_points={
        'console_scripts': [
            'destiny=destiny:main'
        ]
    }
)