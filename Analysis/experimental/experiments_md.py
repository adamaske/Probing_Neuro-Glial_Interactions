import experiment as ex
import os 

def create_dummy_md(filepath):
    
    pass

def read_experiments_file(filepath):
    
    use_dummy_md = True
    if not os.path.exists(filepath):
        if use_dummy_md: 
            create_dummy_md(filepath)
        else:
            return
        
    with open(filepath, 'rb') as f:
        data = f.read()
        print(data)

    pass

def write_experiments_file(experiments):
    for experiment in experiments:
        return
    
def list_experiments():

    
    pass