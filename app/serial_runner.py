import time
import numpy as np
import multiprocessing


class SerialRunner(multiprocessing.Process):

    def __init__(self, config_file_path):
        super(SerialRunner, self).__init__()
        self.config_file_path=config_file_path    
    def run(self) -> None:               
        while True :
            print("Template Process has been initialized")
            print("Doing NOTHING, but has a greppable $PID")      
            time.sleep(1)


