import time, socket
import numpy as np
from acq4.Manager import getManager
from acq4.devices.Stage import Stage, MoveFuture
from acq4.util.Thread import Thread
import acq4.pyqtgraph as pg
from acq4.pyqtgraph.Qt import QtGui, QtCore
from acq4.util.Mutex import Mutex
import win32com.client
import pythoncom

class PrairieView(QtCore.QObject):

    sigDataReady = QtCore.Signal(object)
    sigMarkPointsRun = QtCore.Signal(object)

    def __init__(self):

        QtCore.QObject.__init__(self)
        self.prairieRigIP = "10.128.26.11" #Wayne Rig
        self.pl_socket = None
        self.connected = False


    def connect_to_prairie(self):
 
        if not self.connected:

            self.pl_socket = socket.create_connection((self.prairieRigIP, 1236))
            self.connected = True


    def quit(self):

        closed = self.call_pl('-Exit')

        self.pl_socket.close() 
        print('===PROPER DISCONNECT FROM PRAIRIE OCCURED===') 


    def call_pl(self, cmd):

        if not self.connected:
            self.connect_to_prairie()

        orig_cmd = cmd
        cmd = cmd.replace(' ', '\1') + '\r\n'
        self.pl_socket.send(cmd)
        response = ''
        while True:
            response += self.pl_socket.recv(1000)
            if response.endswith('DONE\r\n'):
                break
            time.sleep(0.005)
        parts = response.split('\r\n')


        self.sigDataReady.emit(orig_cmd)

        if 'MarkPoints' in orig_cmd:
            if '-LoadMarkPoints' not in orig_cmd:
                self.sigMarkPointsRun.emit(orig_cmd)

        #elif 'TSeries' in orig_cmd:
            #self.sigTSeriesRun.emit(orig_cmd)

        return parts[1:-1]