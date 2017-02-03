import h5py

dat = h5py.File('1486144636_sine_wave_plot.h5', 'r')

sample_name = dat['app/settings'].attrs['sample']
print(sample_name)
# Test Sample 42

buffer_data = dat['measurement/sine_wave_plot/buffer']

import matplotlib.pyplot as plt
plt.title(sample_name)
plt.plot( buffer_data)
plt.savefig('sine_wave_data_plot_42.png')
plt.show()