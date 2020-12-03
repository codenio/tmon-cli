'''
tmon view - CSV viewer command tmon  

03-12-2020


codenio - Aananth K
aananthraj1995@gmail.com
'''

import click

import pandas as pd
import matplotlib.pyplot as plt


@click.command()
@click.argument('file', type=click.File('r'))
def cli(file):
    """view previously collected data\n\n FILE - specify the .csv file location that you want to view"""
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
        plt.figure('tmon')
        plt.plot(df['time'], df["sensor1"], label='sensor 1')
        plt.plot(df['time'], df["sensor2"], label='sensor 2')
        plt.plot(df['time'], df["sensor3"], label='sensor 3')

        plt.title('Temperature Plot')
        plt.xlabel('Time [Sec]')
        plt.ylabel('Temperature [deg C]')
        plt.grid()
        plt.legend()
        plt.show()
    else:
        print('Invalid File Format, please select a .csv file to view the data')
