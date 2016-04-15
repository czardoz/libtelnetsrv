from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="libtelnetsrv",
    packages=["libtelnetsrv"],
    version="0.0.1",
    extras_require={
        'green': ['gevent'],
        'ssh': ['paramiko'],
    },
    description="Telnet server handler library",
    long_description=readme(),
    author="Aniket Panse",
    author_email="aniketpanse@gmail.com",
    url="https://github.com/czardoz/libtelnetsrv",
    keywords=["gevent", "telnet", "server"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Communications :: BBS",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Terminals :: Telnet",
    ],
)
