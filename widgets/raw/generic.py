# pyright: strict

# the generic widgets the whole ui is built upon

from typing import Dict, Union, Any, List
import tkinter as tk
# for use in DropDown only
from tkinter import ttk

# fields applied to every widget
# developer note: should always be a superclass of an extended tk widget
# used to colour scheme
# Legacy note: did control the default widget direction
class Widget:
    # default universal colours
    uniStyle: Dict[str, Union[str, int]] = {
        "bg": "grey"
    }
   
    # widget specific
    widgetStyle: Dict[str, Dict[str, Union[str, int]]] = {
        "FormFrame": {
            "bg": "red",
            "highlightthickness": 2,
            "highlightbackground": "blue"
        }
    }
    
    # update universal style
    def changeStyle(self, newColours: Dict["str", "str"]):
        self.uniStyle.update(newColours)

    # update widget specifc style
    def changeWidgetStyle(self, widgetName: str, widgetStyling: Dict[str, Union[str, int]]):
        self.widgetStyle.update({ widgetName: { **widgetStyling } })

    # get the widget styling for the given widget
    def style(self) -> Dict[str, Union[str, int]]:
        return { **self.uniStyle, **self.widgetStyle.get(self.__class__.__name__, {}) }

# default text field, takes a parent widget
class TextField(Widget, tk.Label):
    def __init__(self, parent: tk.Frame, **labelOptions: Any):
        super().__init__(parent, **self.style(), **labelOptions)

# default entry field, takes a parent widget
class EntryField(Widget, tk.Entry):
    def __init__(self, parent: tk.Frame, **entryOptions: Any):
        super().__init__(parent, **self.style(), **entryOptions)

# default drop down
# uses ttk for inbuilt scrolling capability

# this superclass exists to remove incompatible style arguments
class customComboBox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        kwargs.pop("bg")
        super().__init__(*args, **kwargs)

class DropDown(Widget, customComboBox):
    def __init__(self, parent: tk.Frame, items: List[str], width: int = 5, **optionMenuOptions: Any):
        if len(items) == 0:
            raise ValueError("No content in dropdown")
        
        # create TKinter variable to track current value; assoicate it with parent frame
        # note when retrieving this variable you should use self.get() rather than the tkinter variable system 
        self.value: tk.StringVar = tk.StringVar(parent)
        self.value.set(items[0])

        # initalise actual widget
        super().__init__(parent, textvariable = self.value, width = width, **self.style(), **optionMenuOptions)
        
        # further configuration
        # ttk uses this system, rather than the classic tk.configure
        self["values"] = items
        self["state"] = "readonly"
    
    # retrieves dropdown value
    def get(self) -> str:
        return self.value.get()

