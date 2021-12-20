import matplotlib.pyplot as plt


def main():
    time = [0, 1, 2, 3]
    position = [0, 100, 200, 300]

    plt.plot(time, position)
    plt.xlabel('time (hr)')
    plot.ylabel('Position (km)')