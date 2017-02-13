from sys import platform as _platform

class System():
    "Implements all regarding system on which Robbie framework is running"
    
    def get_os(self):
        "Gets OS name as string"
        
        switcher={
        "linux": "Linux",
        "linux2": "Linux",
        "darwin": "MacOS",
        "win32": "Windows",
        }
        return switcher.get(_platform,"Unknown")
