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
table1.get_horizontal_lines()[2:].set_opacity(0)
table1.get_vertical_lines().set_color(BLACK)
table1.get_vertical_lines()[1:4].set_opacity(0)
table1.shift(DOWN).scale(0.9)




modifiedLastRow1 = VGroup(
    MathTex("x_1", color = textColorNormal), MathTex("\\frac{4}{4}", color = textColorNormal), 
    MathTex("\\frac{1}{4}", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("\\frac{1}{4}", color = textColorNormal), MathTex("\\frac{54}{4}", color = textColorNormal)
)
modifiedLastRow1[0].shift(DOWN*2.6, LEFT*3.7)
modifiedLastRow1[1].shift(DOWN*2.6, LEFT*2.2).scale(0.9)
modifiedLastRow1[2].shift(DOWN*2.6, LEFT*0.45).scale(0.9)
modifiedLastRow1[3].shift(DOWN*2.6, RIGHT).scale(0.9)
modifiedLastRow1[4].shift(DOWN*2.6, RIGHT*2.35).scale(0.9)
modifiedLastRow1[5].shift(DOWN*2.6, RIGHT*3.7).scale(0.9)

modifiedLastRow2 = VGroup(
    MathTex("x_1", color = textColorNormal), MathTex("1", color = textColorNormal), 
    MathTex("0.25", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("0.25", color = textColorNormal), MathTex("13.5", color = textColorNormal)
)
modifiedLastRow2[0].shift(DOWN*2.6, LEFT*3.7)
modifiedLastRow2[1].shift(DOWN*2.6, LEFT*2.2).scale(0.9)
modifiedLastRow2[2].shift(DOWN*2.6, LEFT*0.45).scale(0.9)
modifiedLastRow2[3].shift(DOWN*2.6, RIGHT).scale(0.9)
modifiedLastRow2[4].shift(DOWN*2.6, RIGHT*2.35).scale(0.9)
modifiedLastRow2[5].shift(DOWN*2.6, RIGHT*3.7).scale(0.9)

modifiedLastRow3 = VGroup(
    MathTex("x_1", color = textColorNormal), MathTex("1", color = textColorNormal), 
    MathTex("0", color = textColorNormal), MathTex("-0.09", color = textColorNormal), 
    MathTex("0.273", color = textColorNormal), MathTex("10.64", color = textColorNormal)
)
modifiedLastRow3[0].shift(DOWN*2.6, LEFT*3.7)
modifiedLastRow3[1].shift(DOWN*2.6, LEFT*2.2).scale(0.9)
modifiedLastRow3[2].shift(DOWN*2.6, LEFT*0.45).scale(0.9)
modifiedLastRow3[3].shift(DOWN*2.6, RIGHT).scale(0.9)
modifiedLastRow3[4].shift(DOWN*2.6, RIGHT*2.3).scale(0.9)
modifiedLastRow3[5].shift(DOWN*2.6, RIGHT*3.8).scale(0.9)


modifiedObjFunc1 = VGroup(
    MathTex("Z", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("-0.125", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("0.375", color = textColorNormal), MathTex("20.25", color = textColorNormal)
)
modifiedObjFunc1[0].shift(DOWN*0.55, LEFT*3.7)
modifiedObjFunc1[1].shift(DOWN*0.55, LEFT*2.2).scale(0.9)
modifiedObjFunc1[2].shift(DOWN*0.55, LEFT*0.45).scale(0.9)
modifiedObjFunc1[3].shift(DOWN*0.55, RIGHT).scale(0.9)
modifiedObjFunc1[4].shift(DOWN*0.55, RIGHT*2.35).scale(0.9)
modifiedObjFunc1[5].shift(DOWN*0.55, RIGHT*3.7).scale(0.9)

modifiedObjFunc2 = VGroup(
    MathTex("Z", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("0", color = textColorNormal), MathTex("0.045", color = textColorNormal), 
    MathTex("0.367", color = textColorNormal), MathTex("21.68", color = textColorNormal)
)
modifiedObjFunc2[0].shift(DOWN*0.55, LEFT*3.7)
modifiedObjFunc2[1].shift(DOWN*0.55, LEFT*2.2).scale(0.9)
modifiedObjFunc2[2].shift(DOWN*0.55, LEFT*0.45).scale(0.9)
modifiedObjFunc2[3].shift(DOWN*0.55, RIGHT*0.9).scale(0.9)
modifiedObjFunc2[4].shift(DOWN*0.55, RIGHT*2.35).scale(0.9)
modifiedObjFunc2[5].shift(DOWN*0.55, RIGHT*3.7).scale(0.9)

modifiedR2_1 = VGroup(
    MathTex("s_1", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("2.75", color = textColorNormal), MathTex("1", color = textColorNormal), 
    MathTex("-0.25", color = textColorNormal), MathTex("31.5", color = textColorNormal)
)
modifiedR2_1[0].shift(DOWN*1.575, LEFT*3.7)
modifiedR2_1[1].shift(DOWN*1.575, LEFT*2.2).scale(0.9)
modifiedR2_1[2].shift(DOWN*1.575, LEFT*0.45).scale(0.9)
modifiedR2_1[3].shift(DOWN*1.575, RIGHT).scale(0.9)
modifiedR2_1[4].shift(DOWN*1.575, RIGHT*2.35).scale(0.9)
modifiedR2_1[5].shift(DOWN*1.575, RIGHT*3.7).scale(0.9)

modifiedR2_2 = VGroup(
    MathTex("x_2", color = textColorNormal), MathTex("0", color = textColorNormal), 
    MathTex("1", color = textColorNormal), MathTex("0.36", color = textColorNormal), 
    MathTex("-0.09", color = textColorNormal), MathTex("11.45", color = textColorNormal)
)
modifiedR2_2[0].shift(DOWN*1.575, LEFT*3.7)
modifiedR2_2[1].shift(DOWN*1.575, LEFT*2.2).scale(0.9)
modifiedR2_2[2].shift(DOWN*1.575, LEFT*0.45).scale(0.9)
modifiedR2_2[3].shift(DOWN*1.575, RIGHT).scale(0.9)
modifiedR2_2[4].shift(DOWN*1.575, RIGHT*2.3).scale(0.9)
modifiedR2_2[5].shift(DOWN*1.575, RIGHT*3.7).scale(0.9)

