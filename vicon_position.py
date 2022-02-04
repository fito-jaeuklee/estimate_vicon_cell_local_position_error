from tkinter import filedialog
import matplotlib.pyplot as plt
from math import cos, sin, atan2

# vicon_csv_path = filedialog.askopenfilename()


def read_vicon_position_data(filepath):
    tx = []
    ty = []
    tz = []

    f = open(filepath, "r")
    data = f.readlines()

    for i in range(5, len(data)-1):
        try:
            print(data[i])
            data_split = data[i].split(',')
            print(data_split)
            tx.append(float(data_split[6]))
            ty.append(float(data_split[7]))
            tz.append(float(data_split[8][:-2]))
        except:
            print("data empty = ", data_split)
            pass

    return tx, ty, tz


def rotate_to_x_axis(rtx, rty):
    a = []
    b = []
    xn = rtx[-1]
    yn = rty[-1]
    theta = atan2(-yn, xn)
    for i in range(0, len(rtx)):
        a.append(rtx[i]*cos(theta) - rty[i]*sin(theta))
        b.append(rtx[i]*sin(theta) + rty[i]*cos(theta))

    return a, b


# tx, ty, tz = read_vicon_position_data(vicon_csv_path)
# print(tx, ty)
# print(len(tx), len(ty))
#
# rtx, rty = rotate_to_x_axis(tx, ty)
#
# frame = plt.gca()
# # N = 55
# # re = np.convolve(g, np.ones((N,))/N, mode='valid')
# # # print(re)
# # plot.plot(time[:len(time) - N + 1], re, "-y", label="G-RPM")
#
# # roll = np.range
#
#
# # real_yaw = yaw_stretch_data_filter(real_yaw)
#
# plt.plot(tx, ty, "black", label=" x-y ")
# plt.plot(rtx, rty, "red", label=" rx-ry ")
# # plt.scatter(0, 0, color='black', s=100)
#
# plt.title('vicon coordinate data ')
#
# # Give x axis label for the sine wave plot
# plt.xlabel('tx')
#
# # Give y axis label for the sine wave plot
# plt.ylabel('ty')
# # plt.ylim(-400000, 37000)
# plt.grid(False)
# # frame.axes.get_yaxis().set_visible(False)
#
# # plot.axhline(y=0, color='k')
# plt.axhline(y=0, color='k')
# plt.legend(frameon=False)
# plt.get_current_fig_manager().show()
# plt.show()

# rtx, rty = rotate_to_x_axis(tx, ty)





