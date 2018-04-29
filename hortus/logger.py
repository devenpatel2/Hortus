import logging
import os

class Logger:


    def __init__(self, level = logging.INFO, log_file=None):
        
        self._log_file = log_file
        self._file = __file__
        self._level = level
        self._set_log() 
    
    def _set_log(self ):

        FORMAT = '%(asctime)-15s [%(name)s] [%(levelname)s] %(message)s'
        if self._log_file:
            logging.basicConfig(filename=filename, format=FORMAT)
        else:
            logging.basicConfig(format=FORMAT)

        self.log = logging.getLogger(os.path.basename(__file__).split('.')[0])
        self.log.setLevel(self._level)


