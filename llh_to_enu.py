from tkinter import filedialog
import pymap3d as pm
import matplotlib.pyplot as plt
from math import cos, sin, atan2
import numpy as np
import math

# rgp_csv_path = filedialog.askopenfilename()


# degrees / degrees / meters
# Cell start origin
def llh_to_enu(filepath):
    f = open(filepath, "r")
    data = f.readlines()
    origin_lat_lon_alt = [33.25360933, 126.490358333, 103.931]

    lat = []
    lon = []
    hei = []

    east = []
    north = []
    up = []

    # save list lat, lon, height
    for i in range(1, len(data)):
        # print(data[i])
        data_split = data[i].split(',')
        # print(data_split)
        lat.append(float(data_split[4]))
        lon.append(float(data_split[5]))
        hei.append(float(data_split[7]))

    for j in range(0, len(lat)):
        x, y, z = pm.geodetic2enu(lat[j], lon[j], hei[j], origin_lat_lon_alt[0], origin_lat_lon_alt[1], origin_lat_lon_alt[2])
        east.append(x)
        north.append(y)
        up.append(z)

    print(east, north, up)

    return east, north, up


def rotate(rtx, rty, angle):
    a = []
    b = []
    ox, oy = (0, 0)

    for z in range(0, len(rtx)):
        qx = ox + math.cos(angle) * (rtx[z] - ox) - math.sin(angle) * (rty[z] - oy)
        qy = oy + math.sin(angle) * (rtx[z] - ox) + math.cos(angle) * (rty[z] - oy)
        a.append(qx)
        b.append(qy)

    return a, b


# east, north, up = llh_to_enu(rgp_csv_path)
# reast, rnorth = rotate(east, north, math.radians(45))
#
# frame = plt.gca()
#
#
# plt.plot(east, north, "red", label=" x-y ")
# plt.plot(reast, rnorth, "blue", label=" rx-ry ")
# plt.scatter(0, 0, color='black', s=1000)
# plt.scatter(east[-10000], north[-10000], color='blue', s=1000)
# plt.scatter(reast[-10000], rnorth[-10000], color='black', s=1000)
#
# plt.title('ENU coordinate data ')
#
# # Give x axis label for the sine wave plot
# plt.xlabel('east')
#
# # Give y axis label for the sine wave plot
# plt.ylabel('north')
# # plt.ylim(-400000, 37000)
# plt.grid(False)
# # frame.axes.get_yaxis().set_visible(False)
#
# # plot.axhline(y=0, color='k')
# plt.axhline(y=0, color='k')
# plt.legend(frameon=False)
# plt.get_current_fig_manager().show()
# plt.show()

