# %%
import figure

myline = figure.line(10, 20)

width, height = myline.get_length()

try:
    rectacgle = figure.area_rectangle(width, height)
    print(rectacgle)
except ValueError:
    print("please input positive number for width and height")

try:
    right_triangle = figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print("please input positive number for width and height")

try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")
    
# %%