import llh_to_enu as lte
import vicon_position as vp
from tkinter import filedialog
from numpy.fft import fft, ifft, fft2, ifft2, fftshift
import numpy as np
import math


def cross_correlation_using_fft(x, y):
    f1 = fft(x)
    f2 = fft(np.flipud(y))
    cc = np.real(ifft(f1 * f2))
    return fftshift(cc)


# shift < 0 means that y starts 'shift' time steps before x # shift > 0 means that y starts 'shift' time steps after x
def compute_shift(x, y):
    print(len(x), len(y))
    assert len(x) == len(y)
    c = cross_correlation_using_fft(x, y)
    assert len(c) == len(x)
    zero_index = int(len(x) / 2) - 1
    shift = zero_index - np.argmax(c)
    return shift


def calculate_rotate_angle(cell_vector, vicon_vector):
    # vector_1 = [1, 1]
    # vector_2 = [2, -2]

    unit_vector_1 = cell_vector / np.linalg.norm(cell_vector)
    unit_vector_2 = vicon_vector / np.linalg.norm(vicon_vector)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)

    print(angle)
    print(math.degrees(angle))

    return math.degrees(angle)


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


if __name__ == '__main__':
    rgp_csv_path = filedialog.askopenfilename()
    vicon_csv_path = filedialog.askopenfilename()

    print(rgp_csv_path, vicon_csv_path)

    cell_vec = []
    vicon_vec = []
    e, n, u = lte.llh_to_enu(rgp_csv_path)
    tx, ty, tz = vp.read_vicon_position_data(vicon_csv_path)

    # cross correlation for frame shift using cell altitude and vicon altitude
    st_frame = compute_shift(tz, u)
    print("shift frame = ", st_frame)

    # TODO: save new cell/vicon shift data by cross correlation

    # # calculate rotation angle from specific vector
    # rotate_angle = calculate_rotate_angle(cell_vec, vicon_vec)
    # print(rotate_angle)
    #
    # # Rotate x / y data for cell vicon data align
    # r_e, r_n = rotate(e, n, math.radians(rotate_angle))


    # estimate position error



