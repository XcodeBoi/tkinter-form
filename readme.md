### Basic usage
- todo: step by step guide through this code
#### Final product
```py
import tkinter as tk

import TKform
from dataProcess import exportInformation
import components


formLayout = {
    "ID": { "type": "entry" },
    "First Name": { "type": "entry" },
    "Last Name": { "type": "entry" },
    "DOB": { "type": "custom", "component": components.Birthday },
    "House": { "type": "drop", "content": ["Red", "Blue", "Yellow", "Green"] },
    "Year level": { "type": "drop", "content": ["7", "8", "9", "10", "11", "12"] },
    "Active": { "type": "radio", "content": ["True", "False"], "direction": "horizontal" }
}
 
if __name__ == "__main__":
    root: tk.Tk = tk.Tk()

    mainForm = TKform.new(root, formLayout)
    mainForm.setCommand(exportInformation)
    mainForm.grid(row = 0, column = 0, sticky = "e", padx = 25, pady = 25)

    root.mainloop()
```

### The dictionary
```py
formLayout = {
    "ID": { "type": "entry" },
    "First Name": { "type": "entry" },
    "Last Name": { "type": "entry" },
    "DOB": { "type": "birthday" },
    "House": { "type": "drop", "content": ["Red", "Blue", "Yellow", "Green"] },
    "Year level": { "type": "drop", "content": ["7", "8", "9", "10", "11", "12"] },
    "Active": { "type": "radio", "content": ["True", "False"], "direction": "horizontal" }
}
```

### dev patterns
- colour inherance happens at the lowest possible level. Raw widgets access the default colour pallette themselves, you do not pass the colours as kw arguments

### Known issues
- Use of type `any` rather than `Widget` subclasses
This is particularly problematic because pyright doesn't like the fact that items subclassed from `Widget` aren't garateed to have the default tkinter placement methods. This is true, I don't know how to warn the developer from doing so

- Duplicate tkinter variable assignment code; Wontfix

- Handling of data.
The structure passed becomes inconsistent and messy particularly with flags and custom widgets. This is due to the handling not beingproperly dynamic. While originally clean and self documenting, it has become quite confusing as to how to structure things
