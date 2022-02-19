import segmentation
import nibabel as nib
import numpy as np
import os
import matplotlib.pyplot as plt

def read_nii(filepath):
    ct_scan = nib.load(filepath)
    array = ct_scan.get_fdata()
    array = np.rot90(np.array(array))
    return array

def main():
    testfiles = os.listdir('./testfiles')
    os.mkdir('./testresult/')
    for file in testfiles:
        print(file)
        arr = read_nii('./testfiles/'+file)
        result, lung, ct = segmentation.segmentation(arr)
        height = arr.shape[2]
        for i in range(height):
            print(i)
            fig = plt.figure(figsize = (24, 20))
            plt.subplot(1,3,1)
            plt.imshow(ct[i, ...,0], cmap = 'bone')
            plt.title('original lung')
        
            plt.subplot(1,3,2)
            plt.imshow(lung[i,...,0], cmap = 'bone')
            plt.title('lung')

            plt.subplot(1,3,3)
            plt.imshow(ct[i,:,:,0], cmap = 'bone')
            plt.imshow(result[i,:,:,0],alpha = 0.5,cmap = "nipy_spectral")
            plt.title('predicted infection mask')

            plt.savefig('./testresult/'+file+str(i)+'.png')

    print('OK')

if __name__=='__main__':
    main()
