import argparse
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path for result file to parse and plot")
parser.add_argument("--log_datasize", action='store_true', default=False, help="Take a log for datasize values")
parser.add_argument("--log_elapsedtime", action='store_true', default=False, help="Take a log for elapsedtime values")
args = parser.parse_args()

result_df = pd.read_csv(args.path, sep=' - ', header=None, engine='python')
result_df.columns = ['core', 'path', 'size', 'elapsed_time']

result_df['core'] = result_df['core'].str.replace('Core: ', '').str.replace('*','17').astype('int')
result_df['path'] = result_df['path'].str.replace('Input: ', '')
result_df['size'] = result_df['size'].str.replace('Size: ', '').str.replace(' MB', '').astype('float')
result_df['elapsed_time'] = result_df['elapsed_time'].str.replace('Elapsed time:','').str.replace(' sec', '').astype('float')


cores = result_df['core'].unique()
datasize = result_df['size'].unique()
elapsed_time = result_df['elapsed_time'].values.reshape(set(datasize).__len__(),-1)

# log_datasize
datasize = np.log(datasize) if args.log_datasize else datasize
ylabel = 'log(datasize)' if args.log_datasize else 'datasize'

# log_elapsedtime
elapsed_time = np.log(elapsed_time) if args.log_elapsedtime else elapsed_time
zlabel = 'log(elapsed time(sec))' if args.log_elapsedtime else 'elapsed time (sec)'

def plot_3dsurface(x,y,z, params):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel(params['xlabel'])
    ax.set_ylabel(params['ylabel'])
    ax.set_zlabel(params['zlabel']);
    ax.set_title(params['title']);

    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    return plt



plot_3dsurface(x=cores, y=datasize, z=elapsed_time,
               params={'xlabel':'# core',
                       'ylabel':ylabel,
                       'zlabel':zlabel,
                       'title':'spark benchmark (datasize vs #cores)'}).show()
