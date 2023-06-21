import netCDF4
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib.path as mpath

FILE = "../data/Kinugawa2015/wrfout_d01_2015-09-08_12:00:00"
nc = netCDF4.Dataset(FILE, 'r')
nc.variables.keys()
nc.variables["RAINNC"]

from matplotlib import colorbar
from matplotlib.colors import LogNorm
from matplotlib import animation

lats = nc["XLAT"][0]
lons = nc["XLONG"][0]
lon_c = nc.CEN_LON
lat_c = nc.CEN_LAT

precp = nc.variables["RAINNC"][6]

fig = plt.figure(figsize=(12,9))

def _update(frame):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()

    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=frame, central_latitude=lat))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.set_extent([lons[0][0],lons[-1][-1],lats[0][-1],lats[-1][0]],ccrs.PlateCarree())
    ax.coastlines(resolution='10m', lw=0.5)
    ax.gridlines(xlocs=mticker.MultipleLocator(5), 
             ylocs=mticker.MultipleLocator(5), 
             linestyle='-', 
             color='gray')
    levels=[0.1, 0.5,1.0,2.0,5.0,10.0,20.0,50.0,100.0, 200, 400]
    cs = ax.contourf(lons, lats, precp, transform=ccrs.PlateCarree(), levels=levels, vmin=0.1, vmax=400, norm=LogNorm(), cmap='jet')
    cbar = plt.colorbar(cs)
    
def main():
    # 描画領域
    fig = plt.figure(figsize=(12, 9))

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'interval': 1,  # 更新間隔 (ミリ秒)
        'frames': np.arange(359, 0, -1),  # フレーム番号を生成するイテレータ
        'repeat': True,  # 繰り返す
    }
    anime = animation.FuncAnimation(**params)


    # グラフを表示する
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()
