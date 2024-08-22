
import os
import pathlib
import mne
import matplotlib.pyplot as plt
import uuid

class FNIRSDatasetManager:
    def __init__(self) -> None:
        
        self.active_table = 0
        self.active_metadata = 1
        pass
    
fnirs_data_folder = os.path.join(os.getcwd(), "FNIRS\\datasets")
motion_artifacts_folder = os.path.join(fnirs_data_folder, "motion_artifacts")


master_folder = fnirs_data_folder

#This is a datatable for fnir_file instances
def load_table():
    table = []
    with open(os.path.join(master_folder, "table.data"), 'rb') as f:
        data = f.read()
        table.append(data)
        
        
    return table

def load_metadata():
    md = 0
    with open(os.path.join(master_folder, "metadata.data"), 'rb') as f:
        data = f.read()
        md.append(data)
    
        
    
def register_fnirs_dataset():
    uid = uuid.uuid1()
    
    return uid

def is_snirf_file(filename):
    """Checks for .snirf suffix.
    
    Returns true or false
    """
    return filename[-6:] == ".snirf"

def search_folder_for_snirf_files(absoulte_path, check_subfolders = True):
    """
    Search a folder for .snirf files.
    Params:
    absoulte_path : Absoulte path to a folder 
    check_subfolders enables branching search. 
    
    Returns 
    """
    data = []
    for filename in os.listdir(absoulte_path):
        filepath = os.path.join(absoulte_path, filename)
        if os.path.isdir(filepath) and check_subfolders:
            subfolder_data = search_folder_for_snirf_files(filepath)
            data.append(subfolder_data)
            continue
        
        if is_snirf_file(filename):
            raw_snirf = mne.io.read_raw_snirf(filepath, optode_frame='mri', preload=True, verbose=True)
            data.append(raw_snirf)
            
    return data

def load_motion_artifacts_dataset():
    """
    Motion artifacts from https://www.nitrc.org/frs/?group_id=1454&release_id=4334
    
    Uses mne.io.read_raw_snirf()
    
    Returns array of mne.RawSNIRF objects
    """
    motion_data = []
    for subject in os.listdir(motion_artifacts_folder):
     
        subject_path = os.path.join(motion_artifacts_folder, subject)
        if os.path.isdir(subject_path):
            for file in os.listdir(subject_path):
                if is_snirf_file(file):
                    snirf_filepath = os.path.join(subject_path, file)
                    raw_snirf = mne.io.read_raw_snirf(snirf_filepath,optode_frame='mri',preload=True, verbose=True)   
                    motion_data.append(raw_snirf)
        else:
            if is_snirf_file(subject_path):
                snirf_filepath = os.path.join(subject_path, file)
                raw_snirf = mne.io.read_raw_snirf(snirf_filepath,optode_frame='mri',preload=True, verbose=True)   
                motion_data.append(raw_snirf)
                
    return motion_data
                
data = load_motion_artifacts_dataset()

plt.rcParams["figure.figsize"]= (6,6) #w,h
# raw_intensity.plot_sensors()
data[0].plot()        
plt.show()