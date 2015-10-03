import os, sys

from Utils import *

class SlideShow:
    def __init__(self, inputPath, config):
        self.config = config
        self.currentIndex = -1;
        self.startCurrentIndex = -1;
        if inputPath.startswith("file://"):
            inputPath = inputPath[7:]
            inputPath = urllib2.unquote(inputPath)
        self.inputPath = inputPath
        self.inputDir = self.inputPath
        inputFile = None
        if os.path.isfile(self.inputPath):
            self.inputDir,inputFile = os.path.split(self.inputPath)
        self.currentIndex = 0
        allData = os.listdir(self.inputDir)
        if (allData == None) or (len(allData) <= 0):
            return;
        allData = sorted(allData, key = stringSplitByNumbers)
        self.files = []
        for f in allData:
            tf = os.path.join(self.inputDir, f)
            if os.path.isfile(tf):
                canAdd = True
                if self.config.detectImages:
                    try:
                        timg = Image.open(tf)
                    except:
                        canAdd = False
                if not canAdd: continue
                self.files.append(tf)
                if((inputFile != None) and (inputFile == f)):
                    self.currentIndex = len(self.files) - 1
        self.startCurrentIndex = self.currentIndex

    def hasFiles(self):
        return (self.files != None) and (len(self.files) > 0)

    def getCurrent(self):
        if not self.hasFiles():
            raise StopIteration
        return self.files[self.currentIndex]

    def getExtra(self):
        if not self.hasFiles():
            return ''
        return "[{0} / {1}] ".format(self.currentIndex + 1, len(self.files))

    def moveNext(self):
        if not self.hasFiles():
            raise StopIteration
        self.currentIndex += 1
        if self.currentIndex >= len(self.files):
            self.currentIndex = 0;
        if (not self.config.loop) and (self.startCurrentIndex == self.currentIndex):
            raise StopIteration
        return self.getCurrent()

    def movePrevious(self):
        if not self.hasFiles():
            raise StopIteration
        if not self.config.loop:
            return
        self.currentIndex -= 1
        if self.currentIndex < 0:
            self.currentIndex = len(self.files) - 1
        if (not self.config.loop) and (self.startCurrentIndex == self.currentIndex):
            raise StopIteration
        return self.getCurrent()
        
    def moveFirst(self, first):
        if not self.hasFiles():
            raise StopIteration
        if not self.config.loop:
            return
        self.currentIndex = 0
        if not first:
            self.currentIndex = len(self.files) - 1
        return self.getCurrent()
     
    def removeCurrent(self):
        if not self.hasFiles():
            raise StopIteration
        del self.files[self.currentIndex]
        if len(self.files) <= 0:
            self.currentIndex = -1
            raise StopIteration
        if self.currentIndex == len(self.files):
            self.currentIndex = 0;
