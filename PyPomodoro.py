import time
from time import strftime
import os
import sys

import PyQt5
from PyQt5 import QtWidgets,QtCore
import appdirs
from pydub import AudioSegment
from pydub.playback import play
import atexit

from PomodoroWindow import Ui_AppWindow


class PomodoroApp(Ui_AppWindow):
    def __init__(self,screen):
        super().__init__()

        self.setupUi(screen)
        screen.show()

        

        #Create Variables
        self.timer = QtCore.QTimer()
        
        self.workClock = 0
        self.restClock = 0

        self.loadPrevious()
        #Load Signals
        self.signalInit()


    def updateCountDown(self,lcd,timer):
        #Takes public clockTime and prints to QLCDNumber
        minute,sec = divmod(timer,60)
        
        if timer >= 6000:
            lcd.setDigitCount(6)
        else:
            lcd.setDigitCount(5)
        
        #Fixes graphical bug
        if sec < 10:
            lcd.display('{}:0{}'.format(minute,sec))
        else:
            lcd.display('{}:{}'.format(minute,sec))



    def setClockTimesButton(self,time,updateCount=True):
        self.timer.stop()
        self.workClock, self.restClock = time
        self.initialTime = time
        
        if updateCount == True:
            self.updateCountDown(self.workTimer,self.workClock)
            self.updateCountDown(self.restTimer,self.restClock)

        #Updates Sliders
        #Divide by 60 to return to minutes
        self.workSlider.setValue(self.workClock//60)
        self.restSlider.setValue(self.restClock//60)

        self.truncateToFile()

    def setClockTimesSlider(self,timer):
        if not self.timer.isActive():
            #Multiply values by 60 to convert to seconds
            if timer == 'work':
                self.workClock = self.workSlider.value()*60
                self.initialTime = [self.workClock,self.restClock]

                self.updateCountDown(self.workTimer,self.workClock)
            elif timer == 'rest':
                self.restClock = self.restSlider.value()*60
                self.initialTime = [self.workClock,self.restClock]

                self.updateCountDown(self.restTimer,self.restClock)
                self.truncateToFile()
        else:
            pass


        
    def clockTick(self):
        if self.workClock >= 0:
            self.updateCountDown(self.workTimer,self.workClock)
            self.workClock-=1
        elif self.workClock == -1:
            self.ringSound()
            self.workClock -=1
        elif self.restClock >= 0:
            self.updateCountDown(self.restTimer,self.restClock)
            self.restClock-=1
        elif self.restClock == -1:
            self.ringSound()
            self.timer.stop()


    def ringSound(self):
        cwd = os.getcwd()
        p = os.path.join(cwd,'Sounds/bell1.wav')
        song = AudioSegment.from_wav(p)
        play(song)

    def toggleClockTick(self,signal):
        if signal:
            self.timer.start(1000)
        else:
            self.timer.stop()



    def signalInit(self):
        self.timer.timeout.connect(lambda: self.clockTick())

        self.fifteenFivePreset.clicked.connect(lambda: self.setClockTimesButton([900,300]))
        self.twentyfiveFivePreset.clicked.connect(lambda: self.setClockTimesButton([1500,300]))
        self.fortyfiveFivePreset.clicked.connect(lambda: self.setClockTimesButton([2700,600]))

        self.startButton.clicked.connect(lambda: self.toggleClockTick(True))
        self.pauseButton.clicked.connect(lambda: self.toggleClockTick(False))
        self.resetButton.clicked.connect(lambda:self.setClockTimesButton(self.initialTime))

        self.workSlider.valueChanged.connect(lambda:self.setClockTimesSlider('work'))
        self.restSlider.valueChanged.connect(lambda:self.setClockTimesSlider('rest'))

    def truncateToFile(self):
        #TODO Make this function less dumb
        self.configFile.seek(0)
        self.configFile.write('{}:{}'.format(self.workClock,self.restClock))
        self.configFile.truncate()


    def loadPrevious(self):

        appname = 'PomodoroTimer'
        appauthor = 'PSU3D0'

        sysDir = appdirs.user_config_dir(appname=appname,appauthor=appauthor)

        self.configDir = os.path.join(sysDir,'defaults.txt')

        if os.path.exists(self.configDir):
            self.configFile = open(self.configDir,'r+')
            time = [int(x) for x in self.configFile.readline().rstrip('\n').split(":")]
            self.setClockTimesButton(time) 

        else:
            try:
                os.makedirs(sysDir)
            except FileExistsError:
                pass
            self.configFile = open(self.configDir,'w+')
            self.setClockTimesButton([1500,300])
    



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    mWindow = QtWidgets.QDialog()
    Main = PomodoroApp(mWindow)


    #Saves params to file on program exit
   # atexit.register(Main.truncateToFile())

    sys.exit(app.exec_())
        
