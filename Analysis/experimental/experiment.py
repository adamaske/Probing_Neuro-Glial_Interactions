import datetime

class Experiment:
    
    def __init__(self) -> None:
    
        self.created_datetime = datetime.datetime()
        
        self.name = "Unnamed Experiment"
        
        self.author = "Adam Emile Aske"
        
        self.desc = "An test experiment"
        pass
    
    def attach_eeg():
        
        pass
    
    def attach_fnirs():
        
        pass
    
def encode_experiment(ex:Experiment):
    #each experiment is saved as a single line in a file 
    #the line contains a bytearray containing the nessacary information about the experiment 
    encoded = 0

    bts = bytes()

    datetime_bytes = ex.created_datetime.strftime() 

    
    #4 bytes to store unique identifier
    #a few bytes to store datetime
    #20 bytes to store experiment name
    #turn all the valuable information about this experiment
    #into a compressed format
    return encoded

def decode_experiment(data):
    decoded = 0
    
    return decoded
        
        

def save_experiment(experiment:Experiment, filepath, ):
    
    
    
    
    
    pass

def load_experiment():
    
    pass


if __name__ == "__main__":
    
    data_bytes = b"Hello, Bytes!"
    print(data_bytes[0])  # Accessing the first byte
    print(data_bytes[7:12])  # Slicing bytes
    
    pass