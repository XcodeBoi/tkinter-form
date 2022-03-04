# pyright: strict

# these classes are NOT exposed publically as they should be called exclusively through the multi widget interface

from typing import Any
import tkinter as tk
from .generic import Widget


# default SINGULAR radio button
class RadioButton(Widget, tk.Radiobutton):
    def __init__(self, parent: tk.Frame, text: str, variable: tk.StringVar, **radioButtonOptions: Any):
        super().__init__(parent, text = text, value = text, variable = variable, **self.style(), **radioButtonOptions)

