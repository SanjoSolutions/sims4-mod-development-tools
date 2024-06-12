# Sims 4 Mod Development Tools

Compiler for Sims 4 mod python scripts. It creates the `ts4script` file that is usually shipped.

# How to get started

## Installing Python

It's recommended to install the same Python version as is used by Sims 4. At the time of writing this seems to be 3.7. This can be found out by checking the info on the file `<PATH_TO_SIMS_4>/Game/Bin/python*_x64.dll`.

This can be done with [Anaconda](https://www.anaconda.com/download/success). After having installed Anaconda, create a new environment for Sims 4 by opening the `Anaconda Prompt` (you can find that under programs in Windows), and running the command `conda create --name Sims4 python=3.7`. To run Python scripts in this environment, open the `Anaconda Prompt` and switch to the environment with `conda activate Sims4`.

## Installing the Sims 4 Mod Development Tools

Download this project (`git clone https://github.com/SanjoSolutions/sims4-mod-development-tools.git` or download the ZIP).

## Setting up the Sims 4 Mod Development Tools for a project

1. Copy `settings.template.py` from the sims4-mod-development-tools folder to your project and name the file `settings.py`.
2. Adjust the settings to your preferences. Minimally that's the author and project name. And maybe the folder names and paths.
3. To compile your project, open an Anaconda Prompt with the Sims4 environment, go to your projects folder and run `python <PATH_WHERE_sims4-mod-development-tools_IS_INSTALLED>/compile.py`.
