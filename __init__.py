# pyright: strict

# public API for tk form module

from typing import Union, Any
import tkinter as tk

# main form constructor
from .Form import FormFrame

def new(parent: Union[tk.Frame, tk.Tk], formLayout: Any) -> FormFrame:
    return FormFrame(parent, formLayout)
    
# accessor for raw widgets
from .widgets.raw import generic, multi

class raw: 
    TextField = generic.TextField
    EntryField = generic.EntryField
    DropDown = generic.DropDown
    RadioButtons = multi.RadioButtons
    MultiDrop = multi.MultiDrop

# export error classes for external use

from . import errors

class error:
    UiError = errors.UiError
