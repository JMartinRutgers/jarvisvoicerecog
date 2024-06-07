basic voice recognition
Create virtual enviroment python3.5 -m venv <your env name>
install pip install wikipedia speech_recognition as sr
time, ctime, os, gtts import gTTS, playsound
-------------------------------------------------------------------
Using pip¶

The easiest way to install Kivy is with pip, which installs Kivy using either a pre-compiled wheel, if available, otherwise from source (see below).

Kivy provides pre-compiled wheels for the supported Python versions on Windows, macOS, Linux, and RPi.

If no wheels are available pip will build the package from sources (i.e. on *BSD).

Alternatively, installing from source is required for newer Python versions not listed above or if the wheels do not work or fail to run properly.

On RPi, when using a 32 bit OS, wheels are provided for Python 3.7 (Raspberry Pi OS Buster), Python 3.9 (Raspberry Pi OS Bullseye) and Python 3.11 (Raspberry Pi OS Bookworm) via the PiWheels project.

For other Python versions, on 32 bit OSes, you will need to install from source.

Setup terminal and pip¶

Before Kivy can be installed, Python and pip needs to be pre-installed. Then, start a new terminal that has Python available. In the terminal, update pip and other installation dependencies so you have the latest version as follows (for linux users you may have to substitute python3 instead of python and also add a --user flag in the subsequent commands outside the virtual environment):

python -m pip install --upgrade pip setuptools virtualenv
Create virtual environment¶

Create a new virtual environment for your Kivy project. A virtual environment will prevent possible installation conflicts with other Python versions and packages. It’s optional but strongly recommended:

Create the virtual environment named kivy_venv in your current directory:

python -m venv kivy_venv
Activate the virtual environment. You will have to do this step from the current directory every time you start a new terminal. This sets up the environment so the new kivy_venv Python is used.

For Windows default CMD, in the command line do:

kivy_venv\Scripts\activate
If you are in a bash terminal on Windows, instead do:

source kivy_venv/Scripts/activate
If you are in linux or macOS, instead do:

source kivy_venv/bin/activate
Your terminal should now preface the path with something like (kivy_venv), indicating that the kivy_venv environment is active. If it doesn’t say that, the virtual environment is not active and the following won’t work.

Install Kivy¶

Finally, install Kivy using one of the following options:

Pre-compiled wheels¶

The simplest is to install the current stable version of kivy and optionally kivy_examples from the kivy-team provided PyPi wheels. Simply do:

python -m pip install "kivy[base]" kivy_examples
This also installs the minimum dependencies of Kivy. To additionally install Kivy with audio/video support, install either kivy[base,media] or kivy[full]. See Kivy’s dependencies for the list of selectors.

Note
The Pillow library is a dependency of both kivy[base] and kivy[full].
For Windows 32-bit users, please note that the latest releases of Pillow are not available as binary distributions on PyPI. However, Kivy also supports Pillow==9.5.0, which have a binary distribution for all supported Python versions, even on Windows 32-bit.
If you are on Windows 32-bit and prefer not to build Pillow from source, you can use the --only-binary Pillow flag with the following command to instruct pip to install the binary distribution of Pillow, albeit not the latest version:
python -m pip install --only-binary Pillow "kivy[base]"
Note
When using Raspberry Pi OS Lite or similar Linux-based headless systems, it may be necessary to install additional dependencies to ensure Kivy functions properly.
For instance, on Raspberry Pi OS Lite, you will be required to install the following dependencies:
apt-get install libgl1-mesa-glx libgles2-mesa libegl1-mesa libmtdev1
From source¶

If a wheel is not available or is not working, Kivy can be installed from source with some additional steps. Installing from source means that Kivy will be installed from source code and compiled directly on your system.

First install the additional system dependencies listed for each platform: Windows, macOS, Linux, *BSD, RPi

Note
In past, for macOS, Linux and BSD Kivy required the installation of the SDL dependencies from package managers (e.g. apt or brew). However, this is no longer officially supported as the version of SDL provided by the package managers is often outdated and may not work with Kivy as we try to keep up with the latest SDL versions in order to support the latest features and bugfixes.
You can still install the SDL dependencies from package managers if you wish, but we no longer offer support for this.
Instead, we recommend installing the SDL dependencies from source. This is the same process our CI uses to build the wheels. The SDL dependencies are built from source and installed into a specific directory.
With all the build tools installed, you can now install the SDL dependencies from source for SDL support (this is not needed on Windows as we provide pre-built SDL dependencies for Windows)

