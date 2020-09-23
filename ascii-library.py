

class Canvas: 

    def __init__

    def add 

    def clear 

    def render 

    def get_char_for_cell 

    





class Shape:

    def covering_pixel 

    def set_fill_char


class Rectangle(Shape):

    def __init__

    def covering_pixel 

    def translate 








#TASK: implement code that can draw rectangles and square 

# Render canvas
# Print the canvas and any shapes to standard output
# Add a shape to a canvas
# shape the shape to add. For now, assume you only have to deal with rectangles
# Clear all shapes from a canvas
# Create a rectangle
# start_x is the X coordinate of the upper-left-hand corner of the rectangle
# start_y is the Y coordinate of the upper-left-hand corner of the rectangle
# end_x is the X coordinate of the lower-right-hand corner of the rectangle
# end_y is the Y coordinate of the lower-right-hand corner of the rectangle
# fill_char is the character that should be used to draw the rectangle
# Change a rectangle's fill character
# char the character to use in order to draw a pre-existing rectangle
# Translate (move left, right, up, or down)
# axis which axis ('x' or 'y') should we translate the rectangle on? Translating on the X-axis will cause the rectangle to move left and right. Translating on the Y-axis will cause the rectangle to move up and down.
# num is how much to move the rectangle. Negative numbers will cause the rectangle to shift left or down. Positive numbers will cause the rectangle to shift right or up.