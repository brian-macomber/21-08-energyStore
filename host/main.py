#!/usr/bin/env python3
############################


### IMPORTS ###
# standard python libs
import socket
import logging
import threading
import time        #temporarily need this for pausing stuff
# locally defined imports
import defines     #this is basically a config file
import socket_top  #thread dedicated to socket
import monitor_top #thred dedicated to battery monitoring


####################################################################
# MAIN
####################################################################
if __name__  == "__main__":
    print("starting host/main.py")

    
    ##################################
    # set global variables for sharing
    # across threads


    ##################################
    # set up logging
    #TODO move log into logs/
    format = "%(asctime)s %(funcName)s: [%(levelname)s] %(message)s"
    logging.basicConfig(filename=defines.LOG_NAME, format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    log = logging.getLogger(defines.LOG_NAME)
    log.info("logging start")
    print("logging to {}".format(defines.LOG_NAME))


    ##################################
    # set up socket
    log.info("defining host socket")
    socket_port = defines.SOCKET_PORT
    socket_hostname = socket.gethostname()
    log.info("socket_hostname = {}, socket_port = {}".format(socket_hostname, socket_port))


    ##################################
    # set up threading
    #NEED thread for ML?
    log.info("starting socket thread")
    socket_thread = threading.Thread(target=socket_top.socket_top, args=(socket_hostname,socket_port), daemon=True)
    socket_thread.start()
    log.info("starting monitor thread")
    monitor_thread = threading.Thread(target=monitor_top.monitor_top, args=("",), daemon=True)
    monitor_thread.start()


    ##################################
    # run indefinitely
    while True:
        None
