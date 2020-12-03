"""
tmon run - CSV run command tmon

03-12-2020


codenio - Aananth K
aananthraj1995@gmail.com
"""

import sys
import time

import click
import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


trials = {
    "time": [],
    "sensor1": [],
    "sensor2": [],
    "sensor3": [],
}


@click.command()
@click.option('-p', '--path', default="./", help="path for output csv file to be created")
@click.option('-o', '--output', default="temperature-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv",
              help="name of the output csv file to be created")
@click.option('-s', '--show', is_flag=True, help="show captured data as a plot at the end")
def cli(path, output, show):
    """collect the serial data from Arduino"""
    try:
        port = serial.Serial("/dev/ttyUSB0", 9600)
    except serial.serialutil.SerialException:
        print("Arduino Connection Not Found, Check the USB Connection..!!")
        sys.exit(0)

    port.timeout = 1

    print("listening for serial data....")

    try:
        while True:
            data = port.readline().decode().rstrip()
            if len(data) > 0:
                if data == 'done':
                    print('finished')
                    break
                print(data)
                datas = data.split(' ')
                trials["sensor1"].append(datas[0])
                trials["sensor2"].append(datas[1])
                trials["sensor3"].append(datas[2])
            time.sleep(0.5)

        port.close()
        print("Connection Closed")

    except KeyboardInterrupt:
        print("Program Terminated")
        sys.exit(0)

    if len(trials["sensor1"]) > 0:

        x = np.arange(len(trials["sensor1"]))

        print('saving data into csv file')
        trials["time"] = x

        df = pd.DataFrame(trials)
        df.to_csv(path + output, index=False)
        print(f"data saved to : {path + output}")

        if show:
            df = pd.read_csv(path + output)
            plt.figure('tmon')
            plt.plot(df['time'], df["sensor1"], label='sensor 1')
            plt.plot(df['time'], df["sensor2"], label='sensor 2')
            plt.plot(df['time'], df["sensor3"], label='sensor 3')

            plt.title(f'Temperature Plot: {output}')
            plt.xlabel('Time [Sec]')
            plt.ylabel('Temperature [deg C]')
            plt.grid()
            plt.legend()
            plt.show()
