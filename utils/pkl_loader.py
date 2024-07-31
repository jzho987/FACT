import pickle
import numpy as np;

# This loads and prints the data inside a pkl file.

# Main function
def main():
    filename = 'data/aist_plusplus_final/motions/gBR_sBM_cAll_d04_mBR0_ch01.pkl'
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    print("data")
    print(data)

if __name__ == '__main__':
    main()