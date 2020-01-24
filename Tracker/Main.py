# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:34:33 2019

@author: Kuro Azai

Tracker Scripts
"""
import time
import threading
import datetime
import geocoder
from pyfirmata import Arduino, util 



#Global state controls how the tracker reacts to interaction, 0=disarmed, 1=passive_arm,2=Armed 3=High Alert
global state

# Functions
def Send_Message(msg):
    #Sends an alert to owner via application/msg
    pass

def Update_LiveGPS(GPS,GSM,RF,ID):
    #Update Current Position, Date & Time(testing)
    g = geocoder.ip('me')
    
    #Data order : Lat , Long, Date &Time    
    data = { ID:[{'Lat': g.latglong[0], 'Long': g.latglong[1], 'Date': datetime.datetime.now()}]}
    #Send the data      

def Check_Motion(M_Sensor):
    if M_Sensor > 0.3:
            Send_Message("Motion Detected")
    elif M_Sensor > 0.7:
            Send_Message("Hello Darkness")
    

def User_Control():
    #Check for message 
    
    #Update on interaction 
    pass


#Main
def __Main__():
    #dudududu
    global state

    def Refresh_Data(board):
        #Register Pins 
        M_Sens = board.get_pin('x:x:x')
        GPS = board.get_pin('x:x:x')
        RF = board.get_pin('x:x:x')
        GSM = board.get_pin('x:x:x')        
        return M_Sens,GPS,RF,GSM
    
    #Initialise Board
    board = Arduino('COM3')
    #Setup Util with Board
    iterator = util.Iterator(board)
    iterator.start()
    #Wait for Board to initialise 
    time.sleep(1)  
    
    #Start Thread that registers user controls
    t1 = threading.Thread(Target=User_Control)
    t1.start()
    #Persistency ~ 
    while True:
        #Data Stream 
        M_Sens,GPS,RF,GSM = Refresh_Data()
        #State Check  
        if state > 0:
            Update_LiveGPS(GPS)                
            Check_Motion(M_Sens)
        #Sleep
        time.sleep(1)
    exit()
