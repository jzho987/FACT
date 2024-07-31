import numpy as np
from scipy.spatial.transform import Rotation as R
import pickle

# This converts the motion npy to a pkl file, which can be visualised in Blender using the SMPL to FBX add-on. 

# Main function
def main():
    # Used loss and scaling from gBR_sBM_cAll_d04_mBR0_ch01
    my_dict = {
        "smpl_loss": 1.5907235145568848,
        "smpl_poses": None,
        "smpl_scaling": np.array([93.77886], dtype=np.float32),
        "smpl_trans": None,
    }

    filename = 'outputs/gPO_sBM_cAll_d10_mPO1_ch02_mHO5.npy' 
    data = np.load(filename)
    data = np.array(data) # (N, 225)

    trans = data[:, 6:9]
    poses = data[:, 9:]

    poses = R.from_matrix(poses.reshape(-1, 3, 3)).as_rotvec().reshape(-1, 72)

    my_dict["smpl_poses"] = poses
    my_dict["smpl_trans"] = trans

    print("my_dict")
    print(my_dict)

    dict_filename = 'output2.pkl'
    with open(dict_filename, 'wb') as f:
        pickle.dump(my_dict, f)

if __name__ == '__main__':
    main()