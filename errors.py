# pyright: strict

# all errors used throughout the project

# ui form creation exception triggered on malformed dictionary argument
# to be called on NON-RAW classes, as raw classes are potentially not formed by the
# intake dictionary for top level Form
class InvalidUiDict(Exception):
    pass

