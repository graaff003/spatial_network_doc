#!/bin/bash
# creation of python virtual environment
# https://medium.com/bcggamma/data-science-python-best-practices-fdb16fdedf82
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
# =============================================================================
#
# custom function for conventient pause command
function pause(){
   read -p "$*"
}
# usage: pause 'Press [Enter] key to continue...'
#

echo install virtualenv for the creation of python virtual environments
pause 'Press [Enter] key to continue...'
pip3 install virtualenv

echo base dir for environments..
export venv_base_dir=<somewhere>/environments/

echo create the virtual env...
python3 -m venv $venv_base_dir'pynetworkanalysis'

pause 'Press [Enter] key to continue...'

echo ready!
