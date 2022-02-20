import nibabel as nib
import gzip

class Reader():
    def __init__(self):
        pass

    def read_nii(self, path):
        pass

    def read_gzip(self, path):
        '''
        Reads .nii file from gzip and returns pixel array
        '''
        with gzip.open(filepath, 'rb') as f_in:
            with open(filepath[:-3]+'.nii', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        ct_scan = nib.load(filepath[:-3]+'.nii')
        array   = ct_scan.get_fdata()
        array   = np.rot90(np.array(array))
        os.remove(filepath[:-3]+'.nii')
        os.remove(filepath)
        return array

    def read(self, path):
        pass
