from manim import *
import simplexTables


config.background_color = "#fefbea"
# config.background_color = "#04f404" #GreenScreen
# purple bb70c7
# config.background_opacity = 0
# config.frame_rate = 30


textColorNormal = "#0c0c0c"
textColorPositive = "#43b929"
textColorNegative = "#ff2e00"
lineColor = "#0c0c0c"
axesColor = BLACK
vertexColor = "#2d2a32"
selectedVertexColor = "#279af1"
dodgerBlue = "#1098f7"



class WelcomeScene(Scene):
    def construct(self):

        bgRect = Rectangle(height=9, width=16, color=BLACK).set_opacity(1)
        welcome = Text("Welcome", font="Champignon").scale(5).shift(UP)
        title = Text("A SIMPLE SIMPLEX EXPLANATION").scale(0.8).shift(DOWN*1.2)

        step1 = Text("Step1", font="Champignon", weight= BOLD).scale(2).shift(UP*2.6, LEFT*5.5)
        colon = Text(":", weight= BOLD).scale(1.2).next_to(step1, RIGHT)
        step1Contents1 = Text("Convert all the RHSs to ", font="Champignon").scale(1.4).next_to(step1, RIGHT*3).shift(UP*0.2)
        # step1Contents2 = Text("non negative numbers", font="Champignon").scale(1.4).next_to(step1Contents1, DOWN*0.9).shift(LEFT*1.6)


        self.add(bgRect)#, step1Group)# welcome, title)
        self.wait()
        self.play(Write(welcome), run_time=1.8)
        self.wait()
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(welcome, title))
        self.wait()
        self.play(Write(step1), run_time=0.5)
        self.play(Write(colon), run_time=0.1)
        self.wait()
        self.play(Write(step1Contents1))
        self.wait(3)






class Step1(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.1).shift(LEFT*1.7)

        step1 = Text("Step1:", color = textColorNormal, weight= BOLD).shift(UP*3, LEFT*5.5)
        step1Contents1 = Text("Convert all RHSs to non-negative", color = textColorNormal).scale(0.7).next_to(step1, RIGHT)
        step1Contents2 = Text("numbers", color = textColorNormal).scale(0.7).next_to(step1Contents1, DOWN).shift(LEFT*2.8)

        step1Eq = MathTex("(","Ax_1 + Bx_2 ",")","\\leq", "-12",  color = textColorNormal).scale(1.3)
        step1EqInit = VGroup(step1Eq[1], step1Eq[3], step1Eq[4])
        bracketsEq1 = VGroup(step1Eq[0], step1Eq[2])
        geq = MathTex("\\geq", color = textColorNormal).shift(RIGHT*1.2).scale(1.3)
        minus1a = MathTex("-1*", color = textColorNormal).shift(LEFT*3.5, UP*0.07).scale(1.3)
        minus1b = MathTex("*-1", color = textColorNormal).shift(RIGHT*3.7, UP*0.07).scale(1.3)

        step1EqMod = MathTex("-Ax_1 - Bx_2 ","\\geq", "12",  color = textColorNormal).scale(1.3).shift(DOWN)
        

        # self.add(step1, step1Contents1, step1Contents2, step1EqInit, geq, minus1a, minus1b, bracketsEq1, step1EqMod)

        self.wait(2)
        self.play(FadeIn(step1), run_time=0.4)
        self.wait()
        self.play(FadeIn(step1Contents1, step1Contents2), run_time=0.8)
        self.wait()
        self.play(FadeIn(step1EqInit))
        self.wait()
        self.play(FadeIn(bracketsEq1, minus1b, minus1a))
        self.wait(2)
        self.play(Transform(step1Eq[3],geq))
        self.wait(2)
        self.play(FadeIn(step1EqMod))
        self.wait(2)
        self.play(FadeOut(step1, step1Contents1, step1Contents2, step1Eq, minus1a, minus1b, bracketsEq1, step1EqMod))
        self.wait(3)
    




class UnresVarsScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()

        var1Geq0 = MathTex("x_1 \\geq 0", color = textColorNormal).scale(1.3).shift(UP*2)
        var2Geq0 = MathTex("x_2 \\geq 0", color = textColorNormal).scale(1.3).shift(UP*1)
        var3Geq0 = MathTex("x_3 \\geq 0", color = textColorNormal).scale(1.3)
        dot1 = MathTex(".", color = textColorNormal).scale(1.3).shift(DOWN)
        dot2 = MathTex(".", color = textColorNormal).scale(1.3).shift(DOWN*1.2)
        dot3 = MathTex(".", color = textColorNormal).scale(1.3).shift(DOWN*1.4)
        dots = VGroup(dot1, dot2, dot3)

        x_i = MathTex("x_i", color = textColorNormal).shift(LEFT*5.8, DOWN)
        unres = Tex("No Constraints", color = textColorNormal).scale(0.8).next_to(x_i, RIGHT).shift(RIGHT*0.4, UP*0.04)
        varN = VGroup(x_i, unres)

        # self.add(var1Geq0, var2Geq0, var3Geq0, dot1, dot2, dot3, varN)

        staggeredXi = [FadeIn(var1Geq0), FadeIn(var2Geq0), FadeIn(var3Geq0), FadeIn(dots)]

        self.wait(2)
        self.play(LaggedStart(*staggeredXi, lag_ratio=0.2), run_time=3)
        self.wait(3)
        self.play(FadeIn(varN))
        self.wait(3)
        self.play(FadeOut(var1Geq0, var2Geq0, var3Geq0, dots, varN))
        self.wait(3)