In order to do so, we provide a script that will download and build the SDL dependencies from source. This script is located in the tools directory of the Kivy repository.

Create a directory to store the self-built dependencies and change into it:

mkdir kivy-deps-build && cd kivy-deps-build
Then download the build tool script, according to your platform:

On macOS:

curl -O https://raw.githubusercontent.com/kivy/kivy/master/tools/build_macos_dependencies.sh -o build_kivy_deps.sh
On Linux:

curl https://raw.githubusercontent.com/kivy/kivy/master/tools/build_linux_dependencies.sh -o build_kivy_deps.sh
Make the script executable:

chmod +x build_kivy_deps.sh
Finally, run the script:

./build_kivy_deps.sh
The script will download and build the SDL dependencies from source. It will also install the dependencies into a directory named kivy-dependencies. This directory will be used by Kivy to build and install Kivy from source with SDL support.

Kivy will need to know where the SDL dependencies are installed. To do so, you must set the KIVY_DEPS_ROOT environment variable to the path of the kivy-dependencies directory. For example, if you are in the kivy-deps-build directory, you can set the environment variable with:

export KIVY_DEPS_ROOT=$(pwd)/kivy-dependencies
With the dependencies installed, and KIVY_DEPS_ROOT set you can now install Kivy into the virtual environment.

To install the stable version of Kivy, from the terminal do:

python -m pip install "kivy[base]" kivy_examples --no-binary kivy
To install the latest cutting-edge Kivy from master, instead do:

python -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip"
If you want to install Kivy from a different branch, from your forked repository, or from a specific commit (e.g. to test a fix from a user’s PR) replace the corresponding components of the url.

For example to install from the stable branch, the url becomes https://github.com/kivy/kivy/archive/stable.zip. Or to try a specific commit hash, use e.g. https://github.com/kivy/kivy/archive/3d3e45dda146fef3f4758aea548da199e10eb382.zip

Pre-release, pre-compiled wheels¶

To install a pre-compiled wheel of the last pre-release version of Kivy, instead of the current stable version, add the --pre flag to pip:

python -m pip install --pre "kivy[base]" kivy_examples
This will only install a development version of Kivy if one was released to PyPi. Instead, one can also install the latest cutting-edge Nightly wheels from the Kivy server with:

python -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/
python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/
It is done in two steps, because otherwise pip may ignore the wheels on the server and install an older pre-release version from PyPi.

Development install¶

Note
We suggest to select master or relevant branch/version of doc from top left, ensuring correct version/branch of kivy git repository you are working with.
If you want to edit Kivy before installing it, or if you want to try fixing some Kivy issue and submit a pull request with the fix, you will need to first download the Kivy source code. The following steps assumes git is pre-installed and available in the terminal.

The typical process is to clone Kivy locally with:

git clone https://github.com/kivy/kivy.git
This creates a kivy named folder in your current path. Next, follow the same steps of the Installing from source above, but instead of installing Kivy via a distribution package or zip file, install it as an editable install.

In order to do so, first change into the Kivy folder you just cloned:: and then install Kivy as an editable install:

cd kivy
python -m pip install -e ".[dev,full]"
Now, you can use git to change branches, edit the code and submit a PR. Remember to compile Kivy each time you change cython files as follows:

python setup.py build_ext --inplace
Or if using bash or on Linux, simply do:

make
to recompile.

To run the test suite, simply run:

pytest kivy/tests
or in bash or Linux:

make test
On *BSD Unix remember to use gmake (GNU) in place of make (BSD).

Checking the demo¶

Kivy should now be installed. You should be able to import kivy in Python or, if you installed the Kivy examples, run the demo.

on Windows:

python kivy_venv\share\kivy-examples\demo\showcase\main.py
in bash, Linux and macOS:

python kivy_venv/share/kivy-examples/demo/showcase/main.py
on *BSD Unix:

python3 kivy_venv/share/kivy-examples/demo/showcase/main.py

The exact path to the Kivy examples directory is also stored in kivy.kivy_examples_dir.

The 3d monkey demo under kivy-examples/3Drendering/main.py is also fun to see.
