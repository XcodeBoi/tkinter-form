# pyright: strict

# a frame for a widget and an assoicated text piece

from typing import Union, Any, Literal
import tkinter as tk
from .raw.generic import *


# the barebones version of named widget
class BareBonesNamedWidget(Widget, tk.Frame):
    def __init__(self, parent: tk.Frame, textWidth: Union[None, int] = None, **frameOptions: Any):
        
        # initalise frame for content
        super().__init__(parent, **self.style(), **frameOptions)
        self.columnconfigure(1, weight = 1)

        # widget placeholder
        self.widget: Any = None

        # text widget
        unpackableTextWidth: Dict[str, int] = { "width": textWidth } if textWidth else {}
        self.textField: TextField = TextField(self, **unpackableTextWidth)

        # style information
        self.gridArgs: Dict[str, Dict[str, Union[str, int]]] = {
            "both": {},
            "text": {},
            "widget": {}
        }

    # set the style arguments
    def setStyle(self, styleArgs: Dict[str, Dict[str, Union[str, int]]]):
        self.gridArgs.update(styleArgs)
    
    # merges general and specfic style
    def getStyle(self, type: Literal["text", "widget"]) -> Dict[str, Union[str, int]]:
        return { **self.gridArgs["both"], **self.gridArgs[type] }

    # set text next to widget
    def setText(self, text: str):
        self.textField.configure(text = text)
        self.__placeText(**self.getStyle("text")) # type: ignore

    # place text widget
    # private as we don't want to ever replace the text manually
    # safe as we don't ever call this without first calling setText
    def __placeText(self, **gridArgs: Any):
        self.textField.grid(column = 0, row = 0, **gridArgs)

    # unsafe version, where the developer manually verifies and promises me the text has
    # already been placed. Used currently for MessageButton
    def unsafe__setText(self, text: str):
        self.textField.configure(text = text)

    # set the widget
    # widget should be a reference to a widget constructor, not an instance
    # kind of like a class decorator. but this isnt a super class its just calling
    # the constructor.
    def setWidget(self, widget: Any, *args: Any, **kwargs: Any):
        self.widget = widget(self, *args, **kwargs)
        self.__placeWidget(**self.getStyle("widget")) # type: ignore

    # place the assoicated widget
    def __placeWidget(self, **gridargs: Any):
        # placeWidget will only ever be called after self.widget is defined by setWidget
        # hence we don't need to worry about operating on a None type
        self.widget.grid(column = 1, row = 0, **gridargs)

# the default named widget
class NamedWidget(BareBonesNamedWidget):
    def __init__(self, parent: tk.Frame, text: str, **frameOptions: Any):
        # initalise frame for content
        super().__init__(parent, **frameOptions)
        
        # set up styling
        self.setStyle({
            "both": { "pady": 5},
            "text": { "padx": 10, "sticky": "n" },
            "widget": { "padx": 10, "sticky": "ne" }
        })
        
        self.setText(text)
    
    # retrieves value from widget field
    def get(self) -> str:
        return self.widget.get()

