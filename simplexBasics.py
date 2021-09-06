from manim import *

config.background_color = "#fefbea"
# config.background_color = "#04f404" bb70c7
# config.background_opacity = 0
config.frame_rate = 30

textColorNormal = "#0c0c0c"
textColorPositive = "#43b929"
textColorNegative = "#ff2e00"
lineColor = "#0c0c0c"
axesColor = BLACK
vertexColor = "#2d2a32"
selectedVertexColor = "#279af1"


class SimplexBasicsScene(MovingCameraScene):
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
        axes_labels.set_color(BLACK)


        constraint1 = axes.get_graph(lambda x: x+2, color = lineColor)
        constraint2 = axes.get_graph(lambda x: x/3+3, color = lineColor)
        constraint3 = axes.get_graph(lambda x: -3*x+18, color = lineColor)
        constraint4 = axes.get_graph(lambda x: x-3, color = lineColor)
        constraints = VGroup(constraint1, constraint2, constraint3,constraint4)

        objectiveFunction = axes.get_graph(lambda x: -x+2, color = textColorPositive)


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
        feasibleArea.set_stroke(width=3, color = "#0c0c0c")
        feasibleArea.set_fill(PURPLE_A, opacity = 1)


        point1Val = MathTex("0", color = textColorNormal)
        point2Val = MathTex("2", color = textColorNormal)
        point3Val = MathTex("5", color = textColorNormal)
        point4Val = MathTex("9", color = textColorNormal)
        point5Val = MathTex("7.5", color = textColorNormal)
        point6Val = MathTex("3", color = textColorNormal)

        point1Val.shift([-3.3, -2, 0])
        point2Val.next_to(dot2,  LEFT)
        point3Val.shift([-2.2, 0.65, 0])
        point4Val.next_to(dot4, RIGHT)
        point5Val.next_to(dot5, RIGHT)
        point6Val.next_to(dot6, DOWN)
        pointVals = VGroup(point1Val, point2Val, point3Val, point4Val, point5Val, point6Val)



        iter0Plus = Text("+", color = textColorPositive, weight=BOLD).shift([-2.2, 0.65, 0])
        iter0Minus = Text("_", color = textColorNegative, weight=BOLD).shift([-3.3, -2, 0])
        iter0Vals = VGroup(iter0Plus, iter0Minus)
        staggeredIterVals = [FadeIn(iter0Plus), FadeIn(iter0Minus)]
        arrow0 = Arrow(start = dot2.get_center(), end = dot3.get_center(), color = BLACK).scale(1.3).shift(UP*0.2, LEFT*0.2)
        

        iterGreater = Text("+", color = textColorPositive, weight=BOLD).scale(1.3).shift([-2.2, 0.65, 0])
        iterLess = Text("+", color = textColorPositive).shift([-3.3, -2, 0])
        iterBothImprov = VGroup(iterGreater, iterLess)
        staggeredIterBothImprov = [FadeIn(iterGreater), FadeIn(iterLess)]
        arrow1 = Arrow(start = dot2.get_center(), end = dot3.get_center(), color = BLACK).scale(1.3).shift(UP*0.2, LEFT*0.2)


        iter1Plus = MathTex("+3", color = textColorPositive).next_to(point3Val, LEFT)
        iter1Minus = MathTex("-2", color = textColorNegative).next_to(point1Val, LEFT)
        iter1Vals = VGroup(iter1Plus, iter1Minus)
        staggeredIter1Vals = [FadeIn(point1Val, point2Val, point3Val), FadeIn(iter1Vals)]
        arrow2 = Arrow(start = dot2.get_center(), end = dot3.get_center(), color = BLACK).scale(1.3).shift(UP*0.2, LEFT*0.2)
        shift1 = []
        for i in range(3):
            shift1.append(np.round(dot3.get_center()[i]-dot2.get_center()[i], 2))

        
        iter2Plus = MathTex("+4", color = textColorPositive).next_to(point4Val, UP)
        iter2Minus = MathTex("-3", color = textColorNegative).next_to(point2Val, UP)
        iter2Vals = VGroup(iter2Plus, iter2Minus)
        staggeredIter2Vals = [FadeIn(iter2Plus), FadeIn(iter2Minus)]
        arrow3 = Arrow(start = dot3.get_center(), end = dot4.get_center(), color = BLACK).scale(1.3).shift(UP*0.2)
        shift2 = []
        for i in range(3):
            shift2.append(np.round((dot4.get_center()[i]-dot3.get_center()[i])*0.8, 2))
        
        iter3a = MathTex("-4", color = textColorNegative).next_to(point3Val, UP)
        iter3b = MathTex("-1.5", color = textColorNegative).next_to(point5Val, UP)
        iter3Vals = VGroup(iter3a, iter3b)
        staggeredIter3Vals = [FadeIn(iter3a), FadeIn(iter3b)]
        # arrow3 = Arrow(start = dot2.get_center(), end = dot4.get_center(), color = BLACK).scale(1.3).shift(UP*0.2, LEFT*0.2)
        

        screenRect = ScreenRectangle(height=10)
        screenRect.set_fill(color=WHITE, opacity=0.9)
        renderingText = Text("Rendering in 1000", color=textColorNormal).scale(1.5).shift(UP, RIGHT)
        dimentionsText = Text("dimentions...", color=textColorNormal).scale(1.5).next_to(renderingText, DOWN)


        staggeredArrows = [Create(arrow2), Create(arrow3)]


        # self.add( feasibleArea, vertices)
        self.wait(0.3)
        self.play(FadeIn(feasibleArea, axes, axes_labels, constraints, vertices))
        self.wait(0.3)

        dotFlickerRunTime = 0.2
        dot1.set_color(selectedVertexColor)
        self.wait(dotFlickerRunTime)
        dot5.set_color(selectedVertexColor)
        dot1.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot3.set_color(selectedVertexColor)
        dot5.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot6.set_color(selectedVertexColor)
        dot3.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot2.set_color(selectedVertexColor)
        dot6.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot4.set_color(selectedVertexColor)
        dot2.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot1.set_color(selectedVertexColor)
        dot4.set_color(vertexColor)
        self.wait(dotFlickerRunTime)
        dot2.set_color(selectedVertexColor)
        dot1.set_color(vertexColor)
        self.wait(dotFlickerRunTime)

        self.play(FadeOut(axes, axes_labels, constraints), self.camera.frame.animate.scale(0.5).shift(DOWN*1.3, LEFT*3.5))
        self.wait(0.1)
        self.play(Create(arrow2))
        self.wait(0.5)
        self.play(Create(arrow3))
        self.wait(0.1)
        self.play(FadeOut(arrow2, arrow3))
        self.wait(0.1)
        self.play(LaggedStart(*staggeredIterVals, lag_ratio=0.1))
        self.wait()
        self.play(Create(arrow0))
        self.wait(3)

        self.play(FadeOut(iter0Vals, arrow0))
        self.wait()
        self.play(LaggedStart(*staggeredIterBothImprov, lag_ratio=0.1))
        self.wait(2.5)
        self.play(Create(arrow1))
        self.wait()
        
        self.play(FadeOut(iterBothImprov, arrow1))
        self.wait(0.5)
        self.play(LaggedStart(*staggeredIter1Vals, lag_ratio=0.6), run_time = 0.5)
        # self.wait(2)
        self.play(Create(arrow2), run_time = 0.5)
        # self.wait(0.1)
        
        self.add(selectedDot)
        dot2.set_color(vertexColor)
        self.play(FadeOut(iter1Vals, arrow2, point1Val), self.camera.frame.animate.shift(shift1), ApplyMethod(selectedDot.shift, shift1), FadeIn(point4Val), run_time = 0.5)
        # self.wait(0.1)
        self.play(LaggedStart(*staggeredIter2Vals, lag_ratio=0.1), run_time = 0.5)
        # self.wait(0.1)
        self.play(Create(arrow3), run_time = 0.5)
        # self.wait(0.1)
        
        self.play(FadeOut(iter2Vals, arrow3, point2Val), self.camera.frame.animate.shift(shift2), ApplyMethod(selectedDot.shift, dot4.get_center()-dot3.get_center()), FadeIn(point5Val), run_time = 0.5)
        # self.wait(0.1)
        self.play(LaggedStart(*staggeredIter3Vals, lag_ratio=0.1))
        self.wait(6)

        self.play(FadeOut(iter3Vals, selectedDot), FadeIn(axes, axes_labels, constraints, point1Val, point2Val, point6Val), self.camera.frame.animate.shift(dot2.get_center()-dot4.get_center(), UP*1.3, RIGHT*3.5).scale(2))
        self.wait(2)

        self.play(objectiveFunction.animate.become(axes.get_graph(lambda x: -x+9, color = textColorPositive)), run_time=3)
        self.wait()

        self.play(FadeIn(screenRect, renderingText, dimentionsText))
        self.wait(4)

       #TODO: Add windows crashing overlay for 1000 dimentions
