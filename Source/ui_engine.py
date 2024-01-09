from typing import Optional, Tuple, Union
import customtkinter as ctk

from threading import Thread

from osc_connection import OSC_Frame

class UI_Engine:
    def __init__(self) -> None:
        
        self.frames = []
        
        pass
    
    def setup(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
    
        self.root = ctk.CTk()
        self.root.geometry("500x350")
        
        self.add_base_frame()
        
    def add_base_frame(self):
        frame1 = OSC_Frame(engine=self, master=self.root)
        frame1.pack(pady=20, padx=60, fill="both", expand=True)
        frame1.create_self()
        
        frame2 = OSC_Frame(engine=self, master=self.root)
        frame2.pack(pady=20, padx=60, fill="both", expand=True)
        frame2.create_self()
        
        self.frame1 = frame1
        self.frame2 = frame2

    def run(self):
        
        self.root.mainloop()
        
        
        
    def login(self):
        print("Test")
     

if __name__ == "__main__":
    
    engine = UI_Engine()
    
    engine.setup()
    engine.run()
    
    
    


  
