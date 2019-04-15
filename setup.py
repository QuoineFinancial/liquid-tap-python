from setuptools import setup, find_packages

requirements = ["websocket-client!=0.49"]


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="liquidtap",
    version="1.0.1",
    description="QuoineFinancial/LiquidTap websocket client for Python",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords="pusher websocket client liquid liquidapi liquidtap",
    author="Jered Masters",
    author_email="jered.masters@quoine.com",
    license="MIT",
    url="https://github.com/QuoineFinancial/liquid-tap-python",
    install_requires=requirements,
    packages=find_packages(exclude=['contrib', 'docs', 'websocket-client', 'txaio']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
