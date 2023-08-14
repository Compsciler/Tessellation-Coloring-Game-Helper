"""
color: node color string
val: node additional value (such as a number or letter)
props: tuple of special node properties
"""
COLOR = 'color'
VALUE = 'value'
PROPS = 'props'

DEFAULT_NODE_ATTRIBUTE_VALUES = {
    COLOR: 'lightgray',  # Uncolored color, can color over
    VALUE: None, 
    PROPS: (),
}


WIDTH = 'width'

DEFAULT_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'gray',
    WIDTH: 1.0,
}
TRAVELLED_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'black',
    WIDTH: 3.0,
}
