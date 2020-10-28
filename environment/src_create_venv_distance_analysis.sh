#!/bin/bash
# creation of vpython virtual environment
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
: << 'COMMENT'
echo install virtualenv for the creation of python virtual environments
#pip3 install virtualenv

echo base dir for environments..
export venv_base_dir=/home/nico/apps/environments/

echo create the virtual env...
python3 -m venv $venv_base_dir'pynetworkanalysis'

pause 'Press [Enter] key to continue...'

echo activate the env..
source $venv_base_dir'pynetworkanalysis/bin/activate'
pwd
pause 'Press [Enter] key to continue...'

COMMENT
echo install dependencies..
pip install --upgrade pip
pip install matplotlib
# dependencies for geopandas
pip install numpy
pip install pandas
pip install shapely
pip install fiona
pip install pyproj
pip install geopandas
pip install networkx
pip install jupyter
pip install descartes  # plot polygons
pip install progressbar
pip install ipyleaflet
pip install jupyterlab
pip install owslib # ogc services
# geopandas dependecies
pip install rtree #spatial indexing
pip install rasterio


echo wellicht jupyterlab extensie installeren voor ipyleaflet?
echo proberen folium?

pause 'Press [Enter] key to continue...'
echo write requirements
pip freeze > requirements.txt

echo ready!
# usage for reproduction: pip install -r requirements.txt
