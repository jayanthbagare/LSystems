
#Settings for Fractal plant
axiom = 'X'
ruleset = {"X":"F+[[X]-X]-F[-FX]+X","+":"+","-":"-","F":"FF","[":"[","]":"]"}
generations = 6
angle = 25
line_length = 3

#Settings for Dragon Curve
#axiom = 'F'
#ruleset = {"F":"F+G","G":"F-G","+":"+","-":"-"}
#angle = 90
#generations = 10
#line_length = 10

#Settings for Sierpinski's Triangle
#axiom = "F-G-G"
#ruleset = {"F":"F-G+F+G-F","G":"GG","+":"+","-":"-"}
#angle = 120
#generations = 6
#line_length = 5

#Settings for Koch Curve
#axiom = 'F'
#ruleset = {"F":"F+F-F-F+F","+":"+","-":"-"}
#angle = 90
#generations = 3
#line_length = 14

def setup():
    size(800,800)
    stroke('#59A96A')
    strokeWeight(2)

def draw():
    background('#F2F5DE')
    out = generate_grammar(axiom,ruleset,generations)
    translate(width/2,height)
    parse_and_draw(out)
    noLoop()
    

def generate_grammar(axiom,ruleset,generations):
    str_generated = axiom
    for i in range(generations):
        str_calculated = ''
        for char in list(str_generated):
            str_calculated += ruleset[char]
        str_generated = str_calculated
    return str_calculated

def parse_and_draw(str_draw):
    for char in list(str_draw):
        if(char) == 'F':
            line(0,0,0,-line_length)
            translate(0,-line_length)
        elif(char) == 'G':
            line(0,0,0,-line_length)
            translate(0,-line_length)
        elif(char) == '+':
            rotate(radians(angle))
        elif(char) == '-':
            rotate(radians(-angle))
        elif(char) == '[':
            pushMatrix()
        elif(char) == ']':
            popMatrix()
        elif(char) == 'X':
            pass
