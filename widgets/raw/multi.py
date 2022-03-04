# pyright strict

# Every raw widget that extends the MultiWidget base

from .__generic import RadioButton
from .generic import DropDown
import tkinter as tk # covers type hinting in this file only
from .multiwidgetBase import MultiWidget 
from typing import List, Literal, Any


# default radio buttons
class RadioButtons(MultiWidget):
    def __init__(self, parent: tk.Frame, items: List[str], direction: Literal["vertical", "horizontal"] = "vertical", **radioButtonOptions: Any):
        # create TKinter variable to track current value; assoicate it with parent frame
        # note when retrieving this variable you should use self.get() rather than the tkinter variable system 
        self.value: tk.StringVar = tk.StringVar(parent)
        self.value.set(items[0])

        super().__init__(parent, direction = direction)

        # add named radio buttons
        for name in items:
            self.place(RadioButton(self, name, self.value, **radioButtonOptions))
            
    # retrieves selected radio button
    def get(self) -> str:
        return self.value.get()

# mutliple drop downs in the same frame
class MultiDrop(MultiWidget):
    def __init__(self, parent: tk.Frame, items: List[List[str]], direction: Literal["horizontal", "vertical"] = "horizontal", **optionMenuOptions: Any):
        super().__init__(parent, direction = direction)
        
        for name in items:
            self.place(DropDown(self, name, **optionMenuOptions))

    # retrieves selected values from each of the drop downs
    def get(self) -> List[str]:
        return [widget.get() for widget in self.widgets]

