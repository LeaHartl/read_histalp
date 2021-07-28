#! /usr/bin/env python3
import numpy as np
import pandas as pd
import xarray as xr
import cartopy.crs as ccrs
from matplotlib import pyplot as plt

# Weissseespitze coordinates
LAT = 46.846506
LON = 10.717269

# paths/file names HISTALP data
temp5m = 'HISTALP_temperature_1780-2014.nc'
prec_abs = 'HISTALP_precipitation_all_abs_1801-2014.nc'
prec_solid_abs = 'HISTALP_precipitation_solid_abs_1801-2014.nc'
prec_solid_part = 'HISTALP_precipitation_solid_part_1801-2014.nc'
temp = 'HISTALP_temperature_1780-2014old.nc'


# get data at lat/lon coordinates and write to csv.
def makeCSV(filenm, lt, ln, out):
    ds1 = xr.open_dataset(filenm, decode_times=False)
    # select grid cell closest to coordinates
    dp1 = ds1.sel(lon=ln, lat=lt, method='nearest')
    # print elevation of point to console.
    print(dp1.HSURF)
    # write data to csv
    df = dp1.to_dataframe()
    df.to_csv(out+'.csv')


# quick plot to see where coordinates fall on the histalp grid and elevations of grid.
def makefigure(filenm, lat, lon):
    ds1 = xr.open_dataset(filenm, decode_times=False)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    # plot overview
    ds1.HSURF.plot(ax=ax1)
    ds1.HSURF.plot(ax=ax2)

    # zoom in on Weissseespitze
    ax2.set_ylim([46.75, 47.0])
    ax2.set_xlim([10.5, 11.0])
    ax2.scatter(lon, lat, color='r')

    # plot surrounding grid points to see where coordinates are in
    # in relation to closest points.
    ax2.scatter(10.75,  46.833333, color='k')
    ax2.scatter(10.75,  46.916667, color='k')
    ax2.scatter(10.666667,  46.833333, color='k')
    ax2.scatter(10.666667,  46.916667, color='k')

    plt.show()


makeCSV(temp5m, LAT, LON, 'temp_WSP_5m_NE')
makefigure(temp5m, LAT, LON)
