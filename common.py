"""
color: node color string
val: node additional value (such as a number or letter)
props: tuple of special node properties
"""
COLOR = 'color'
VALUE = 'value'
PROPS = 'props'

DEFAULT_ATTRIBUTE_VALUES = {
    COLOR: 'lightgray',  # Uncolored color, can color over
    VALUE: None, 
    PROPS: (),
}
