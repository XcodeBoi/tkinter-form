### to review
- interactionFields.py line 43

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

### more patterns
- colour inherance happens at the lowest possible level. Raw widgets access the default colour pallette themselves, you do not pass the colours as kw arguments

### Known issues
- Use of type `any` rather than `Widget` subclasses
This is particularly problematic because pyright doesn't like the fact that items subclassed from `Widget` aren't garateed to have the default tkinter placement methods. This is true, I don't know how to warn the developer from doing so

- Duplicate tkinter variable assignment code; Wontfix
