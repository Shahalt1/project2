import text_to_gcode
from gcodeparser import GcodeParser
import turtle
from tkinter import *
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cairosvg
import io


class TurtleCanvas(turtle.RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas

    def move(self, x, y):
        self.goto(x * 2, y * 2)

window = Tk()

canvas = Canvas(master=window, width=800, height=800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

draw = TurtleCanvas(canvas)


def draw_with_turtle(commands):
    draw.speed(0)
    for command in commands:
        if 'X' in command.params.keys() or 'Y' in command.params.keys():
            x = command.params.get('X', 0)
            y = command.params.get('Y', 0)
            if command.command == ('G', 0):
                draw.penup()
                draw.move(x, y)
            elif command.command == ('G', 1):
                draw.pendown()
                draw.move(x, y)
    draw.hideturtle()

def play(gcode):
    draw_with_turtle(GcodeParser(gcode).lines)

def Take_input():
    INPUT = input.get("1.0", "end-1c")
    if INPUT == "":
        svg2gcode()
        with open('drawing.gcode', 'r') as f:
            gcode = f.read()
        play(gcode)
        Output.insert(END, gcode)
    else:
        gcode = text_to_gcode.main(INPUT)
        play(gcode)
        Output.insert(END, gcode)
        var1.set("Length of G-code : " + str(len(gcode)))
        var2.set("Length of Text : " + str(len(INPUT)))
        var3.set("Time taken to write : " + str(round(len(gcode)/3000, 2)) + ' seconds')
    
def svg2gcode():
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=5)
    curves = parse_file(filename()) # Parse an svg file into geometric curves
    gcode_compiler.append_curves(curves) 
    gcode_compiler.compile_to_file("drawing.gcode", passes=2)

def filename():
    f_types = [('SVG Files', '*.svg')]   # type of files to select 
    filename = filedialog.askopenfilename(filetypes=f_types)
    return filename

def show_svg():
    image_data = cairosvg.svg2png(url=filename())
    image = Image.open(io.BytesIO(image_data))
    basewidth = 50
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    resized_image = image.resize((basewidth, hsize), resample=Image.BILINEAR)
    
    l7 = Label(window, text="SVG Image").place(x=1060, y=100)
    tk_image = ImageTk.PhotoImage(resized_image)
    img_svg=Label(window, image=tk_image).place(x=1060, y=140)
    img_svg.pack(expand=True, fill="both")
    
    
# ---------------------------------------------------------------------------------------


var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

plot = Button(master=window, text="Plot!", command=lambda:Take_input())
plot.config(bg="cyan", fg="black")
plot.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

input = Text(window, height = 10, width = 25, bg = "light yellow")
input.grid(padx=2, pady=2, row=3, column=11, sticky='nsew')

Output = Text(window, height = 15, width = 25, bg = "light cyan")
Output.grid(padx=2, pady=2, row=6, column=11, sticky='nsew')

b1 = Button(window, text='Upload File', width=20,command = lambda:show_svg())
b1.config(bg="cyan", fg="black")
b1.grid(padx=2, pady=2, row=0, column=13, sticky='nsew')

l1 = Label(window, text = "Enter text to Plot").place(x = 870, y = 110)  
l2 = Label(window, text = "Gcode for above Text").place(x = 860, y = 390)  
l3 = Label(window, text = "Statistics for Plotting").place(x=860, y=700)
l4 = Label(window, textvariable = var1).place(x=810, y=730)
l5 = Label(window, textvariable = var2).place(x=810, y=750)
l6 = Label(window, textvariable = var3).place(x=810, y=770)


window.mainloop()
