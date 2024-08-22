from FNIRS import fnirs_datasets as fd
from EEG import eeg_datasets as ed


if __name__ == "__main__":
    
    table = fd.load_table()
    metadata = fd.load_metadata()
#Welcome to analyzing fnris and eeg data at the same time


#what are we looking for

#1. We want to inspect the EEG data
#2. We want to inspect FNIRS data

#3. We want to analyze EEG -> Identify Sensory evoked potentioals (event realted desyncronizasiton)
#4. Analyze FNIRS -> Mehtod not yet identified

#5. Correlate SERPs and FNIRS-values
 
motion_artifacts_data = fd.load_motion_artifacts_dataset()

