# run with python visualize_output.py

import numpy as np

# Main function
def main():
    filename = 'outputs/gJB_sBM_cAll_d09_mJB5_ch01_mJB5.npy' 
    data = np.load(filename)
    print(data)
    print(data.shape)

    np.savetxt('data.txt', data, fmt='%s')

if __name__ == '__main__':
    main()