class Step2(Scene):
    def construct(self):

        step2 = Text("Step2:", color = textColorNormal, weight= BOLD).shift(UP*2.7, LEFT*5.2)
        step2Contents = Text("Convert all inequalities to eqations", color = textColorNormal).scale(0.7).next_to(step2, RIGHT)

        lessThanEq = MathTex("Ax_1 + Bx_2 ","\\leq", "C",  color = textColorNormal).scale(1.3).shift(UP*0.5)
        equals1 = MathTex("=",  color = textColorNormal).scale(1.3).shift(UP*0.5, RIGHT*1.2)

        greaterThanEq = MathTex("Ax_1 + Bx_2 ","\\geq", "C",  color = textColorNormal).scale(1.3).shift(DOWN*1.5)
        equals2 = MathTex("=",  color = textColorNormal).scale(1.3).shift(DOWN*1.5, RIGHT*1.2)


        slackVar = MathTex("+","s_1",  color = textColorNormal).scale(1.3).shift(UP*0.5)
        slackVarConstraint = MathTex("s_1 \\geq 0",  color = textColorNormal).scale(1.3).shift(UP*0.5, RIGHT*4.5)

        surplusVar = MathTex("-","S_1",  color = textColorNormal).scale(1.3).shift(DOWN*1.5)
        surplusVarConstraint = MathTex("S_1 \\geq 0",  color = textColorNormal).scale(1.3).shift(DOWN*1.5, RIGHT*4.5)

        artificialVar = MathTex("+a_1",  color = textColorNormal).scale(1.3).shift(DOWN*1.5)
        artificialVarConstraint = MathTex("a_1 \\geq 0",  color = textColorNormal).scale(1.3).shift(DOWN*2.5, RIGHT*4.5)
        
        # lessThanEq[0].shift(LEFT*1.3)
        # greaterThanEq[0].shift(LEFT*1.3)
        # greaterThanEq[0].shift(LEFT*1.3)
        # surplusVar.shift(LEFT*1.3)

        equation1 = VGroup(lessThanEq, slackVar, equals1)
        equation2 = VGroup(greaterThanEq, surplusVar, artificialVar, equals2)

        # equation1.shift(UP*0.9, RIGHT*1.5)
        # equation2.shift(UP*1.9, RIGHT*1.5)
        

        variables = MathTex("x_1,x_2,s_1,S_1,a_1", color = textColorNormal).scale(1.3).shift(DOWN*3, LEFT*3)
        braceVars = Brace(variables, UP, color = "#f50000")
        noOfVars = MathTex("5", color = "#f50000").scale(1.7).next_to(braceVars, UP).shift(UP*0.37)

        geq = MathTex("\\geq", color = textColorNormal).scale(1.7).next_to(noOfVars, RIGHT*4.5)

        # self.add(step2, step2Contents, lessThanEq, equals1, greaterThanEq, equals2, slackVar, surplusVar, artificialVar , variables, braceVars, braceEqs, noOfEqs, noOfVars, geq)#, slackVarConstraint, surplusVarConstraint, artificialVarConstraint)

        self.wait(2)
        self.play(FadeIn(step2))
        self.play(FadeIn(step2Contents))
        self.wait(2)
        self.play(FadeIn(lessThanEq))
        self.play(FadeIn(greaterThanEq))
        self.wait(2)
        
        self.play(ApplyMethod(lessThanEq[0].shift, LEFT*1.5), FadeIn(slackVar), FadeIn(slackVarConstraint))
        self.wait()
        self.play(ApplyMethod(slackVar[0].scale, 2/1.3))
        self.wait()
        self.play(ApplyMethod(lessThanEq[1].scale, 1.6/1.3))
        self.wait()
        self.play(Transform(lessThanEq[1], equals1), ApplyMethod(slackVar[0].scale, 1.3/2))
        self.wait()
        
        self.play(ApplyMethod(greaterThanEq[0].shift, LEFT*1.5), FadeIn(surplusVar), FadeIn(surplusVarConstraint))
        self.wait()
        self.play(ApplyMethod(surplusVar[0].scale, 2/1.3))
        self.wait()
        self.play(ApplyMethod(greaterThanEq[1].scale, 1.6/1.3))
        self.wait()
        self.play(Transform(greaterThanEq[1], equals2),ApplyMethod(surplusVar[0].scale, 1.3/2))
        self.wait(2)
        self.play(ApplyMethod(greaterThanEq[0].shift, LEFT*1.3), 
        ApplyMethod(surplusVar.shift, LEFT*1.3), FadeIn(artificialVar), FadeIn(artificialVarConstraint))
        self.wait(3)

        self.play(FadeOut(surplusVarConstraint, slackVarConstraint, artificialVarConstraint), 
        ApplyMethod(equation1.shift, UP*0.9, RIGHT*1.5), ApplyMethod(equation2.shift, UP*1.9, RIGHT*1.5), Write(variables))
        self.wait()

        braceEqs = Brace(equation2, DOWN, color = "#7e3a7e")
        noOfEqs = MathTex("2", color = "#7e3a7e").scale(1.7).next_to(braceEqs, DOWN).shift(DOWN*0.37)

        laggedVarStats = [FadeIn(braceVars), Write(noOfVars)]
        laggedEqStats = [FadeIn(braceEqs), Write(noOfEqs)]
        self.play(LaggedStart(*laggedVarStats, lag_ratio=0.2))
        self.play(LaggedStart(*laggedEqStats, lag_ratio=0.2))
        self.wait()
        self.play(FadeIn(geq))
        self.wait(2)
        self.play(FadeOut(step2, step2Contents, equation1, equation2, braceEqs, braceVars, noOfEqs, noOfVars, geq, variables))
        self.wait()





class Step1Intuition(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.9)#.shift(LEFT*1.7)

        axes = Axes(
            x_length= 14,
            y_length= 14*9/16,
            x_range=[-1*16/9, 10*16/9, 1],
            y_range=[-1, 10, 1],
            axis_config={"color":axesColor},
            tips= False
        )


        constraint1 = axes.get_graph(lambda x: x+2, color = lineColor)
        constraint2 = axes.get_graph(lambda x: x/3+3, color = lineColor)
        constraint3 = axes.get_graph(lambda x: -3*x+18, color = lineColor)
        constraint4 = axes.get_graph(lambda x: x-3, color = lineColor)
        constraints = VGroup(constraint1, constraint2, constraint3,constraint4)


        graph = VGroup(axes, constraints)
        graph.shift(UP*2.45, RIGHT*1.52).scale(4/5-0.01)
        

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
        feasibleArea.set_stroke(width=2, color = lineColor)
        feasibleArea.set_fill(PURPLE_A, opacity = 1)


        plottedGraph = VGroup(graph, feasibleArea, vertices)
        plottedGraph.shift(LEFT)

        # self.camera.frame.scale(0.7).shift(DOWN, LEFT*4)
        # dot1.set_color(selectedVertexColor)

        
        
        step1Eq1 = MathTex("Ax_1+Bx_2 \\geq -12", color=textColorNormal).scale(0.8).shift(LEFT*7, UP*0.7)
        step1Eq2 = MathTex("-Ax_1-Bx_2 \\leq 12", color=textColorNormal).scale(0.8).next_to(step1Eq1, DOWN)
        step1Eq2Dupl = MathTex("-Ax_1-Bx_2 \\leq 12", color=textColorNormal).scale(0.8).next_to(step1Eq1, DOWN)
        step1Eq3 = MathTex("-A","x_1","-B","x_2"," +"," s_1 = 12", color=textColorNormal).scale(0.8).shift(LEFT*6.2, DOWN*2)


        # constraints.set_opacity(0)
        # plottedGraph.shift(UP*1.5, RIGHT*2.5)

        x1_0 = MathTex("x_1=0", color=textColorNormal).scale(0.7).shift(LEFT*2.2, DOWN*0.5)
        x2_0 = MathTex("x_2=0", color=textColorNormal).scale(0.7).next_to(x1_0, DOWN*0.7)

        allVarsGEQ0 = MathTex("x_i",",","s_i",",","S_i",",","a_i ","\\geq 0", color=textColorNormal).scale(0.8).shift(LEFT*1.5, DOWN*2.5)

        times0_1 = MathTex("*0", color=textColorNormal).scale(0.8).shift(LEFT*7.4, DOWN*2)
        times0_2 = MathTex("*0", color=textColorNormal).scale(0.8).shift(LEFT*6.2, DOWN*2)



        # self.add(feasibleArea, axes, constraints, vertices, step1Eq1, step1Eq2, x1_0, x2_0, allVarsGEQ0, step1Eq3, times0_1, times0_2)

        

        self.wait()
        self.play(FadeIn(axes), run_time=0.5)
        self.play(Create(constraint1), Create(constraint2), Create(constraint3), Create(constraint4),  run_time=0.5)
        self.play(FadeIn(feasibleArea, vertices))
        self.wait()

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
        dot2.set_color(vertexColor)

        self.wait()
        self.play( ApplyMethod(dot1.set_color, selectedVertexColor), 
        ApplyMethod(constraints.set_opacity, 0), self.camera.frame.animate.scale(0.7).shift(DOWN, LEFT*4))
        self.wait()

        self.play(FadeIn(step1Eq1))
        self.play(FadeIn(step1Eq2))
        self.wait(2)
        self.play(ApplyMethod(plottedGraph.shift, UP*1.5, RIGHT*2.5))
        self.wait()
        self.play(FadeIn(x1_0), run_time=0.5)
        self.play(FadeIn(x2_0), run_time=0.5)
        self.wait()
        self.play(FadeIn(allVarsGEQ0))
        self.wait()
        self.play(Transform(step1Eq2Dupl, step1Eq3))
        self.add(step1Eq3)
        step1Eq2Dupl.set_opacity(0)
        self.wait(2)
        self.play(Transform(step1Eq3[1], times0_1), run_time=0.5)
        self.play(Transform(step1Eq3[3], times0_2), run_time=0.5)
        self.wait(2)
        self.play(ApplyMethod(step1Eq3[0:5].set_opacity, 0), ApplyMethod(allVarsGEQ0[3:7].set_opacity, 0), 
        ApplyMethod(allVarsGEQ0[0:2].set_opacity, 0), ApplyMethod(step1Eq3[5].set_color, textColorNegative), 
        ApplyMethod(allVarsGEQ0[2].set_color, textColorNegative), ApplyMethod(allVarsGEQ0[7].set_color, textColorNegative))
        self.play(ApplyMethod(allVarsGEQ0[2].shift, RIGHT))
        self.wait(2)
        self.play(FadeOut(step1Eq1, step1Eq2, step1Eq3, step1Eq2Dupl, allVarsGEQ0))
        self.wait(2)





