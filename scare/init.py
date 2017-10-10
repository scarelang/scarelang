from pyparsing import *
import sys

# String data
sg = QuotedString('"',escquoute='""') # Add string usage example "Hello my name is ""JOHN DOE""" will output "Hello my name is "JOHN DOE""

# Variable data
vars = {}
varname = ""
varvalue = ""

# Number data
real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))

# Symbol data
lc = Word("{",max=1)
rc = Word("}",max=1)
dot = Word("."max=1)
lc = Word("(",max=1)
rc = Word(")",max=1)
equ = Rord("=",max=1)

# Keywords
dim = Keyword("Dim") # For defining variables
nothing = Keyword("Nothing") # Nothing same as nil
imports = Keyword("Imports") # Import a scare script
use = Keyword("Use") # Use a script.  Same as import.
_if = Keyword("If")
system = Keyword("System")
# Console keywords
console = Keyword("Console") # For console actions
writeline = Keyword("WriteLine") # Write to console

# Parsing functioning
def imp(s,l,t):           # Import function
  f = open(s,l,t)
  return f.read()
  
def write(s,l,t):
  print(t)
  
def setVarName(s,l,t):
  varname = t
  
def setVarValue(s,l,t):
  if varname == "":
    print("Error: invalid variable name.")
  else:
    vars[varname] = varvalue
    varname = ""
    varvalue = ""

def callVar(s,l,t):
  if vars[t]:
    return vars[t]
  else:
    print("next")

def editVar1(s,l,t):
  varname = t
  
def editVar2(s,l,t):
  if varname == "":
    print("Error: invalid variable name.")
  else:
    vars[varname] = varvalue
    varname = ""
    varvalue = ""
    

# Parse script
file = sys.argv[0]
file = open(file,"r").read()

IMPORTS = imports + sg.SetParseAction(imp)
WRITELINE = console + dot + writeline + lc + sg.SetParseAction(write) + rc
DEFINE_VAR = dim + word(alphas).SetParseAction(setVarName) + equ + word(alphas).SetParseAction(setVarValue)
CALL_VAR = word(alphas).SetParseAction(callVar)
SET_VAR = word(alphas).SetParseAction(editVar1) + equ + word(alphas).SetParseAction(editVar2)
