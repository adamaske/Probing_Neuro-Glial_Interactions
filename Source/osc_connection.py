import ui_engine 

from threading import Thread

from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher

import customtkinter as ctk


class OSC_Frame(ctk.CTkFrame):
    def __init__(self, 
                engine: any,
                master: any, 
                width: int = 200, 
                height: int = 200, 
                corner_radius: int | str | None = None, 
                border_width: int | str | None = None, 
                bg_color: str | Tuple[str, str] = "transparent", 
                fg_color: str | Tuple[str, str] | None = None, 
                border_color: str | Tuple[str, str] | None = None, 
                background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                overwrite_preferred_drawing_method: str | None = None, **kwargs
                ):
        self.engine = engine
        super().__init__(master, #init properly
                        width,
                        height,
                        corner_radius,
                        border_width,
                        bg_color, fg_color, border_color,
                        background_corner_colors,
                        overwrite_preferred_drawing_method,
                        **kwargs)
    def update(self) -> None:
        print("test")
        
        return super().update()
    def create_self(self):
        #add custom stuff
        self.label = ctk.CTkLabel(master=self, text="OSC Server")#, text_font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.ip_entry = ctk.CTkEntry(master=self, placeholder_text="IP-ADDRESS")
        self.ip_entry.pack(pady=12, padx=10)

        self.port_entry = ctk.CTkEntry(master=self, placeholder_text="PORT")
        self.port_entry.pack(pady=12, padx=10)

        self.connect_button = ctk.CTkButton(master=self, text="Connect", command=self.Connect)
        self.connect_button.pack(pady=12, padx=10)

    def Connect(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        print(f"ip : {ip}")
        print(f"port = {port}")


def default_handler(address, *args):
    print(f"DEFAULT : {address}: {args}")


class OSC_Server():
    def __init__(self, name, ip, port) -> None:
        self.name = name
        self.ip = ip
        self.port = port
        pass
    def run(self):
        
        dispatcher = Dispatcher()
        dispatcher.map("",)
        dispatcher.set_default_handler(default_handler)
    
        server =  BlockingOSCUDPServer((self.ip, self.port), dispatcher)

        server.serve_forever()
    
    

class OSC_Client():
    def __init__(self, name, ip, port) -> None:
        pass
    
class OSC_Controller(Thread):
    def __init__(self) -> None:
        
        
        self.queue = []
        
    def run(self):
        
        return
    
    def Create_Server(self, server):
        self.servers.append(server)
        return
    def Create_Client(self, client):
        self.clients.append(client)
        return
        
        
        
    
    
    