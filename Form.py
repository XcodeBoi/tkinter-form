# pyright: strict

# Main form constructor

from typing import Union, Any, Dict, Callable
import tkinter as tk
from .widgets.interactionFeild import NamedInteractionField
from .widgets.raw.generic import Widget
from .widgets.messageButton import MessageButton
from . import errors


# self placing NamedInteractionField
class FormField(NamedInteractionField):
    def __init__(self, *args: Any):
        super().__init__(*args)
        # append to grid
        self.grid(column = 0, row = [*args][0].grid_size()[1], sticky = "we")

# composes the form widgets, The list of fields in the form of a dictionary defined in the readme
class FormFrame(Widget, tk.Frame):
    def __init__(self, parent: Union[tk.Frame, tk.Tk], formLayout: Any):
        super().__init__(parent, **self.style())

        self.grid_columnconfigure(0, weight = 1)

        # add fields; these are self-placing
        self.fields: Dict[str, FormField] = { field:FormField(self, field, widgetInformation) for (field, widgetInformation) in formLayout.items() }

        # add submit button, append to grid with alignment information
        self.button: MessageButton = MessageButton(self, "Submit") 
        # append after form fields 
        self.button.grid(column = 0, row = self.grid_size()[1], padx = 10, pady = 5, sticky = "e")
        
    # returns an object of data from the form
    def data(self) -> Dict[str, str]:
        return { name:data.get() for (name, data) in self.fields.items() }

    # empties all feilds of their current values
    def clearFields(self) -> None:
        for widget in self.fields.values():
            widget.clearValue()
    
    # set the command to occur on button press
    def setCommand(self, func: Callable[[Dict[str, str]], Union[str, None]]):
        # the decorator passes self.data to the anonymous function passed into the parent method
        def buttonCommand():
            # clear the user message field
            self.button.showMessage("")
            
            # clear the fields when success occurs
            # and allow a user to show a custom return message
            def uiSuccess(result: Union[str, None] = None) -> str:
                self.clearFields()
                return result if result else "Success!"

            try:
                result: Union[str, None] = func(self.data())
                # user feedback success
                self.after(200, lambda: self.button.showMessage(uiSuccess(result)))
                
            except errors.UiError as error:
                errorText: str = str(error)
                usrErrorText: str = errorText if errorText else "Failure."
                # user feedback fail
                self.after(200, lambda: self.button.showMessage(usrErrorText))
        self.button.setCommand(buttonCommand)

