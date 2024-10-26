import numpy as np
data_1 = np.load ("/home/edw/spotdog8/src/spotdog/data/joint_angle_8.npy")
data_in_deg = data_1 * ( 180 / np.pi )
np.set_printoptions(threshold=np.inf)  # In toàn bộ mảng
size = data_1.shape 
print(data_in_deg)