class ArtificialVariablesIntuition(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.9)#.shift(LEFT*1.7)

        axes = Axes(
            x_length= 14,
            y_length= 14*9/16,
            x_range=[-1*16/9, 10*16/9, 1],
            y_range=[-1, 10, 1],
            axis_config={"color":axesColor},
            tips= False
        )


        constraint1 = axes.get_graph(lambda x: x+2, color = lineColor)
        constraint2 = axes.get_graph(lambda x: x/3+3, color = lineColor)
        constraint3 = axes.get_graph(lambda x: -3*x+18, color = lineColor)
        constraint4 = axes.get_graph(lambda x: x-3, color = lineColor)
        constraints = VGroup(constraint1, constraint2, constraint3,constraint4)


        graph = VGroup(axes, constraints)
        graph.shift(UP*2.45, RIGHT*1.52).scale(4/5-0.01)
        

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
        feasibleArea.set_stroke(width=2, color = lineColor)
        feasibleArea.set_fill(PURPLE_A, opacity = 1)


        plottedGraph = VGroup(graph, feasibleArea, vertices)
        plottedGraph.shift(LEFT)

        self.camera.frame.scale(0.7).shift(DOWN, LEFT*4)
        dot1.set_color(selectedVertexColor)

        
        
        greaterThanIneq1= MathTex("Ax_1+Bx_2 \\geq C", color=textColorNormal).scale(0.8).shift(LEFT*6)
        greaterThanEq1 = MathTex("A","x_1","+B","x_2"," -","S_1","+","a_1"," = ","C", color=textColorNormal).scale(0.8).shift(LEFT*6.2, DOWN)
        greaterThanEq1Dupl = MathTex("A","x_1","+B","x_2"," -","S_1","+","a_1"," = ","C", color=textColorNormal).scale(0.8).shift(LEFT*6.2, DOWN)
        minusC = MathTex("-C", color=textColorNormal).scale(0.8).shift(LEFT*4, DOWN*0.98)
        C = MathTex("C", color=textColorNormal).scale(0.8).shift(LEFT*4.1, DOWN*0.98)

        willBeZeroAtBeginning = Tex("Will be 0 at start", color=textColorNormal).scale(0.56).shift(LEFT*4.3, DOWN*1.7)
        arrow = CurvedArrow([-5.1, -2, 0], [-6.1, -1, 0], color = textColorNormal, angle= -TAU/4).scale(0.4)


        constraints.set_opacity(0)
        plottedGraph.shift(UP*1.5, RIGHT*2.5)

        x1_0 = MathTex("x_1=0", color=textColorNormal).scale(0.7).shift(LEFT*2.2, DOWN*0.5)
        x2_0 = MathTex("x_2=0", color=textColorNormal).scale(0.7).next_to(x1_0, DOWN*0.7)

        allVarsGEQ0 = MathTex("x_i",",","s_i",",","S_i",",","a_i ","\\geq 0", color=textColorNormal).scale(0.8).shift(LEFT*1.3, DOWN*2.5)
        allVarsGEQ0Dupl = MathTex("x_i",",","s_i",",","S_i",",","a_i ","\\geq 0", color=textColorNormal).scale(0.8).shift(LEFT*1.3, DOWN*2.5)
        allVarsGEQ0[4].set_color(textColorNegative).scale(9/8)
        allVarsGEQ0[7].set_color(textColorNegative).scale(9/8)

        times0_1 = MathTex("*0", color=textColorNormal).scale(0.8).shift(LEFT*8, DOWN)
        times0_2 = MathTex("*0", color=textColorNormal).scale(0.8).shift(LEFT*6.75, DOWN)

        objFuncMax = MathTex("Z = Px_1+qx_2", "-Ma_1", color = textColorNormal).scale(0.8).shift(LEFT*4.6, DOWN*2.05)
        objFuncMin = MathTex("Z = Px_1+qx_2", "+Ma_1", color = textColorNormal).scale(0.8).shift(LEFT*4.6, DOWN*2.75)
        maximize = Tex("Maximize:", color = textColorNormal).scale(0.8).shift(LEFT*7.7, DOWN*2)
        minimize = Tex("Minimize:", color = textColorNormal).scale(0.8).shift(LEFT*7.7, DOWN*2.7)

        m = MathTex("M", color = textColorNormal).scale(0.8).shift(LEFT*6.2, DOWN*2)
        arrowM = Arrow([-6.2,-2, 0], [-5.3,-2, 0], color = textColorNormal)
        large = MathTex("Large", color = textColorNormal).scale(0.8).shift(LEFT*5, DOWN*2.05)
        mIsLarge = VGroup(m, arrowM, large).shift(DOWN*0.05, RIGHT*4.7)

        



        # self.add(feasibleArea, axes, constraints, vertices, x1_0, x2_0, greaterThanIneq1, greaterThanEq1, 
        # allVarsGEQ0, minusC, times0_1, times0_2, C, willBeZeroAtBeginning, arrow, mIsLarge, objFunc1, objFunc2, maximize, minimize)
        
        
        self.add(feasibleArea, axes,  constraints, vertices, x1_0, x2_0)

        self.wait()
        self.play(FadeIn(greaterThanIneq1))
        self.wait()
        self.play(FadeIn(greaterThanEq1))
        self.wait(2)
        self.play(Transform(greaterThanEq1[1], times0_1), Transform(greaterThanEq1[3], times0_2))
        self.wait(0.1)
        self.play(FadeOut(greaterThanEq1[1], greaterThanEq1[3], greaterThanEq1[0], greaterThanEq1[2]))
        self.wait()
        self.play(greaterThanEq1[7].animate.set_opacity(0), greaterThanEq1[6].animate.set_opacity(0))
        self.wait()
        self.play(greaterThanEq1[4].animate.set_opacity(0),Transform(greaterThanEq1[9], minusC))
        # self.play(Transform(greaterThanEq1[9], minusC))
        self.wait()
        self.play(FadeIn(allVarsGEQ0))
        self.wait()
        self.play(greaterThanEq1[7].animate.set_opacity(1),  greaterThanEq1[6].animate.set_opacity(1), 
        Transform(greaterThanEq1[9], C), allVarsGEQ0[4].animate.set_color(textColorNormal).scale(8/9), 
        greaterThanEq1[4].animate.set_opacity(1), allVarsGEQ0[7].animate.set_color(textColorNormal).scale(8/9))
        self.play(FadeIn(arrow, willBeZeroAtBeginning), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(arrow, willBeZeroAtBeginning, allVarsGEQ0))
        self.wait()
        self.play(FadeIn(greaterThanEq1Dupl[0:6]))
        self.wait()
        self.play(FadeIn(objFuncMax[0]))
        self.wait()
        self.play(FadeIn(objFuncMax[1], mIsLarge))
        self.wait()
        self.play(FadeIn(maximize))
        self.play(FadeIn(minimize, objFuncMin))
        # self.play(Transform(greaterThanEq1[9], C))
        self.wait(2)
        self.play(FadeOut(feasibleArea, axes, constraints, vertices, greaterThanEq1[4:], greaterThanIneq1, mIsLarge,
        minimize, maximize, objFuncMin, objFuncMax, x1_0, x2_0, greaterThanEq1Dupl[0:6]))
        self.wait(2)






