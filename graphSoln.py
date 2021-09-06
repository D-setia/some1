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


class GraphSolutionScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.1).shift(LEFT*1.7)
        axes = Axes(
            x_range=[-20*16/9, 50*16/9, 10],
            y_range=[-35, 50, 10],
            y_length=7,
            x_length=7*16/9,
            x_axis_config={"color":BLACK},
            y_axis_config={"color":BLACK}
        )
        axes_labels = axes.get_axis_labels()
        axes_labels.set_color(BLACK)

        constraint1 = axes.get_graph(lambda x: -1/3*x+10, color = BLACK)
        constraint2 = axes.get_graph(lambda x: -4*x+36, color = BLACK)

        constraint1Eq = MathTex("x + 3y = 45", color = textColorNormal).shift(DOWN*1.5, RIGHT*1.5)
        constraint2Eq = MathTex("4x + y = 54", color = textColorNormal).shift(UP*0.3, LEFT*0.2)
        
        rect = Rectangle(
            height= 10,
            width=20,
        )
        rect.set_fill(PINK, opacity=0)
        rect.set_stroke(width=0)
        rect.rotate(np.arctan(-0.275))
        rect.shift(LEFT, DOWN*5.45)

        rect2 = Rectangle(
            height= 9,
            width=20,
        )
        rect2.set_fill(BLUE, opacity=0)
        rect2.set_stroke(width=0)
        rect2.rotate(np.arctan(-3.3))
        rect2.shift(LEFT*6.35, DOWN)

        rect2Duplicate = Rectangle(
            height= 13,
            width=20,
        )
        rect2Duplicate.set_fill(color=GOLD, opacity=0)
        rect2Duplicate.set_stroke(width=0)
        rect2Duplicate.rotate(np.arctan(-3.3))
        rect2Duplicate.shift(RIGHT*5,DOWN*0.5)



        dotA = Dot([-2.67,-0.62,0], color=ORANGE).scale(0.8)
        dotB = Dot([-1.765,-0.62,0], color=ORANGE).scale(0.8)
        dotC = Dot([-1.95,0.01,0], color=RED).scale(0.8)
        dotD = Dot([-2.67,0.21,0], color=ORANGE).scale(0.8)

        edgeDot1 = Dot([-0.74,-4,0], color=ORANGE).scale(0.3)
        edgeDot2 = Dot([-7.1,1.42,0], color=RED).scale(0.3)
        edgeDot3 = Dot([-7.1,-4,0], color=RED).scale(0.3)
        vertices = VGroup(dotA, dotB, dotC, dotD)


        randomPoint = Dot([-3,0.4,0], color = RED_A).scale(1.2)
        cubicBezier = CubicBezier([-3,0.4,0], [-4,-5,0], [0, -1.35606898, 0], [-2.67,-0.62,0], color = BLACK)


        constraint2Dup1 = axes.get_graph(lambda x: -4*x, color = BLACK)
        constraint2Dup1Eq = MathTex("4x + y = ","n", color = textColorNormal).shift(DOWN*2.1, LEFT*4)
        eqAt0 =  MathTex("4*0 + 1*0 = ",  color = textColorNormal).shift(DOWN*2.1, LEFT*4.2)        
        n0 =  MathTex("0 ",  color = textColorNormal).shift(DOWN*2.1, LEFT*2.4)        
        lessThan60 =  MathTex("< 54 ",  color = textColorNormal).shift(DOWN*2.1, LEFT*1.6).add_background_rectangle(color="#fefbea", opacity=0.8)    

        correctHalfPlaneEq =  MathTex("4x + y < 54",  color = textColorNormal).shift(DOWN*1.6, LEFT*4.1)    


        # arcPt1 = Dot([-2,0.4,0], color = BLACK)
        # arcPt2 = Dot([-3.5,-0.05,0], color = BLACK)
        # arcPt3 = Dot([-2.0276397, -1.35606898, 0], color = BLACK)
        # arcPt4 = Dot([-2.67,-0.62,0], color = BLACK)

        # arcVertices = [[-2,0.4,0], [-3.5,-0.05,0], [-2.0276397, -1.35606898, 0], [-2.67,-0.62,0]]
        

        # arcPts = VGroup(arcPt1, arcPt2, arcPt3, arcPt4)

        # arc1 = ArcBetweenPoints(start=arcPt1.get_center(), end=arcPt2.get_center(), angle=PI*0.6, color = BLACK)
        # arc2 = Arc(radius= 1.8, arc_center = [-5.08,-0.9,0], start_angle = 0.5, angle=-1*PI*0.4, color = BLACK)
        # arc3 = Arc(radius= 1.2, arc_center = [-3.2,-1.1,0], start_angle = -2.1, angle=PI*0.6, color = BLACK)
        # arc4 = ArcBetweenPoints(start=arcPt3.get_center(), end=arcPt4.get_center(), angle=PI*0.6, color = BLACK)
        # arcs = VGroup(arc1, arc2, arc3, arc4)


        polyBlue1 = Polygon([-0.74,-4,0],[-1.95,0.01,0], [-7.1,1.42,0], [-7.1,-4,0])
        polyBlue1.set_fill(color=BLUE, opacity=0.7)
        polyBlue1.set_stroke(width=0)
        
        polyPink1 = Polygon([-0.74,-4,0], [-1.95,0.01,0], [-7.1,1.42,0], [-7.1,-4,0])
        polyPink1.set_fill(color=PINK, opacity=0.7)
        polyPink1.set_stroke(width=0)

        commonShadedPink = Polygon([-2.67,-0.62,0], [-1.765,-0.62,0], [-1.95,0.01,0], [-2.67,0.21,0])
        commonShadedPink.set_fill(color = PINK, opacity= 0.7)
        commonShadedPink.set_stroke(width=0)
        
        commonShadedBlue = Polygon([-2.67,-0.62,0], [-1.765,-0.62,0], [-1.95,0.01,0], [-2.67,0.21,0])
        commonShadedBlue.set_fill(color = BLUE, opacity= 0.7)
        commonShadedBlue.set_stroke(width=0)


        objFuncRand = axes.get_graph(lambda x: -3*x + 6, color = BLUE_D)
        objFuncRand1 = axes.get_graph(lambda x: -3*x + 18, color = BLUE_D)
        objFuncOptimal = axes.get_graph(lambda x: -3*x + 29, color = BLUE_D)
        
        objFuncEq1 = MathTex("1.5x + 0.5y = ","6", color = BLACK).scale(0.7).shift(DOWN, LEFT*1.1)
        valV =  MathTex("v", color = BLACK).scale(0.7).shift(DOWN)
        objFuncEq1a = MathTex("1.5x + 0.5y > 6", color = BLACK).scale(0.7).shift(UP*0.5, LEFT*0.2)

        objFuncRect = Rectangle(
            height= 13,
            width=20,
        )
        objFuncRect.set_fill(color=GOLD, opacity=0)
        objFuncRect.set_stroke(width=0)
        objFuncRect.rotate(np.arctan(-2.5))
        objFuncRect.shift(RIGHT*4.5,DOWN*0.5)


        objFunc1 = axes.get_graph(lambda x: -8*x + 2, color = TEAL)
        objFunc1Opt = axes.get_graph(lambda x: -8*x + 72, color = TEAL)
        
        objFunc2 = axes.get_graph(lambda x: -1*x + 6, color = MAROON)
        objFunc2Opt = axes.get_graph(lambda x: -1*x + 14.9, color = MAROON)
        
        objFunc3 = axes.get_graph(lambda x: 5*x - 80, color = GOLD)
        objFunc3Opt = axes.get_graph(lambda x: 5*x + 10, color = GOLD)
        
        objFunc4 = axes.get_graph(lambda x: -5*x + 100, color = GREEN)
        objFunc4Opt = axes.get_graph(lambda x: -5*x , color = GREEN)



        # constraint1Copy = axes.get_graph(lambda x: -1/3*x+10, color = BLACK)
        # constraint2Copy = axes.get_graph(lambda x: -3/2*x+30, color = BLACK)

        # constrnt2Parallel = axes.get_graph(lambda x: -3/2*x, color = BLACK)
        # constrnt1P2d = axes.get_graph(lambda x: -3*x-30, color = BLACK)
        # constrnt1P3d = axes.get_graph(lambda x: -3*x-60, color = BLACK)
        # constrnt1P4d = axes.get_graph(lambda x: -3*x-90, color = BLACK)
        # constrnt1P1u = axes.get_graph(lambda x: -3*x+60, color = BLACK)
        # constrnt1P2u = axes.get_graph(lambda x: -3*x+90, color = BLACK)
        # constrnt1P3u = axes.get_graph(lambda x: -3*x+120, color = BLACK)
        # constrnt1P4u = axes.get_graph(lambda x: -3*x+150, color = BLACK)

        # # constrnt1Group = VGroup(constrnt1P4u, constrnt1P3u, constrnt1P2u, constrnt1P1u, constrnt1P4d, constrnt1P3d, constrnt1P2d)
        # line3 = axes.get_graph(lambda x: -2/3*x+20)
        # # area = axes.get_area(line1, color=BLUE, opacity=0.1)

        # # self.camera.frame.scale(0.8).shift(UP, RIGHT)

        # self.add(rect, rect2, axes, axes_labels, constraint2, arcPts, arcs, randomPoint)
        # self.add(rect, rect2, axes, axes_labels, constraint2, randomPoint)

        
        # self.wait(2)
        # print(randomPoint.get_center())


        # self.add(rect2, rect, rect2Duplicate, objFuncRect, rect2Duplicate, axes, constraint1, constraint2, dotB, edgeDot1)
        
        
        self.add(rect, rect2, rect2Duplicate)

        self.wait(0.2)
        staggeredStart= [FadeIn(axes), FadeIn(axes_labels)]
        self.play(LaggedStart(*staggeredStart, lag_ratio=0.1))
        self.wait(0.1)
        self.play(Create(constraint2))
        self.wait(0.1)
        self.play(Write(constraint2Eq))
        self.wait(1.5)
        
        self.play(ApplyMethod(rect2Duplicate.set_opacity, 0.7), run_time = 0.5)
        self.wait(0.2)

        self.play(ApplyMethod(rect2Duplicate.set_opacity, 0), ApplyMethod(rect2.set_opacity, 0.7), run_time = 0.5)
        self.wait(0.2)
        
        self.play(ApplyMethod(rect2.set_opacity, 0),  run_time = 0.5)
        self.wait(3.2)

        self.play(FadeIn(randomPoint))
        self.wait(0.1)
        self.play(MoveAlongPath(randomPoint, cubicBezier), run_time = 2.5, rate = linear)
        self.wait(0.5)

        self.play(Create(constraint2Dup1))
        self.wait(13.5)
        self.play(Write(constraint2Dup1Eq))
        self.wait(3)
        self.play(Transform(constraint2Dup1Eq[0], eqAt0), ApplyMethod(constraint2Dup1Eq[1].shift,RIGHT*0.7))#, Transform(rect2, polyPink1))
        self.wait(6)
        self.play(Transform(constraint2Dup1Eq[1], n0))
        self.wait()
        self.play(FadeIn(lessThan60))
        self.wait(3)

        self.play(ApplyMethod(rect2.set_opacity, 0.7), FadeOut(constraint2Dup1Eq, constraint2Dup1, lessThan60, randomPoint))
        self.wait(0.1)
        self.play(FadeIn(correctHalfPlaneEq))
        self.wait()
        self.play(FadeOut(correctHalfPlaneEq))
        self.wait(0.6)

        self.play(Create(constraint1), (ApplyMethod(constraint2Eq.shift, UP, LEFT*0.3)), Write(constraint1Eq))
        self.wait(0.1)
        self.play(ApplyMethod(rect.set_opacity, 0.7))
        self.wait(6)

        self.play(ApplyMethod(rect2.set_opacity, 1))
        self.wait(0.1)
        self.play(ApplyMethod(rect2.set_opacity, 0.7))
        self.play(ApplyMethod(rect.set_opacity, 1))
        self.wait(0.1)
        self.play(ApplyMethod(rect.set_opacity, 0.7))
        self.wait()
        self.play(Transform(rect, polyBlue1), Transform(rect2, polyPink1))
        self.wait(8)
        self.play(Transform(rect, commonShadedBlue), Transform(rect2, commonShadedPink), self.camera.frame.animate.scale(0.4).shift(LEFT), FadeOut(constraint2Eq, constraint1Eq))
        self.wait(13.5 )

        feasibleArea = Text("Feasible Area", color = BLACK).scale(0.5).shift(LEFT, UP)
        self.play(Write(feasibleArea))
        self.wait(2)
        self.play(FadeOut(feasibleArea))
        self.wait(8)

        self.play(Create(objFuncRand), Write(objFuncEq1))
        self.wait(12)
        self.play(ApplyMethod(objFuncRect.set_opacity, 0.7))
        self.play(Write(objFuncEq1a))
        self.wait(7)

        self.play(ApplyMethod(objFuncRect.set_opacity, 0), FadeOut(objFuncEq1a))
        self.wait()
        self.play(objFuncRand.animate.become(objFuncRand1), Transform(objFuncEq1[1], valV))
        self.wait(13)

        # #TODO: add portion of line inside feasible area AFTER EFFECTS?

        objFuncRect.shift(RIGHT*0.4)
        self.play(ApplyMethod(objFuncRect.set_opacity, 0.7))
        self.wait(2)
        self.play(ApplyMethod(objFuncRect.set_opacity, 0))
        self.wait(3)

        self.play(objFuncRand.animate.become(objFuncOptimal), run_time = 3)
        self.play(FadeIn(dotC))
        self.wait()

        self.play(FadeOut(objFuncEq1, valV, dotC))
        self.wait(0.1)

        self.play(objFunc1.animate.become(objFunc1Opt))
        self.play(objFunc3.animate.become(objFunc3Opt))
        self.play(objFunc2.animate.become(objFunc2Opt))
        self.play(objFunc4.animate.become(objFunc4Opt))
        self.wait(3)
        self.play(FadeOut(objFunc1, objFunc2, objFunc3, objFunc4))
        self.wait(0.1)

        self.play(constraint1.animate.set_color(GOLD), constraint2.animate.set_color(GOLD))
        self.wait(2.5)
        dotA.set_color(GOLD)
        dotB.set_color(GOLD)
        dotC.set_color(GOLD)
        dotD.set_color(GOLD)
        self.play(FadeIn(vertices), constraint1.animate.set_color(BLACK), constraint2.animate.set_color(BLACK))
        self.wait(9)
        self.play(dotA.animate.set_color(BLACK), dotB.animate.set_color(BLACK), dotD.animate.set_color(BLACK))
        self.wait(5)  


        objFuncOpp = axes.get_graph(lambda x: -3*x , color = BLUE_D)
        self.play(objFuncRand.animate.become(objFuncOpp), run_time = 2)

        self.wait(2.5)
        self.play(FadeOut(axes, constraint2, constraint1, objFuncRand, rect, rect2, vertices))
        self.wait()
