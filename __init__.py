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
    Widget = generic.Widget
    TextField = generic.TextField
    EntryField = generic.EntryField
    DropDown = generic.DropDown
    RadioButtons = multi.RadioButtons
    MultiDrop = multi.MultiDrop

# accessor for composition related things
from .widgets.raw.multiwidgetBase import MultiWidget

class composition:
    Multi = MultiWidget

# export error classes for external use
from . import errors

class error:
    UiError = errors.UiError

# unsafe things. Avert your gaze and wish you wern't here
# exports for things intended to be private, but we allow because I'm lazy and implemented some
# stuff in fairly ok ways i want to use in other projects but don't want to make sure the api
# works for every use case
from .widgets.namedWidget import NamedWidget

class unsafe:
    class composition:
        # NamedWidget is supposed to be private, but a nice use case for it occured
        # in an external project so I allow it to be exported
        # this is hacky. hacky is bad except where the project is small scale
        # and interwoven unexpected deps don't make your head hurt too much
        NamedWidget = NamedWidget
        

# TODO: style interface for mutating the base Widget class.
# Also document that it must be called prior to widget construction
