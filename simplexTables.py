from manim import *


textColorNormal = "#0c0c0c"

rowLables1 = [MathTex("x_1", color = textColorNormal).scale(1.2), MathTex("x_2", color = textColorNormal).scale(1.2), 
        MathTex("s_1", color = textColorNormal).scale(1.2), MathTex("s_2", color = textColorNormal).scale(1.2), 
        Tex("C", color = textColorNormal).scale(1.2)]

columnLabels1 = [MathTex("Z", color = textColorNormal), MathTex("s_1", color = textColorNormal), 
MathTex("s_2", color = textColorNormal)]

table1 = MathTable(
    [["-1.5","-0.5","0","0","0"],
    ["1","3","1","0","45"], 
    ["4","1","0","1","54"]],
    col_labels= rowLables1,
    row_labels= columnLabels1,
    element_to_mobject_config={"color":textColorNormal},
    h_buff=1,
)

table1.get_horizontal_lines().set_color(BLACK)
table1.get_horizontal_lines()[1:].set_opacity(0)
table1.get_vertical_lines().set_color(BLACK)
table1.get_vertical_lines()[1:4].set_opacity(0)
table1.shift(DOWN).scale(0.9)





rowLables2 = [MathTex("x_1", color = textColorNormal).scale(10/9), MathTex("x_2", color = textColorNormal).scale(10/9), 
        MathTex("s_1", color = textColorNormal).scale(10/9), MathTex("s_2", color = textColorNormal).scale(10/9), 
        Tex("C", color = textColorNormal).scale(10/9)]

columnLabels2 = [MathTex("Z", color = textColorNormal).scale(10/9), MathTex("s_1", color = textColorNormal).scale(10/9), 
MathTex("s_2", color = textColorNormal).scale(10/9)]

table2 = MathTable(
    [["\\frac{2}{3}","1","1","1","1"], 
    ["1","1","1","1","1"], 
    ["1","1","1","1","1"]],
    col_labels= rowLables2,
    row_labels= columnLabels2,
    element_to_mobject_config={"color":textColorNormal}
)

table2.get_horizontal_lines().set_color(BLACK)
table2.get_horizontal_lines()[1:].set_opacity(0)
table2.get_vertical_lines().set_color(BLACK)
table2.get_vertical_lines()[1:4].set_opacity(0)
table2.shift(DOWN).scale(0.9)




rowLables3 = [MathTex("x_1", color = textColorNormal), MathTex("x_2", color = textColorNormal), 
        MathTex("s_1", color = textColorNormal), MathTex("s_2", color = textColorNormal), 
        MathTex("C", color = textColorNormal)]

columnLabels3 = [MathTex("Z", color = textColorNormal), MathTex("s_1", color = textColorNormal), 
MathTex("s_2", color = textColorNormal)]

table3 = MathTable(
    [["1","1","1","1","1"], 
    ["1","1","1","1","1"], 
    ["1","1","1","1","1"]],
    col_labels= rowLables1,
    row_labels= columnLabels1,
    element_to_mobject_config={"color":textColorNormal}
)

table3.get_horizontal_lines().set_color(BLACK)
table3.get_horizontal_lines()[1:].set_opacity(0)
table3.get_vertical_lines().set_color(BLACK)
table3.get_vertical_lines()[1:4].set_opacity(0)
table3.shift(DOWN).scale(0.9)




rowLables4 = [MathTex("x_1", color = textColorNormal), MathTex("x_2", color = textColorNormal), 
        MathTex("s_1", color = textColorNormal), MathTex("s_2", color = textColorNormal), 
        MathTex("C", color = textColorNormal)]

columnLabels1 = [MathTex("Z", color = textColorNormal), MathTex("s_1", color = textColorNormal), 
MathTex("s_2", color = textColorNormal)]

table4 = MathTable(
    [["1","1","1","1","1"], 
    ["1","1","1","1","1"], 
    ["1","1","1","1","1"]],
    col_labels= rowLables1,
    row_labels= columnLabels1,
    element_to_mobject_config={"color":textColorNormal}
)

table4.get_horizontal_lines().set_color(BLACK)
table4.get_horizontal_lines()[1:].set_opacity(0)
table4.get_vertical_lines().set_color(BLACK)
table4.get_vertical_lines()[1:4].set_opacity(0)
table4.shift(DOWN).scale(0.9)