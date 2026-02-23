import numpy as np

scan_data = np.arange(64)      # creates numbers from 0 to 63
vol = scan_data.reshape(4,4,4) # converts into 3D matrix

print("3D MRI Volume Shape:", vol.shape)