from manim import *


config.background_color = "#fefbea"
# config.frame_rate = 
# config.background_color = "#04f404" bb70c7
# config.background_opacity = 0
config.frame_rate = 30


textColor = BLACK



class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class LinEqBasicsScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        self.camera.frame.scale(0.7).shift(UP*1.5, RIGHT*2.8)

        axes = Axes(
            x_range=[-6*16/9, 6*16/9, 1],
            y_range=[-6, 6, 1],
            y_length=7,
            axis_config={"color":BLACK},
        )

        axes_labels = axes.get_axis_labels()
        axes_labels.set_color(textColor)

        line1 = axes.get_graph(lambda x: -0.5*x+3, color = BLACK)
        line1Copy = axes.get_graph(lambda x: -0.5*x+3, color = BLACK)
        line2 = axes.get_graph(lambda x: -5*x+3, color = BLACK)
        line3 = axes.get_graph(lambda x: 3*x+3, color = BLACK)
        line4 = axes.get_graph(lambda x: -1*x+3, color = BLACK)
        line5 = axes.get_graph(lambda x: -1*x-1, color = BLACK)
        line6 = axes.get_graph(lambda x: -1*x+4, color = BLACK)
        line7 = axes.get_graph(lambda x: -1*x+1, color = BLACK)
        
        line8 = axes.get_graph(lambda x: -3*x+5, color = BLACK)
        line9 = axes.get_graph(lambda x: 7*x-1, color = BLACK)
        line10 = axes.get_graph(lambda x: 1.5*x+2, color = BLACK)


        equation = MathTex("A", "x + ","B","y = ","C", color = textColor)
        equation2 = MathTex("By = -Ax + C", color = textColor)
        equation3 = MathTex("y = -\\frac{A}{B}x + \\frac{c}{B}", color = textColor)
        equation4 = MathTex("y = Mx + C'", color = textColor)

        equation.shift(UP*1.9, RIGHT*3)
        equation2.shift(UP*2.9, RIGHT*4.5)
        equation3.shift(UP*2, RIGHT*4.5)
        equation4.shift(UP*3, RIGHT*4.5)

        mEquals = MathTex("M = ", color= textColor)
        mEquals.shift(UP*2.4, RIGHT*4)
        mVal = DecimalNumber(-0.5, num_decimal_places=1).set_color(textColor)
        mVal.add_updater(lambda number: number.next_to(mEquals, RIGHT))
       
        cEquals = MathTex("c = ", color= textColor)
        cEquals.shift(UP*1.8, RIGHT*4)
        cVal = DecimalNumber(3, num_decimal_places=1).set_color(textColor)
        cVal.add_updater(lambda number: number.next_to(cEquals, RIGHT))
    
        mValGroup = VGroup(mEquals, mVal)
        cValGroup = VGroup(cEquals, cVal)

        underline1 = Underline(mobject=equation[0], buff=0.1, color = BLACK)
        underline2 = Underline(mobject=equation[2], buff=0.1, color = BLACK)
        underline3 = Underline(mobject=equation[4], buff=0.1, color = BLACK)
        staggeredUnderline = [Create(underline1), Create(underline2), Create(underline3)]
        underlines = VGroup(underline1, underline2, underline3)        


        # self.add(axes, axes_labels, line1, equation)

        self.wait(2)
        self.play(FadeIn(axes, axes_labels))
        self.play(Create(line1))
        self.wait(1)
        self.play(Write(equation))
        self.wait(1)
        self.play(LaggedStart(*staggeredUnderline, lag_ratio=0.1), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(equation.shift, UP*1.6, RIGHT*1.5), FadeOut(underlines))
        self.wait()
        self.play(FadeIn(equation2))
        self.wait(0.1)
        self.play(FadeIn(equation3))
        self.wait(1)
        self.play(FadeOut(equation), FadeOut(equation2),Transform(equation3, equation4))
        self.wait(3)

        self.play(FadeIn(mValGroup))
        self.wait(0.1)
        self.play(Transform(line1, line2), Count(mVal, -0.5, -5))
        self.wait(0.3)
        self.play(Transform(line1, line3), Count(mVal, -5, 3), rate_func=linear)
        self.wait(0.3)
        self.play(Transform(line1, line4), Count(mVal, 3, -1), rate_func=linear)
        self.wait(0.3)

        self.play(FadeIn(cValGroup))
        self.wait(0.1)
        self.play(Transform(line1, line5), Count(cVal, 3, -1))
        self.wait(0.3)
        self.play(Transform(line1, line6), Count(cVal, -1, 4))
        self.wait(0.3)
        self.play(Transform(line1, line7), Count(cVal, 4, 1))
        self.wait(0.3)

        self.play(Transform(line1, line8), Count(mVal, -1, -3), Count(cVal, 1, 5))
        self.wait(0.3)
        self.play(Transform(line1, line9), Count(mVal, -3, 7), Count(cVal, 5, -1), rate_func=linear)
        self.wait(0.3)
        self.play(Transform(line1, line10), Count(mVal, 7, 1.5), Count(cVal, -1, 2))
        self.wait(0.3)

        self.wait(0.2)
        self.play(FadeOut(axes, axes_labels, line1, mValGroup, cValGroup, equation3))
        self.wait()
        # self.play(Count(number, 0, 100), run_time=4, rate_func=linear)
