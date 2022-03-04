# pyright: strict

# all errors used throughout the project

# ui form creation exception triggered on malformed dictionary argument
# to be called on NON-RAW classes, as raw classes are potentially not formed by the
# intake dictionary for top level Form
class InvalidUiDict(Exception):
    pass

# exported with __init__.py to be used by other programs. 
# Though only used in the context of form set command
class UiError(Exception):
    pass
