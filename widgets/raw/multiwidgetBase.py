# pyright: strict

# defines the mutli widget container implementation

from .generic import Widget
import tkinter as tk
from typing import Literal, List, Any


# default mutli item widget
class MultiWidget(Widget, tk.Frame):
    def __init__(self, parent: tk.Frame, direction: Literal["vertical", "horizontal"] = "vertical", **subWidgetOptions: Any):
        super().__init__(parent, **self.style())
        
        # keep track of all sub widgets
        # all items should be a Widget subclass
        self.widgets: List[Any] = []

        self.direction = direction

    # place widget in grid of this widget
    def place(self, widget: Any):
        # add to widget tracking
        self.widgets.append(widget)

        # place widget
        # note grid_size() does not return the index, it returns the size. the size is the index + 1
        match self.direction:
            case "vertical":
                # append to row
                widget.grid(column = 0, row = self.grid_size()[1], sticky = "e", pady = 2)
            case "horizontal":
                # append to column
                widget.grid(column = self.grid_size()[0], row = 0, padx = 2)
            case _:
                raise ValueError("Invalid direction")

