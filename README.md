# gps-location-finder

A simple application allowing to get GPS coordinates of any location by its address developed in Python (current version is 3.10). It uses an Open street map https://www.openstreetmap.org as well as the application has a simple graphical user interface (GUI).

# Requirements

There are several libraries besides python 3.x should be installed before running the application. The below installation guid has been tested on Win 10 and Ubuntu 20 maschiens.


# Installation
To install requiered packages the anaconda distribution https://www.anaconda.com/ should be pre-installed. 

Update your conda by typing in the termina (Linux) or open Anaconda Prompt as Administrator (Windoes).

```console
conda update --all
conda config --prepend channels conda-forge
```
The gps-location-finder app requieres osmx PyQt, geppy folium and mathplotlib libraries.  
```console
conda create -n <your_env_name> --strict-channel-priority osmnx pyqt geopandas geopy folium matplotlib
```
Install PyQtWebEngine to show map in QtWidget


