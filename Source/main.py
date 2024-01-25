import numpy as np

import mne


sample_data_folder = mne.datasets.sample.data_path() #sample data

sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file)

print(raw)
#https://mne.tools/stable/auto_tutorials/intro/20_events_from_raw.html