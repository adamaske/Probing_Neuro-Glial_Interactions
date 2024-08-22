import os
import datetime
import experiment as ex
import experimental.experiments_md as emd

std_filepath = os.path("C:/dev/Probing_Neuro_Glial_Interactions/Analysis/experiment/")

def run_experiment(experiment:ex.Experiment):
    
    #is this loop interactive ? 
    
    return 

if __name__ == "__main__":

    experiments_metadata = emd.read_experiments_file(std_filepath)
    
    
    
    #perform some action
    
    emd.write_experiments_file(experiments_metadata)
    pass