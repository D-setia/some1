from math import frexp
from manim import *


config.background_color = "#04f404"


textColorNormal = WHITE
textColorPositive = "#43b929"
textColorNegative = "#ff2e00"
lineColor = WHITE
axesColor = WHITE
vertexColor = "#e6af2e"
selectedVertexColor = "#058ed9"


class SimplexOnScreenDispScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        self.camera.frame.scale(0.95).shift(UP*0.6, RIGHT*1.5)

        axes = Axes(
            x_length= 14,
            y_length= 14*9/16,
            x_range=[-4*16/9, 10*16/9, 1],
            y_range=[-4, 10, 1],
            axis_config={"color":axesColor},
            # tips= False
        )

        axes_labels = axes.get_axis_labels()
        axes_labels.set_color(WHITE)


        constraint1 = axes.get_graph(lambda x: x+2, color = lineColor)
        constraint2 = axes.get_graph(lambda x: x/3+3, color = lineColor)
        constraint3 = axes.get_graph(lambda x: -3*x+18, color = lineColor)
        constraint4 = axes.get_graph(lambda x: x-3, color = lineColor)
        constraints = VGroup(constraint1, constraint2, constraint3,constraint4)
        

        dot1 = Dot([-3, -1.68, 0], color = vertexColor).scale(1.2)
        dot2 = Dot([-3, -0.55, 0], color = vertexColor).scale(1.2)
        dot3 = Dot([-2.15, 0.28, 0], color = vertexColor).scale(1.2)
        dot4 = Dot([-0.46, 0.85, 0], color = vertexColor).scale(1.2)
        dot5 = Dot([-0.05, -0.42, 0], color = vertexColor).scale(1.2)
        dot6 = Dot([-1.31, -1.68, 0], color = vertexColor).scale(1.2)
        
        selectedDot = Dot(ORIGIN, color = selectedVertexColor).scale(1.2)
        selectedDot.shift(dot2.get_center())
    
        vertices = VGroup(dot1, dot2, dot3, dot4, dot5, dot6)


        feasibleArea = Polygon([-3, -1.68, 0], [-3, -0.55, 0], [-2.15, 0.28, 0], [-0.465, 0.85, 0], [-0.05, -0.42, 0], [-1.31, -1.68, 0])
        feasibleArea.set_stroke(width=3, color = WHITE)
        feasibleArea.set_fill(PURPLE_A, opacity = 1)

        self.add(axes, axes_labels, feasibleArea, constraints, vertices)
        self.wait(3)

        self.play(ApplyMethod(dot1.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)
        self.play(ApplyMethod(dot2.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)
        self.play(ApplyMethod(dot3.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)
        self.play(ApplyMethod(dot4.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)
        self.play(ApplyMethod(dot5.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)
        self.play(ApplyMethod(dot6.set_color, selectedVertexColor), run_time = 0.5)
        # self.wait(0.3)

        self.wait(3)

        # self.play(ApplyMethod(dot1.set_color, vertexColor), ApplyMethod(dot2.set_color, vertexColor), ApplyMethod(dot6.set_color, vertexColor))
        self.play(FadeOut(dot1, dot2, dot6))
        self.wait(2)


