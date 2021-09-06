from manim import *


config.background_color = "#fefbea"
# config.background_color = "#04f404" bb70c7
# config.background_opacity = 0
config.frame_rate = 30


textColor = "#861657"
lineColor = "#0c0c0c"
axesColor = BLACK


class HalfPlanesScene(Scene):
    def construct(self):

        axes = Axes(
            x_length= 15,
            y_length= 15*9/16,
            x_range=[-8*16/9, 8*16/9, 1],
            y_range=[-8, 8, 1],
            axis_config={"color":axesColor},
            tips= False
        )

        axes_labels = axes.get_axis_labels()
        axes_labels.set_color(BLACK)

        # constraint1 = axes.get_graph(lambda x: -3*x+3, color = BLACK)
        constraint2 = axes.get_graph(lambda x: -3/2*x+3, color = lineColor)
        duplicate = axes.get_graph(lambda x: -3/2*x+3, color = lineColor)

        parallelLine1 = axes.get_graph(lambda x: -3/2*x+9, color = lineColor)
        parallelLine2 = axes.get_graph(lambda x: -3/2*x+12, color = lineColor)
        parallelLine3 = axes.get_graph(lambda x: -3/2*x+18, color = lineColor)
        parallelLine4 = axes.get_graph(lambda x: -3/2*x-5, color = lineColor)
        parallelLine5 = axes.get_graph(lambda x: -3/2*x-9, color = lineColor)
        parallelLine6 = axes.get_graph(lambda x: -3/2*x-15, color = lineColor)

        copyColor = BLUE_E
        eqOriginal = MathTex("3x + 2y = ","6", color = lineColor).scale(0.75).shift(DOWN*0.5, RIGHT*1.55)
        eq1 = MathTex("3x + 2y = ","18", color = textColor).scale(0.75).shift(UP, RIGHT*2.25)
        eq1Copy = MathTex("y = ","-\\frac{3}{2}","x + 9", color = copyColor).scale(0.75).shift(UP*1.75, RIGHT*1.75)
        frameboxSlope1 = SurroundingRectangle(eq1Copy[1], buff = .1, color = "#ff2e00")
        eq2 = MathTex("3x + 2y = ","24", color = textColor).scale(0.75).shift(UP*2, RIGHT*3.5)
        eq2Copy = MathTex("y = ","-\\frac{3}{2}","x + 12", color = copyColor).scale(0.75).shift(UP*2.75, RIGHT*3)
        frameboxSlope2 = SurroundingRectangle(eq2Copy[1], buff = .1, color = "#ff2e00")
        eq3 = MathTex("3x + 2y = ","36", color = textColor).scale(0.75).shift(UP*2.7, RIGHT*5.8)
        eq3Copy = MathTex("y = ","-\\frac{3}{2}","x + 18", color = copyColor).scale(0.75).shift(UP*3.45, RIGHT*5.8)
        frameboxSlope3 = SurroundingRectangle(eq3Copy[1], buff = .1, color = "#ff2e00")
        eq4 = MathTex("3x + 2y = ","-10", color = textColor).scale(0.75).shift(UP*0.75, LEFT)
        eq4Copy = MathTex("y = ","-\\frac{3}{2}","x-5", color = copyColor).scale(0.75).shift(UP*1.5, LEFT)
        frameboxSlope4 = SurroundingRectangle(eq4Copy[1], buff = .1, color = "#ff2e00")
        eq5 = MathTex("3x + 2y = ","-18", color = textColor).scale(0.75).shift(DOWN*0.75, LEFT*3.1)
        eq5Copy = MathTex("y = ","-\\frac{3}{2}","x - 9", color = copyColor).scale(0.75).shift(LEFT*3.1).add_background_rectangle(color = "#fefbea", opacity=0.8)
        frameboxSlope5 = SurroundingRectangle(eq5Copy[2], buff = .1, color = "#ff2e00")
        eq6 = MathTex("3x + 2y = ","-30", color = textColor).scale(0.75).shift(DOWN*2, LEFT*4.5)
        eq6Copy = MathTex("y = ","-\\frac{3}{2}","x - 15", color = copyColor).scale(0.75).shift(DOWN*2.75, LEFT*4.5)
        frameboxSlope6 = SurroundingRectangle(eq6Copy[1], buff = .1, color = "#ff2e00")

        frameboxSlopes = VGroup(frameboxSlope1, frameboxSlope2, frameboxSlope3, frameboxSlope4, frameboxSlope5, frameboxSlope6)

        framebox1 = SurroundingRectangle(eq1[1], buff = .1, color = "#6ab547")
        framebox2 = SurroundingRectangle(eq2[1], buff = .1, color = "#6ab547")
        framebox3 = SurroundingRectangle(eq3[1], buff = .1, color = "#6ab547")
        framebox4 = SurroundingRectangle(eq4[1], buff = .1, color = "#ff2e00")
        framebox5 = SurroundingRectangle(eq5[1], buff = .1, color = "#ff2e00")
        framebox6 = SurroundingRectangle(eq6[1], buff = .1, color = "#ff2e00")

        equations = VGroup(eq1, eq2 , eq3, eq4, eq5, eq6)
        frameboxes = VGroup(framebox1, framebox2, framebox3, framebox4, framebox5, framebox6)

        eqGroup1 = VGroup(eq1, eq4)
        eqGroup2 = VGroup(eq2, eq5)
        eqGroup3 = VGroup(eq3, eq6)
        staggeredEq = [FadeIn(eqGroup1), FadeIn(eqGroup2), FadeIn(eqGroup3)]

        staggeredFrameboxGreaterThan = [Create(framebox1), Create(framebox2), Create(framebox3)]
        staggeredFrameboxLessThan = [Create(framebox4), Create(framebox5), Create(framebox6)]

        parallelLineGroup = VGroup(parallelLine1, parallelLine2, parallelLine3, parallelLine4, parallelLine5, parallelLine6)

        halfPlane = Rectangle(
            height= 10,
            width=20,
        )
        halfPlane.set_fill(BLUE, opacity=0)
        halfPlane.set_stroke(width=0)
        halfPlane.rotate(np.arctan(-1.5))
        halfPlane.shift(LEFT*4.95)    
        
        halfPlane2 = Rectangle(
            height= 10,
            width=20,
        )
        halfPlane2.set_fill(PINK, opacity=0)
        halfPlane2.set_stroke(width=0)
        halfPlane2.rotate(np.arctan(-1.5))
        halfPlane2.shift(RIGHT*7.05)    

        halfPlaneEq = MathTex("3x + 2y < 6", color = lineColor)
        halfPlaneEq.shift(DOWN*2, LEFT*3)
        halfPlane2Eq = MathTex("3x + 2y > 6", color = lineColor)
        halfPlane2Eq.shift(UP*2, RIGHT*4)

        underline1 = Underline(mobject=halfPlaneEq, buff=0.1)
        underline2 = Underline(mobject=halfPlane2Eq, buff=0.1)
        staggeredUnderline = [Create(underline1), Create(underline2)]



        self.add(halfPlane, halfPlane2)
        self.wait(1)

        self.play(FadeIn(axes, axes_labels))
        self.wait(1)

        self.play(Create(constraint2), Create(duplicate))
        # self.wait()

        self.play(FadeIn(eqOriginal))
        self.wait()

        self.play(ApplyMethod(constraint2.set_color, GOLD_B), Transform(duplicate, parallelLineGroup))
        self.wait()

        self.play(LaggedStart(*staggeredEq, run_time=1.5, lag_ratio=0.1))
        self.wait(2)
        self.play(FadeIn(eq4Copy, eq1Copy, eq2Copy, eq3Copy, eq5Copy, eq6Copy))
        self.wait(4)
        self.play(Create(frameboxSlope1), Create(frameboxSlope2), Create(frameboxSlope3), Create(frameboxSlope4), Create(frameboxSlope5), Create(frameboxSlope6))
        self.wait(1.5)
        self.play(FadeOut(eq4Copy, eq1Copy, eq2Copy, eq3Copy, eq5Copy, eq6Copy, frameboxSlopes))
        self.wait(2)
        
        self.play(LaggedStart(*staggeredFrameboxLessThan), run_time = 0.8)
        self.wait(2.3)
        self.play(LaggedStart(*staggeredFrameboxGreaterThan), run_time = 0.8)
        self.wait(2)

        self.play(ApplyMethod(constraint2.set_color, lineColor), FadeOut(equations, duplicate, frameboxes))
        self.wait(2)
        self.play(ApplyMethod(eqOriginal.scale, 1/0.75*0.9))
        self.wait(2)

        self.play(ApplyMethod(halfPlane.set_opacity, 0.7))
        self.wait(0.1)
        self.play(ApplyMethod(halfPlane2.set_opacity, 0.7))
        self.wait(2)

        self.play(FadeIn(halfPlaneEq))
        self.wait(2)
        self.play(FadeIn(halfPlane2Eq))
        self.wait(2)

        self.play(LaggedStart(*staggeredUnderline, run_time=1.5, lag_ratio=0.1))
        self.wait()

        self.play(FadeOut(halfPlane, halfPlane2, axes_labels, axes, halfPlaneEq, halfPlane2Eq, underline2, underline1, eqOriginal, constraint2))
        
        self.wait(2)
      
