from setuptools import setup
setup(
    name="guachi",
    version="0.0.6",
    packages=["guachi"],
    include_package_data=True,
    author="Alfredo Deza",
    author_email="alfredodeza@gmail.com",
    description="Global, persistent configurations as dictionaries",
    long_description="""
When projects start to grow, the need for a globally accessible configuration
manager is obvious.

Having configurations mapped to dictionaries is really useful, but can create a
problem with memory.

**Guachi** not only holds persistent dictionaries on disk, but it also maps
INI style keys to dictionary keys, and can fill in the default values if some
of them are missing.

You do not need to know anything about how **guachi** stores the values, just
treat it like a regular dictionary!
""",
    install_requires=[],
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
      ],
    license = "MIT",
    keywords = "configuration management persistent dictionaries dictionary parse map mapping",
    url = "http://code.google.com/p/guachi",
)

