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

NO_COLOR_NODE_COLOR = 'k'  # Color for "just fill everything in" mode


WIDTH = 'width'

DEFAULT_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'lightgray',
    WIDTH: 3.0,
}
TRAVELLED_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'black',
    WIDTH: 3.0,
}


def get_key_by_list_value(dictionary, val):
    for k, list_v in dictionary.items():
        for v in list_v:
            if v == val:
                return k
    return None
