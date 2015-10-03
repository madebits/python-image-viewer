import os, sys
import subprocess

class UserCommands:
    def __init__(self, commandsFile):
        self.commands = None
        if (commandsFile != None) and os.path.isfile(commandsFile):
            with open(commandsFile) as f:
                self.commands = f.readlines()
    
    # quit|separator|commandParts
    def parseCommand(self, command, currentFile):
        if (command == None) or (len(command) <= 0): return None
        parts = command.strip('\r\n \t').split('|', 3);
        if len(parts) < 3: return None
        shouldQuit = parts[0].strip() == 'quit'
        commandParts = parts[2].split(parts[1])
        for i, p in enumerate(commandParts):
            p = p.strip()
            if currentFile != None:
                p = p.replace("%f%", currentFile)
            commandParts[i] = p
        return (shouldQuit, commandParts)
    
    def runCommand(self, commandIndex, currentFile):
        if currentFile == None: return
        if (self.commands == None) or (len(self.commands) == 0) or commandIndex >= len(self.commands): return
        commandText = self.commands[commandIndex]
        command = self.parseCommand(commandText, currentFile)
        if command == None: return
        commandText = " ".join(command[1])
        text = "Run"
        if command[0]:
            text += " and quit"
        if not askokcancel("Confirm Command", text + ":\n" + commandText):
                return
        #subprocess.call(command[1], shell=False)
        subprocess.Popen(command[1], shell=False)
        if command[0]:
            quit(None)
    
    def listCommands(self):
        if (self.commands == None) or (len(self.commands) == 0): return ""
        res = "Custom commands (key command):\n"
        for i, c in enumerate(self.commands):
            if i > 9: break
            command = self.parseCommand(c, None)
            if command == None: continue
            commandText = " ".join(command[1])
            if command[0]: commandText += " # quit after run"
            res += " {0} {1}\n".format(i + 1, commandText)
        return res
