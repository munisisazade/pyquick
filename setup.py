import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of PyQuick requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install django
This will install the latest version of Django which works on your
version of Python. If you can't upgrade your pip (or Python), request
an older version of Django:
    $ python -m pip install "django<2"
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent Django are
# still present in site-packages. See #18115.
overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "pyquick"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break

version = __import__('pyquick').get_version()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


EXCLUDE_FROM_PACKAGES = ['pyquick.conf.project_template',
                         'pyquick.conf.app_template',
                         'pyquick.bin']

setup(
    name='pyquick',
    version=version,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    url='https://www.pyquick.com/',
    author='Munis Isazade',
    author_email='munisisazade@gmail.com',
    description=('A low-level Python Micro Web framework that encourages '
                 'rapid development and clean, pragmatic design.'),
    long_description=read('README.md'),
    license='MID',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    scripts=['pyquick/bin/pyquick'],
    entry_points={'console_scripts': [
        'pyquick = pyquick.bin.pyquick',
    ]},
    install_requires=['peewee', 'japronto'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Framework :: PyQuick',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
