# pyright: strict

# The frame used for each field of a form

from .namedWidget import NamedWidget
import tkinter as tk # for typing
from typing import Any
from ..errors import InvalidUiDict
from .raw.generic import *
from .raw.multi import *

# the default named entry field, takes a parent widget
class NamedInteractionField(NamedWidget):
    # widgetInformation matches the structure of a dict defined in the readme
    def __init__(self, parent: tk.Frame, text: str, widgetInformation: Any):
        super().__init__(parent, text = text)

        # save configuration for this widget. Should not be changed
        self.config = widgetInformation

        # add user input widget
        try:
            match widgetInformation["type"]:
                case "entry":
                    self.configWidget(EntryField)
                case "drop":
                    self.configWidget(DropDown, widgetInformation["content"])
                case "radio":
                    self.configWidget(RadioButtons, widgetInformation["content"], direction = widgetInformation["direction"])
                case "multidrop":
                    self.configWidget(MultiDrop, widgetInformation["content"], direction = widgetInformation["direction"])
                case "custom":
                    self.setWidget(widgetInformation["component"], widgetInformation["data"])
                case _:
                    raise InvalidUiDict
        except InvalidUiDict:
            # added for programmer error observability reasons
            print("WARNING: Invalid widget information passed")
            print(widgetInformation)
            # problems will occur if the code contiues to run at all with half constructed widgets
            # so we force an exit. The developer SHOULD NOT be given the option to catch this and 
            # contiue to work with half constructed widgets.
            exit()
    
    # minor abstraction of setWidget to pass kwargs defined in the configuration dictionary
    def configWidget(self, widget: Any, *args: Any, **kwargs: Any):
        self.setWidget(widget, *args, **self.config.get("flags", {}), **kwargs)