class CornerPointsSimplex(Scene):
    def construct(self):

        step3 = Text("Step3:", color = textColorNormal, weight= BOLD).shift(UP*3, LEFT*5.5)
        step3Contents1 = Text("Find a corner point and start traversing", color = textColorNormal).scale(0.7).next_to(step3, RIGHT)
        step3Contents2 = Text("edges to reach the optimal point", color = textColorNormal).scale(0.7).next_to(
            step3Contents1, DOWN).shift(LEFT*0.8)


        eq1 = MathTex("A_{1,1}x_1+A_{1,2}x_2+A_{1,3}x_3+...+A_{1,n}a_l = C_1", color=textColorNormal).scale(0.8).shift(UP)
        eq2 = MathTex("A_{2,1}x_1+A_{2,2}x_2+A_{2,3}x_3+...+A_{2,n}a_l = C_2", color=textColorNormal).scale(0.8).next_to(eq1, DOWN)
        eq3 = MathTex("A_{3,1}x_1+A_{3,2}x_2+A_{3,3}x_3+...+A_{3,n}a_l = C_3", color=textColorNormal).scale(0.8).next_to(eq2, DOWN)
        

        dot1 = MathTex(".", color = textColorNormal).shift(DOWN*0.7).scale(0.9)
        dot2 = MathTex(".", color = textColorNormal).shift(DOWN*0.8).scale(0.9)
        dot3 = MathTex(".", color = textColorNormal).shift(DOWN*0.9).scale(0.9)
        dots = VGroup(dot1, dot2, dot3)
        
        eqM = MathTex("A_{m,1}x_1+A_{m,2}x_2+A_{m,3}x_3+...+A_{m,n}a_l = C_m", color=textColorNormal).scale(0.8).next_to(dots, DOWN*0.3)

        equations = VGroup(eq1, eq2, eq3, dots, eqM)
        eqBrace = Brace(equations, RIGHT, color=textColorNegative)
        m = MathTex("m", color=textColorNegative).next_to(eqBrace, RIGHT)


        variables = MathTex("x_1,...x_i,s_1,...s_j,S_1,...S_k,a_1,...a_l", color=textColorNormal).shift(DOWN*3).scale(0.9)
        varBrace = Brace(variables, UP, color=dodgerBlue)
        n = MathTex("n", color=dodgerBlue).next_to(varBrace, UP)



        # m.shift(LEFT*9, UP).set_color(textColorNormal)
        # n.shift(LEFT*3.95, UP*2).set_color(textColorNormal)

        eqsText = MathTex("equations", color=textColorNormal)#.next_to(m, RIGHT).shift(UP*0.03,RIGHT*0.5)
        arrowEqs = Arrow([-3.8, 0.9, 0], [-2.8, 0.9, 0], color = textColorNormal)
        varsText = MathTex("variables", color=textColorNormal)#.next_to(n, RIGHT).shift(UP*0.08,RIGHT*0.5)
        arrowVars = Arrow([-3.9, 0.08, 0], [-2.9, 0.08, 0], color = textColorNormal)

        noOfCornerPtsText = Tex("No. of corner points ", color = textColorNormal).shift(LEFT*3, DOWN*0.8).scale(0.9)
        nChooseM = MathTex("=^nC_m", color = textColorNormal).next_to(noOfCornerPtsText, RIGHT)
        noOfCornerPts = MathTex("= \\frac{n!}{m!(n-m)!}", color = textColorNormal).next_to(nChooseM, RIGHT)

        obtainedByText = Tex("Obtained by:", color = textColorNormal).scale(0.9).shift(LEFT*3, DOWN*2)
        expl1 = Tex("1. Setting (n-m) variables equal to 0", color = textColorNormal).next_to(obtainedByText, RIGHT)
        expl2 = Tex("2. Solving for remaining m variables", color = textColorNormal).next_to(expl1, DOWN)
        basicVars = Tex("Basic Variables", color = textColorNegative).next_to(expl2, DOWN)


        # self.add(step3, step3Contents1, step3Contents2, eq1, eq2, eq3, dots, eqM, variables, eqBrace, varBrace, m, n)
        # self.add(step3, step3Contents1, step3Contents2, m, n, eqsText, varsText, arrowEqs, arrowVars, noOfCornerPtsText, 
        # nChooseM, noOfCornerPts, obtainedByText, expl1, expl2, basicVars)

        self.wait()
        self.play(FadeIn(step3), run_time = 0.7)
        self.wait()
        self.play(FadeIn(step3Contents1), run_time = 0.7)
        self.wait()
        self.play(FadeIn(step3Contents2), run_time = 0.7)
        self.wait()

        staggeredEqDisp = [FadeIn(eq1), FadeIn(eq2), FadeIn(eq3), FadeIn(dots), FadeIn(eqM)]
        self.play(LaggedStart(*staggeredEqDisp, lag_ratio=0.2), run_time=3)
        self.wait(0.2)
        self.play(FadeIn(eqBrace, m))
        self.wait()
        self.play(FadeIn(variables))
        self.wait(0.2)
        self.play(FadeIn(varBrace, n))
        self.wait()
        self.play(m.animate.shift(LEFT*9, UP).set_color(textColorNormal), n.animate.shift(LEFT*3.95, UP*2).set_color(textColorNormal),
        FadeOut(equations, variables, varBrace, eqBrace))

        eqsText.next_to(m, RIGHT).shift(UP*0.03,RIGHT*0.5)
        varsText.next_to(n, RIGHT).shift(UP*0.08,RIGHT*0.5)
        self.wait()
        self.play(FadeIn(arrowVars, arrowEqs, eqsText, varsText), run_time = 0.7)
        self.wait()
        self.play(FadeIn(noOfCornerPtsText), run_time = 0.7)
        self.wait()
        self.play(FadeIn(nChooseM), run_time = 0.7)
        self.wait()
        self.play(FadeIn(noOfCornerPts), run_time = 0.7)
        self.wait(2)
        self.play(FadeIn(obtainedByText), run_time = 0.7)
        self.wait()
        self.play(FadeIn(expl1), run_time = 0.7)
        self.wait()
        self.play(FadeIn(expl2), run_time = 0.7)
        self.wait(2)
        self.play(FadeIn(basicVars), run_time = 0.7)
        self.wait(2)
        self.play(FadeOut(step3Contents1, step3Contents2, step3, arrowEqs, arrowVars, eqsText, varsText, noOfCornerPtsText,
        noOfCornerPts, nChooseM, obtainedByText, expl1, expl2, basicVars, m, n))
        self.wait(2)





class DataToTableScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.9)#.shift(LEFT*1.7) MathTex("", color = textColorNormal).shift()

        optimizeText = Tex("Optimize Score:", color = textColorNormal).scale(0.9).shift(UP*3, LEFT*5)
        objFunc = MathTex("Z = ","1.5","x_1","+","0.5","x_2", color = textColorNormal).shift(UP*3, LEFT*1)

        constraintsText = Tex("Under the constraints:", color = textColorNormal).shift(UP*2, LEFT*4.4).scale(0.9)

        scriptingConstraintText = Tex("(Scripting)", color = textColorNormal).shift(UP*1.7, RIGHT*4.4).scale(0.9)
        scriptingConst1 = MathTex("2x_1+ 6x_2 \\leq 90", color = textColorNormal).shift(UP*1.7)
        scriptingConst2 = MathTex("\\frac{2}{2}x_1+ \\frac{6}{2}x_2 \\leq \\frac{90}{2}", color = textColorNormal).shift(UP*1.7)
        scriptingConst3 = MathTex("x_1+ 3x_2 \\leq 45", color = textColorNormal).shift(UP*0.7)
        scriptingEq = MathTex("x_1","+","3","x_2","+","s_1","=","45", color = textColorNormal).shift(UP*0.7)

        scripting = VGroup(scriptingConstraintText, scriptingConst1, scriptingConst2, scriptingConst3, scriptingEq)

        productionConstraintText = Tex("(Production)", color = textColorNormal).shift(UP*0.7, RIGHT*4.4).scale(0.9)
        productionConst1 = MathTex("20x_1+ 5x_2 \\leq 270", color = textColorNormal).shift(UP*0.7)
        productionConst2 = MathTex("\\frac{20}{5}x_1+ \\frac{5}{5}x_2 \\leq \\frac{270}{5}", color = textColorNormal).shift(UP*0.3)
        productionConst3 = MathTex("4x_1+ 4x_2 \\leq 54", color = textColorNormal).shift(DOWN*2)
        productionEq = MathTex("4","x_1","+","x_2","+","s_2","=","54", color = textColorNormal).shift(DOWN*2)

        production = VGroup(productionConstraintText, productionConst1, productionConst2, productionConst3, productionEq)


        # productionConstraintText.shift(DOWN*1.7)
        # productionEq.shift(UP*2.4)
        # scriptingEq.shift(UP*0.7)


        atTheOriginText = Tex("At the origin:", color = textColorNormal).shift(DOWN*0.7, LEFT*5.2).scale(0.9)
        scriptingEqOrg = MathTex("0 + 3*0 +"," s_1"," = ","45", color = textColorNormal).shift(DOWN*1.3)
        productionEqOrg = MathTex("4*0 + 0 +"," s_2 ","= ","54", color = textColorNormal).shift(DOWN*2.3)
        basicVars = VGroup(scriptingEqOrg[1], productionEqOrg[1])
        basicVarsBrace = Brace(basicVars, LEFT, color = RED, sharpness=1)
        basicVarsText = Tex("Basic variables", color = RED).scale(0.9).next_to(basicVarsBrace, LEFT)


        # productionEqOrg[0].set_opacity(0)
        # scriptingEqOrg[0].set_opacity(0)

        # optimizeText.set_opacity(0)
        # constraintsText.set_opacity(0)
        # atTheOriginText.set_opacity(0)
        # basicVarsBrace.set_opacity(0)
        # basicVarsText.set_opacity(0)

        # objFunc.shift(LEFT*3.7)
        # scriptingEq.shift(UP*1.65, RIGHT*0.5)
        # productionEq.shift(UP*1.95, RIGHT*0.5)
        # scriptingEqOrg.shift(UP*4.4, RIGHT*4)
        # productionEqOrg.shift(UP*4.7, RIGHT*4)


        table1 = simplexTables.table1
        staggeredColLabelDisp = [FadeIn(table1.get_rows()[0][1]), FadeIn(table1.get_rows()[0][2]), 
        FadeIn(table1.get_rows()[0][3]), FadeIn(table1.get_rows()[0][4]), FadeIn(table1.get_rows()[0][5])]

        table2 = simplexTables.table2

        objEqn = MathTex("Z ","-1.5","x_1","-0.5","x_2","=","0", color = textColorNormal).shift(UP*3, RIGHT)


        staggeredScriptingEqToTable = [ReplacementTransform(scriptingEq[0], table1.get_rows()[2][1]), 
        FadeOut(scriptingEq[1], scriptingEq[4]), ReplacementTransform(scriptingEq[2], table1.get_rows()[2][2]), 
        ReplacementTransform(scriptingEq[3], table1.get_rows()[0][2]), ReplacementTransform(scriptingEq[5], table1.get_rows()[2][3]), 
        FadeOut(scriptingEq[6]), FadeIn(table1.get_rows()[2][4]), Create(table1.get_vertical_lines()[4]),
        ReplacementTransform(scriptingEq[7], table1.get_rows()[2][5])]

        staggeredProdEqToTable = [ReplacementTransform(productionEq[0], table1.get_rows()[3][1]), 
        ReplacementTransform(productionEq[1], table1.get_rows()[0][1]), FadeOut(productionEq[2], productionEq[4]),
        ReplacementTransform(productionEq[3], table1.get_rows()[3][2]), FadeIn(table1.get_rows()[3][3]),
        ReplacementTransform(productionEq[5], table1.get_rows()[3][4]), FadeOut(productionEq[6]), 
        ReplacementTransform(productionEq[7], table1.get_rows()[3][5])]

        staggeredBasicVar1ToTable = [Create(table1.get_vertical_lines()[0]), 
        ReplacementTransform(scriptingEqOrg[1], table1.get_rows()[2][0]), 
        FadeOut(scriptingEqOrg[2]), ReplacementTransform(scriptingEqOrg[3], table1.get_rows()[2][5])]

        staggeredBasicVar2ToTable = [ReplacementTransform(productionEqOrg[1], table1.get_rows()[3][0]), 
        FadeOut(productionEqOrg[2]), ReplacementTransform(productionEqOrg[3], table1.get_rows()[3][5]),]

                                #FadeOut(objFunc)
        staggeredObjEqToTable = [ ReplacementTransform(objEqn[0], table1.get_rows()[1][0]), 
        ReplacementTransform(objEqn[1], table1.get_rows()[1][1]), ReplacementTransform(objEqn[2], table1.get_rows()[0][1]), 
        ReplacementTransform(objEqn[3], table1.get_rows()[1][2]), ReplacementTransform(objEqn[4], table1.get_rows()[0][2]),
        FadeIn(table1.get_rows()[1][3], table1.get_rows()[1][4]), FadeOut(objEqn[5]), 
        ReplacementTransform(objEqn[6], table1.get_rows()[1][5]), Create(table1.get_horizontal_lines()[1])]

        # self.add(optimizeText, objFunc, constraintsText, scriptingEq, productionEq, atTheOriginText, 
        # scriptingEqOrg, productionEqOrg, basicVarsBrace, basicVarsText, table1, objEqn)

        # self.wait()
        # # self.play(FadeIn( simplexTable2))
        # self.wait()
        # self.play(Transform(table1.get_rows()[1][1], table2.get_rows()[1][1]))
        # self.wait()


        self.wait()
        # staggeredOpt = [FadeIn(optimizeText), FadeIn(objFunc)]
        # self.play(LaggedStart(*staggeredOpt, lag_ratio=0.2), run_time=1.7)
        self.play(FadeIn(optimizeText))
        self.play(FadeIn(objFunc))
        
        self.wait()
        staggeredConst = [FadeIn(scriptingConst1, scriptingConstraintText), FadeIn(productionConst1, productionConstraintText)]
        self.play(FadeIn(constraintsText))
        self.play(LaggedStart(*staggeredConst, lag_ratio=0.2), run_time=1.7)
        self.wait()
        self.play(Transform(scriptingConst1, scriptingConst2), Transform(productionConst1, productionConst2),
        productionConstraintText.animate.shift(DOWN*0.4))
        self.wait()
        self.play(FadeIn(scriptingConst3, productionConst3), productionConstraintText.animate.shift(DOWN*1.3), 
        productionConst1.animate.shift(DOWN*1.3))
        self.wait()
        self.play(ReplacementTransform(scriptingConst3, scriptingEq), ReplacementTransform(productionConst3, productionEq))
        self.wait()
        self.play(FadeOut(scriptingConst1, productionConst1), scriptingEq.animate.shift(UP*0.7), 
        productionEq.animate.shift(UP*2.4), productionConstraintText.animate.shift(UP*1.4),
        scriptingConstraintText.animate.shift(DOWN*0.25))
        self.wait()
        
        staggeredOrgEqs = [FadeIn(scriptingEqOrg), FadeIn(productionEqOrg)]
        self.play(FadeIn(atTheOriginText))
        self.play(LaggedStart(*staggeredOrgEqs, lag_ratio=0.2), run_time=1.7)
        self.wait()
        self.play(FadeOut(productionEqOrg[0], scriptingEqOrg[0]))
        self.wait()
        self.play(FadeIn(basicVarsBrace, basicVarsText))
        self.wait(2)
        self.play(FadeOut(optimizeText, constraintsText, atTheOriginText, basicVarsBrace, 
        basicVarsText, productionConstraintText, scriptingConstraintText))
        self.play(objFunc.animate.shift(LEFT*3.7), scriptingEq.animate.shift(UP*1.65, RIGHT*0.5),
        productionEq.animate.shift(UP*1.95, RIGHT*0.5), scriptingEqOrg[1:].animate.shift(UP*4.4, RIGHT*4),
        productionEqOrg[1:].animate.shift(UP*4.7, RIGHT*4))
        
        self.wait()
        self.play(LaggedStart(*staggeredColLabelDisp, lag_ratio=0.2), run_time=3)
        self.wait()
        self.play(Create(table1.get_horizontal_lines()[0]))
        self.wait()
        self.play(LaggedStart(*staggeredScriptingEqToTable, lag_ratio=0.3), run_time=5.2)
        self.wait()
        self.play(LaggedStart(*staggeredProdEqToTable, lag_ratio=0.3), run_time=5)
        self.wait()
        self.play(LaggedStart(*staggeredBasicVar1ToTable, lag_ratio=0.3), run_time=3)
        self.wait()
        self.play(LaggedStart(*staggeredBasicVar2ToTable, lag_ratio=0.3), run_time=3)
        self.wait()
        self.play(TransformFromCopy(objFunc, objEqn))
        self.wait()
        self.play(LaggedStart(*staggeredObjEqToTable, lag_ratio=0.3), run_time=6)
        self.wait(3)





