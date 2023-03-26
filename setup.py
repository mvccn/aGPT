from setuptools import setup, find_packages

setup(
    name='aGPT',
    version='0.1.0',
    description='chatgpt coder assistant',
    # url='PACKAGE_URL',
    author='Michael Li',
    # author_email='AUTHOR_EMAIL',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='aGPT',
    # packages=find_packages(),
    # packages=['openai'],
    install_requires=[
        'openai',
        'typer',
        'rich'
        # 'DEPENDENCY2',
    ],
    entry_points={
        'console_scripts': [
            'SCRIPT_NAME=aGPT.aGPT:main',
        ],
    },
)
