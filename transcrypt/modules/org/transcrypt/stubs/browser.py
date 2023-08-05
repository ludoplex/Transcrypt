# This module emulates some browser functionality when running on the desktop using CPython

import builtins
import tokenize
import os

from org.transcrypt import utils

# Get environment from runtime and correct executor to be interpreter

pathOfThisFile = os.path.dirname (os.path.abspath (__file__)) .replace ('\\', '/')
__envir__ = utils.Any ()
with tokenize.open (f'{pathOfThisFile}/../__envir__.js') as envirFile:
    exec (envirFile.read ());
__envir__.executor_name = __envir__.interpreter_name

# Set main to commandArgs.source rather than transcrypt
class __main__:
    # Var source is only set if browser module is NOT imported from sphinx conf.py
    __file__ = utils.commandArgs.source if hasattr (utils.commandArgs, 'source') else 'UNKNOWN'
        
# Browser root singleton
class window:
    class console:
        def log(self):
            builtins.print('console.log :\t', *self)
            
        def dir(self):
            builtins.print('console.dir :\t', self, '\tof type\t', type(self))

    def alert(self):
        input(f'window.alert:\t {self}\t(Press [ENTER] to continue)')

# Add attributes of window to global namespace as is done in a browser
for attributeName in window.__dict__:
    vars () [attributeName] = window.__dict__ [attributeName]

# Make print on the desktop add 'console.log' prefix, to distinguish from alert 
def print (*args):
    console.log (*args)

def __new__ (constructedObject):
    return constructedObject
    
__symbols__ = []
def __set_stubsymbols__ (symbols):
    global __symbols__
    __symbols__ = symbols
    
def __pragma__(*args):
    if args [0] == 'defined':
        return any(arg in __symbols__ for arg in args[1 :])
    