class SimplexCalculationsScene(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        # self.camera.frame.scale(0.9)#.shift(LEFT*1.7) MathTex("", color = textColorNormal).shift()


        objFunc = MathTex("Z = ","1.5","x_1","+","0.5","x_2", color = textColorNormal).shift(UP*3, LEFT*4.7)
        objFuncAtOrigin = MathTex("=1.5*0+0.5*0", color = textColorNormal).shift(UP*3, LEFT*0.6)
        val0 = MathTex("=0", color = textColorNormal).shift(UP*3, RIGHT*2)
        objEqn = MathTex("Z ","-1.5","x_1","-0.5","x_2","=","0", color = textColorNormal).shift(UP*3, RIGHT)

        backgroundHighlightRect = Rectangle(color=GREEN, height=1, width=1.3).set_opacity(0.7).shift(RIGHT*3.7, DOWN*0.5)

        table1 = simplexTables.table1
        # table1.get_rows()[0][5].add_to_back(backgroundHighlightRect)
        #table1.get_horizontal_lines()[1]

        underlineX1Coeff = Underline(objFunc[1], color = BLUE)
        underlineX2Coeff = Underline(objFunc[3:5], color = BLUE)
        rateOfImprovText = Tex("Rates of improvement", color = dodgerBlue).scale(0.9).next_to(underlineX1Coeff, DOWN).shift(RIGHT)
        ratesOfImprovement = VGroup(underlineX1Coeff, underlineX2Coeff, rateOfImprovText)

        frameBoxObjFunc = SurroundingRectangle(objFunc[1], buff=0.1, color = PURE_RED)
        frameBoxObjEqn = SurroundingRectangle(objEqn[1], buff=0.1, color = PURE_RED)
        frameBoxObjEqnSimplex = SurroundingRectangle(table1.get_rows()[1][1], buff=0.1, color = PURE_RED)
        frameboxes = VGroup(frameBoxObjFunc, frameBoxObjEqnSimplex)

        ratioHeading = MathTex("C","/","Coeff", color = textColorNormal).scale(0.9).shift(RIGHT*5.8, DOWN*0.6)
        ratioHeading2 = MathTex("C","/","Coeff", color = textColorNormal).scale(0.7).shift(RIGHT*5.8, DOWN*0.6)
        ratio1 = MathTex("45","/","1","=","45", color = textColorNormal).scale(0.9).shift(RIGHT*5.8, DOWN*1.6)
        ratio2 = MathTex("54","/","4","=","13.5", color = textColorNormal).scale(0.9).shift(RIGHT*5.8, DOWN*2.6)

        ratio3 = MathTex("\\frac{31.5}{2.75}","=","11.45", color = textColorNormal).scale(0.7).shift(RIGHT*5.8, DOWN*1.6)
        ratio4 = MathTex("\\frac{13.5}{0.25}","=","54", color = textColorNormal).scale(0.7).shift(RIGHT*5.8, DOWN*2.6)
        ratios = VGroup(ratioHeading, ratio1, ratio2)

        axes = Axes(
            x_range=[-1*16/9, 50*16/9, 10],
            y_range=[-1, 50, 10],
            y_length=7,
            x_length=7*16/9,
            x_axis_config={"color":BLACK},
            y_axis_config={"color":BLACK}
        ).scale(1.7).shift(UP*5, RIGHT*9)

        constraint1 = axes.get_graph(lambda x: -1/3*x+10, color = BLACK)
        constraint2 = axes.get_graph(lambda x: -4*x+36, color = BLACK)

        dotA = Dot([-1.165,-0.7,0], color=ORANGE).scale(0.8)
        dotB = Dot([0.94,-0.7,0], color=ORANGE).scale(0.8)
        dotC = Dot([0.49,1.08,0], color=RED).scale(0.8)
        dotD = Dot([-1.165,1.63,0], color=ORANGE).scale(0.8)

        constraint1Eq = MathTex("x + 3y = 45", color = textColorNormal).shift(UP*0.3, RIGHT*4.5)
        constraint2Eq = MathTex("4x + y = 54", color = textColorNormal).shift(DOWN*2, RIGHT*2.7)
        commonShadedPink = Polygon([-1.165,-0.7,0], [0.94,-0.7,0], [0.49,1.08,0], [-1.165,1.63,0])
        commonShadedPink.set_fill(color = PINK, opacity= 0.7)
        commonShadedPink.set_stroke(width=0)       
        commonShadedBlue = Polygon([-1.165,-0.7,0], [0.94,-0.7,0], [0.49,1.08,0], [-1.165,1.63,0])
        commonShadedBlue.set_fill(color = BLUE, opacity= 0.7)
        commonShadedBlue.set_stroke(width=0)
        constraint1Intercept = MathTex("45", color = textColorNormal).shift(DOWN, RIGHT*5.5)
        constraint2Intercept = MathTex("13.5", color = textColorNormal).shift(DOWN, RIGHT*0.5)
        xSmallestInterceptUnderline = Underline(constraint2Intercept, color = PURE_RED)
        currentPt = Dot(color=selectedVertexColor).scale(1.3).shift(dotA.get_center())
        
        
        currentPt2 = Dot(color=selectedVertexColor).scale(1.3).shift(dotB.get_center())
        currentPt3 = Dot(color=selectedVertexColor).scale(1.3).shift(dotC.get_center())

        graph = VGroup(commonShadedBlue, commonShadedPink, axes, constraint1, constraint2, 
        constraint1Eq, constraint2Eq, currentPt)
        # constraint2Intercept, constraint1Intercept, xSmallestInterceptUnderline,

        pivotRowFramebox = SurroundingRectangle(table1.get_rows()[3], color = PURE_RED)
        pivotColFramebox = SurroundingRectangle(table1.get_columns()[1], color = PURE_RED)
        pivotRowText = Tex("Pivot Row", color = PURE_RED).scale(0.9).next_to(pivotRowFramebox, LEFT)
        pivotColText = Tex("Pivot Column", color = PURE_RED).scale(0.9).next_to(pivotColFramebox, UP).shift(RIGHT)

        pivotElementText = Tex("Pivot Element", color = dodgerBlue).scale(0.9).next_to(pivotRowFramebox, DOWN).shift(LEFT)
        backgroundHighlightRect2 = Rectangle(color=dodgerBlue, height=0.5, width=1.02).set_opacity(0.5).shift(LEFT*2.2, DOWN*2.6)

        s2Underline = Underline(table1.get_rows()[3][0], color = PURE_RED).scale(1.3)
        x1Underline = Underline(table1.get_rows()[0][1], color = PURE_RED).scale(1.3)

        extendedTable = VGroup(table1,ratios)#.scale(0.6).shift(LEFT*4.5, DOWN*1.3)
        # extendedTable.shift(RIGHT*4.5, UP*1.3).scale(5/3)
        # table1.get_rows()[3][1].add_to_back(backgroundHighlightRect2)


        # staggeredColLabelDisp = [FadeIn(table1.get_rows()[0][1]), FadeIn(table1.get_rows()[0][2]), 
        # FadeIn(table1.get_rows()[0][3]), FadeIn(table1.get_rows()[0][4]), FadeIn(table1.get_rows()[0][5])]

        modifiedLastRow1 = simplexTables.modifiedLastRow1
        modifiedLastRow2 = simplexTables.modifiedLastRow2

        modifiedObjFunc1 = simplexTables.modifiedObjFunc1
        modifiedObjFunc2 = simplexTables.modifiedObjFunc2

        modifiedR2_1 = simplexTables.modifiedR2_1
        modifiedR2_c2 = simplexTables.modifiedR2_2


        rowLabel1 = MathTex("R_1", color = textColorNormal).shift(DOWN*0.55, LEFT*5.5).scale(0.9)
        rowLabel2 = MathTex("R_2", color = textColorNormal).shift(DOWN*1.575, LEFT*5.5).scale(0.9)
        rowLabel3 = MathTex("R_3", color = textColorNormal).shift(DOWN*2.6, LEFT*5.5).scale(0.9)

        gaussJordElimGeneral = MathTex("R_{i,New} "," = R_{i,Current} ","- (Pivot Column Coeff)_{R_i}","*R_{Pivot}", 
        color = textColorNormal).shift(UP*3)
        gaussJordElimR1 = MathTex("R_{1,New}"," = ","R_{1,Current} ","- ","(Pivot Column Coeff)_{R_1}","*",
        "R_{Pivot}", color = textColorNormal).scale(0.9).shift(UP*2)
        gaussJordElimR1a = MathTex("R_{1,New}"," = ","[","-1.5",",","-0.5",",","0",",","0",",","0","] ","- ",
        "(-1.5)","*","[","1",",","0.25",",","0",",","0.25",",","13.5","]", color = textColorNormal).scale(0.9).shift(UP*2, RIGHT*0.2)
        gaussJordElimR1b = MathTex("R_{1,New}"," = ","[","-1.5",",","-0.5",",","0",",","0",",","0","] ","- ",
        "[","-1.5",",","-0.375",",","0",",","-0.375",",","-20.25","]", color = textColorNormal).scale(0.9).shift(UP*2, RIGHT*0.5)
        gaussJordElimR1c = MathTex("R_{1,New}"," = ","[","0",",","-0.125",",","0",",","0.375",",","20.25","]", 
        color = textColorNormal).scale(0.9).shift(UP*2, LEFT*2)

        staggeredGaussJordAnimR1 = [ ReplacementTransform(gaussJordElimR1[2], gaussJordElimR1a[2:13]),
            TransformFromCopy(table1.get_rows()[1][1],  gaussJordElimR1a[3]), TransformFromCopy(table1.get_rows()[1][2],  gaussJordElimR1a[5]),
            TransformFromCopy(table1.get_rows()[1][3],  gaussJordElimR1a[7]), TransformFromCopy(table1.get_rows()[1][4],  gaussJordElimR1a[9]),
            TransformFromCopy(table1.get_rows()[1][5],  gaussJordElimR1a[11]), ReplacementTransform(gaussJordElimR1[4], gaussJordElimR1a[14]), 
            TransformFromCopy(table1.get_rows()[1][1],  gaussJordElimR1a[14]),  ReplacementTransform(gaussJordElimR1[5], gaussJordElimR1a[15]),
            ReplacementTransform(gaussJordElimR1[6], gaussJordElimR1a[16:27]), TransformFromCopy(table1.get_rows()[3][1],  gaussJordElimR1a[17]), 
            TransformFromCopy(table1.get_rows()[3][2],  gaussJordElimR1a[19]), TransformFromCopy(table1.get_rows()[3][3],  gaussJordElimR1a[21]), 
            TransformFromCopy(table1.get_rows()[3][4],  gaussJordElimR1a[23]), TransformFromCopy(table1.get_rows()[3][5],  gaussJordElimR1a[25]),
        ]

        staggeredObjFuncMod1 = [
            FadeOut(gaussJordElimR1[:2]), Transform(table1.get_rows()[1][1], modifiedObjFunc1[1]),
            FadeOut(gaussJordElimR1c[2]), ReplacementTransform(gaussJordElimR1c[3], modifiedObjFunc1[1]),
            Transform(table1.get_rows()[1][2], modifiedObjFunc1[2]), FadeOut(gaussJordElimR1c[4]), 
            ReplacementTransform(gaussJordElimR1c[5], modifiedObjFunc1[2]), Transform(table1.get_rows()[1][3], modifiedObjFunc1[3]),
            FadeOut(gaussJordElimR1c[6]), ReplacementTransform(gaussJordElimR1c[7], modifiedObjFunc1[3]),
            Transform(table1.get_rows()[1][4], modifiedObjFunc1[4]), FadeOut(gaussJordElimR1c[8]), 
            ReplacementTransform(gaussJordElimR1c[9], modifiedObjFunc1[4]), Transform(table1.get_rows()[1][5], modifiedObjFunc1[5]),
            FadeOut(gaussJordElimR1c[10]), ReplacementTransform(gaussJordElimR1c[11], modifiedObjFunc1[5]), 
            FadeOut(gaussJordElimR1c[12])
        ]


        gaussJordElimR2 = MathTex("R_{2,New}"," = ","R_{2,Current} ","- ","(Pivot Column Coeff)_{R_2}","*","R_{Pivot}", 
        color = textColorNormal).scale(0.9).shift(UP*2)
        gaussJordElimR2a = MathTex("R_{2,New}"," = ","[","1",",","3",",","1",",","0",",","45","] ","- ","1","*","[","1",",",
        "0.25",",","0",",","0.25",",","13.5","]", color = textColorNormal).scale(0.9).shift(UP*2)
        gaussJordElimR2b = MathTex("R_{2,New}"," = ","[","0",",","2.75",",","1",",","-0.25",",","31.5","]", 
        color = textColorNormal).scale(0.9).shift(UP*2)



        
        pivotElement2 = Rectangle(color=dodgerBlue, height=0.5, width=1.02).set_opacity(0.5).shift(table1.get_rows()[2][2].get_center())
        modifiedLastRow3 = simplexTables.modifiedLastRow3
        modifiedR2_2 = simplexTables.modifiedR2_2

        x1_final = MathTex("x_1 ","= ","10.64", color = textColorNormal).shift(UP*3)
        x2_final = MathTex("x_2 ","= ","11.45", color = textColorNormal).shift(UP*2)
        

        # gaussJordTransformationsI

    #     self.add(table1, objFunc, objFuncAtOrigin, val0, ratesOfImprovement, frameboxes,  x1Underline, s2Underline, 
    #     modifiedLastRow1, modifiedLastRow2)#pivotRowFramebox, 
    #     self.play(Transform(table1.get_rows()[3][0], table2.get_rows()[3][0]))
    #    pivotColFramebox, pivotRowText, pivotColText, pivotElementText)#, ratios, graph)

        self.add(table1, objFunc)
        self.wait()
        self.play(FadeIn(objFuncAtOrigin))
        self.play(FadeIn(val0), FadeIn(backgroundHighlightRect))
        self.wait(2)
        self.play(FadeOut(backgroundHighlightRect, objFuncAtOrigin, val0))
        self.wait()
        self.play(Create(underlineX1Coeff), Create(underlineX2Coeff), FadeIn(rateOfImprovText)),
        self.wait()
        self.play(Uncreate(underlineX1Coeff), Uncreate(underlineX2Coeff), FadeOut(rateOfImprovText), Create(frameBoxObjFunc))
        self.wait()
        self.play(FadeIn(objEqn))
        self.wait()
        self.play(Create(frameBoxObjEqn), Create(frameBoxObjEqnSimplex))
        self.wait(2)
        self.play(Uncreate(frameBoxObjFunc), Uncreate(frameBoxObjEqn), Uncreate(frameBoxObjEqnSimplex), FadeOut(objEqn, objFunc))
        self.wait()
        self.play(FadeIn(ratioHeading), run_time=0.7)
        self.wait()
        self.play(FadeIn(ratio1[1]), TransformFromCopy(table1.get_rows()[2][5], ratio1[0]), TransformFromCopy(table1.get_rows()[2][1], ratio1[2]))
        self.play(FadeIn(ratio1[3:]), run_time=0.7)
        self.wait()
        self.play(FadeIn(ratio2[1]), TransformFromCopy(table1.get_rows()[3][5], ratio2[0]), TransformFromCopy(table1.get_rows()[3][1], ratio2[2]))
        self.play(FadeIn(ratio2[3:]), run_time=0.7)
        self.wait()
        self.play(extendedTable.animate.scale(0.6).shift(LEFT*4.5, DOWN*1.3), FadeIn(graph))
        self.wait()
        self.play(ReplacementTransform(ratio1, constraint1Intercept))
        self.play(ReplacementTransform(ratio2, constraint2Intercept))
        self.play(FadeOut(ratioHeading), run_time=0.7)
        self.wait()
        self.play(Transform(currentPt, currentPt2))
        self.wait()
        self.play(FadeOut(graph, constraint1Intercept, constraint2Intercept), 
            table1.animate.shift(RIGHT*4, UP*1.3).scale(5/3))
        self.wait()
        self.play(Create(x1Underline))
        self.wait()
        self.play(Create(s2Underline))
        self.wait()
        self.play(Uncreate(s2Underline), Uncreate(x1Underline))
        self.play(Create(pivotColFramebox), FadeIn(pivotColText))
        self.wait()
        self.play(Create(pivotRowFramebox), FadeIn(pivotRowText))
        self.wait()
        self.play(FadeIn(backgroundHighlightRect2, pivotElementText))
        self.wait()
        self.play(Uncreate(pivotColFramebox), Uncreate(pivotRowFramebox), 
            FadeOut(pivotRowText, pivotColText, pivotElementText))

        self.wait()
        self.play(Transform(table1.get_rows()[3][0], modifiedLastRow1[0]))
        self.wait()
        self.play(FadeOut(backgroundHighlightRect2))
        staggeredLastRowMod1 = [Transform(table1.get_rows()[3][1], modifiedLastRow1[1]), 
        Transform(table1.get_rows()[3][2], modifiedLastRow1[2]), Transform(table1.get_rows()[3][3], modifiedLastRow1[3]), 
        Transform(table1.get_rows()[3][4], modifiedLastRow1[4]), Transform(table1.get_rows()[3][5], modifiedLastRow1[5])]
        self.play(LaggedStart(*staggeredLastRowMod1, lag_ratio=0.3), run_time=4)
        self.wait()
        self.play(Transform(table1.get_rows()[3][1], modifiedLastRow2[1]), 
        Transform(table1.get_rows()[3][2], modifiedLastRow2[2]), Transform(table1.get_rows()[3][3], modifiedLastRow2[3]), 
        Transform(table1.get_rows()[3][4], modifiedLastRow2[4]), Transform(table1.get_rows()[3][5], modifiedLastRow2[5]))
        self.wait()

        staggeredGaussJordGeneral = [FadeIn(gaussJordElimGeneral[0]), FadeIn(gaussJordElimGeneral[1]),
        FadeIn(gaussJordElimGeneral[2]), FadeIn(gaussJordElimGeneral[3])]
        self.play(LaggedStart(*staggeredGaussJordGeneral, lag_ratio=0.3), run_time=4)
        self.wait()
        self.play(FadeIn(gaussJordElimR1))




        # self.add(table1, modifiedLastRow1, modifiedLastRow2, rowLabel1, rowLabel2, rowLabel3, gaussJordElimGeneral, gaussJordElimR1)
        self.wait()
        self.play(ApplyMethod(gaussJordElimR1[3:].shift, RIGHT*1.4), run_time=0.7)
        self.play(LaggedStart(*staggeredGaussJordAnimR1, lag_ratio=0.3), run_time=12)
        self.wait()
        self.play(Transform(gaussJordElimR1a[14:], gaussJordElimR1b[14:]))
        self.wait()
        gaussJordElimR1[2:].set_opacity(0)
        self.play(ReplacementTransform(gaussJordElimR1a[2:], gaussJordElimR1c[2:]))
        self.wait()
        self.play(LaggedStart(*staggeredObjFuncMod1, lag_ratio=0.3), run_time=6)
        self.wait()
        self.play(FadeIn(gaussJordElimR2), FadeOut(modifiedObjFunc1[1:]))
        self.wait()
        self.play(ReplacementTransform(gaussJordElimR2, gaussJordElimR2a))
        self.wait()
        self.play(ReplacementTransform(gaussJordElimR2a, gaussJordElimR2b))
        self.wait()
        self.play(Transform(table1.get_rows()[2][1], modifiedR2_1[1]), Transform(table1.get_rows()[2][2], modifiedR2_1[2]),
        Transform(table1.get_rows()[2][3], modifiedR2_1[3]), Transform(table1.get_rows()[2][4], modifiedR2_1[4]),
        Transform(table1.get_rows()[2][5], modifiedR2_1[5]), FadeOut(gaussJordElimR2b, gaussJordElimGeneral))
        self.wait(3)

        modifiedR2_1.set_opacity(0)
        iter2EnterVarUnderline = Underline(table1.get_rows()[1][2], color = PURE_RED)

        self.play(Create(iter2EnterVarUnderline))
        self.wait()
        self.play(Uncreate(iter2EnterVarUnderline), FadeIn(ratioHeading2), run_time=0.7)
        self.play(FadeIn(ratio3), run_time=0.7)
        self.play(FadeIn(ratio4), run_time=0.7)
        self.wait()
        self.play(FadeIn(pivotElement2))
        self.wait()
        self.play(FadeOut(pivotElement2), FadeOut(ratio4, ratio3, ratioHeading2))
        self.play(
        Transform(table1.get_rows()[1][1], modifiedObjFunc2[1]), Transform(table1.get_rows()[1][2], modifiedObjFunc2[2]),
        Transform(table1.get_rows()[1][3], modifiedObjFunc2[3]), Transform(table1.get_rows()[1][4], modifiedObjFunc2[4]),
        Transform(table1.get_rows()[1][5], modifiedObjFunc2[5]),
        Transform(table1.get_rows()[2][1], modifiedR2_2[1]), Transform(table1.get_rows()[2][2], modifiedR2_2[2]),
        Transform(table1.get_rows()[2][3], modifiedR2_2[3]), Transform(table1.get_rows()[2][4], modifiedR2_2[4]),
        Transform(table1.get_rows()[2][5], modifiedR2_2[5]),
        Transform(table1.get_rows()[3][1], modifiedLastRow3[1]), Transform(table1.get_rows()[3][2], modifiedLastRow3[2]),
        Transform(table1.get_rows()[3][3], modifiedLastRow3[3]), Transform(table1.get_rows()[3][4], modifiedLastRow3[4]),
        Transform(table1.get_rows()[3][5], modifiedLastRow3[5]),)
        self.wait(2)

        underlineNoNeg1 = Underline(table1.get_rows()[1][1], color = PURE_RED)
        underlineNoNeg2 = Underline(table1.get_rows()[1][2], color = PURE_RED)
        underlineNoNeg3 = Underline(table1.get_rows()[1][3], color = PURE_RED)
        underlineNoNeg4 = Underline(table1.get_rows()[1][4], color = PURE_RED)
        self.play(Create(underlineNoNeg1), Create(underlineNoNeg2), Create(underlineNoNeg3), Create(underlineNoNeg4))
        self.wait()
        self.play(Uncreate(underlineNoNeg1), Uncreate(underlineNoNeg2), Uncreate(underlineNoNeg3), Uncreate(underlineNoNeg4))
        self.play(TransformFromCopy(table1.get_rows()[3][0], x1_final[0]),  TransformFromCopy(table1.get_rows()[3][5], x1_final[2]))
        self.play(FadeIn(x1_final[1]), run_time=0.5)
        self.play(TransformFromCopy(table1.get_rows()[2][0], x2_final[0]), TransformFromCopy(table1.get_rows()[2][5], x2_final[2]))
        self.play(FadeIn(x2_final[1]), run_time=0.5)
        self.wait()


        graph.shift(RIGHT*10, DOWN)
        currentPt3.shift(LEFT*2, DOWN)
        self.play(table1.animate.shift(LEFT*14), graph.animate.shift(LEFT*12))
        self.wait()
        self.play(Transform(currentPt, currentPt3), x1_final.animate.shift(DOWN*1.4), x2_final.animate.shift(DOWN*1.2))
        self.wait(3)



