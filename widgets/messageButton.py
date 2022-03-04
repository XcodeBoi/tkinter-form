# pyright: strict

# the button used at the bottom of the form

from .namedWidget import BareBonesNamedWidget
import tkinter as tk
from typing import Callable

# button with an adjacent text field for user feedback
class MessageButton(BareBonesNamedWidget):
    def __init__(self, parent: tk.Frame, buttonText: str):
        # instantiate a named widget 
        super().__init__(parent)
        
        self.setWidget(tk.Button, text = buttonText)
        self.setText("")
    
    # set command to be triggered for button press
    def setCommand(self, func: Callable[[], None]):
        self.widget.configure(command = func)
    
    # show message to user
    # safe to call unsafe__setText here because self.setText() is called in the constructor
    def showMessage(self, text: str):
        self.unsafe__setText(text)

