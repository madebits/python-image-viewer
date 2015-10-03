try:
    from Tkinter import *
    from tkMessageBox import *
    from tkFileDialog import *
    import urllib2
    
except:
    from tkinter import *
    from tkinter.messagebox import *
    from tkinter.filedialog import *
    import urllib

class HelpBox(Toplevel):

    def __init__(self, root, extra = None):
        Toplevel.__init__(self, root)
        self.root = root
        self.title("Image Viewer Help")
        self.geometry("480x360")
        self.resizable(width=FALSE, height=FALSE)
        self.maxsize(width=480, height=360)
        self.bind("<Escape>", self.cancel)
        self.bind("q", self.cancel)
        self.bind("<F1>", self.cancel)
        self.bind("h", self.cancel)
        text = Text(self)
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)
        data = """http://madebits.com Press Esc key or right-click to close help.

miv.pyw [OPTIONS] pathToFileOrFolder

Command-line options:
 -?\t\tshow this help
 -d\t\tdetect image files (a bit slower)
 -w\t\tshow window border (640x480)
 -l\t\tloop only once forward (previous not allowed)
 -s\t\tauto start slideshow
 -st timeInSeconds for auto start slideshow (default 3)
 -z fit | scale | fill sets default zoom mode
 -c customCommandsFile
 
Application commanding keys:
 F1 or h\t\tshow / hide this help
 Esc or q\t\tquit
 Space or Down or Enter
 \t\tnext file
 Up\t\tprevious file
 Right\t\tzoom 100%
 Left\t\tzoom default (fit)
 z\t\tswitch default zoom fit / scale / fill
 r\t\trotate 90 degrees right
 Shift+r\t\trotate 90 degrees left
 g\t\tswitch grayscale filter
 s\t\tswitch auto slideshow
 o\t\topen a new file
 f\t\tswitch fullscreen
 Del or d\t\tdelete current file
 Shift+arrows\t\ton 100% zoom pan image

Mouse:
 Right\t\tswitch zoom 100% / default (fit)
 Left\t\ton 100% zoom drag to pan image
 Wheel\t\tmove next / previous
      \t\ton 100% zoom pan up / down
      \t\tor with Shift key left / right
"""
        if extra != None:
            data += '\n' + extra + '\n'
        data += """Custom commands file can contain up to 9 lines mapped
to keyboard keys 1 to 9 with custom commands of form:
quit|separator|commandPartsSeparatedWithSeparator
 quit is optional if set the application exits after command
 %f% in commandParts is replaced with current file path

Examples: 
quit|,|pinta,%f%
|,|pcmanfm,-w,%f%
"""
        text.insert(INSERT, data)
        text.config(state=DISABLED)
        text.bind("<Button-3>", self.cancel)
        text.pack(side=LEFT, fill=Y)
        # modal
        self.focus_set()
        self.grab_set()
        self.transient(root)
        self.wait_window(self)

    def cancel(self, event=None):
        self.root.focus_set()
        self.destroy()
        
