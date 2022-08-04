from time import sleep
import matplotlib.pyplot as plt
import random

def live_plotter(num1, num2, num3, line1, line2, line3, list, list2, list3):
    # list = [0,0,0,0,0,0,0,0,0,0]
    # list2 = [0,0,0,0,0,0,0,0,0,0]
    # list3 = [0,0,0,0,0,0,0,0,0,0]


    x_values = [*range(len(list))]

    if line1==[]:

        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()

        fig, axs = plt.subplots(3)
        fig.suptitle('IMU sensor data')
        line1, = axs[0].plot(x_values, list)
        line2, = axs[1].plot(x_values, list2)
        line3, = axs[2].plot(x_values, list3)

        axs[0].set_title("Yaw")
        axs[1].set_title("Pitch")
        axs[2].set_title("Roll")

        axs[0].set_ylim([0, 360])
        axs[1].set_ylim([-180, 180])
        axs[2].set_ylim([-180, 180])

        plt.show()

    #print(list.pop(0))
    list.pop(0)
    list.append(num1)

    #print(list2.pop(0))
    list2.pop(0)
    list2.append(num2)

    #print(list3.pop(0))
    list3.pop(0)
    list3.append(num3)

    #Update the plots
    line1.set_ydata(list)
    line2.set_ydata(list2)
    line3.set_ydata(list3)

    #plt.pause(0.2)

    return line1, line2, line3, list, list2, list3

    # axs[0].clear()
    # axs[0].plot(x_values, list)

    # axs[1].clear()
    # axs[1].plot(x_values, list2)

    # plt.show()
    # sleep(1)