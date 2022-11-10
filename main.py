from manim import *

class RiemannSums(Scene):
    def construct(self):
        title = Tex("Riemann Sums")
        subtitle = Tex("0-4?")
        subtitle.next_to(title, DOWN)
        gr1 = VGroup(title, subtitle).arrange(DOWN)

        self.play(
            Write(gr1),
        )
        self.wait()

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinates()
        graph = axes.plot(lambda x: -0.5*x**3 + 2*x**2 + 2)
        graph.set_color(YELLOW)
        self.play(
            gr1.animate.move_to(5 * RIGHT + 3 * UP),
            Create(axes, run_time = 3, lag_ratio = 0.1),
            Create(graph, run_time = 3, lag_ratio = 0.1),
        )

        all_rects = VGroup(*(
            axes.get_riemann_rectangles(graph, (0, 4), dx).set_stroke(BLACK, np.round(4 * dx, 1), background=False)
            for dx in [2**(-n) for n in range(0, 6)]
        ))
        rects = all_rects[0]
        last_rects = all_rects[-1].copy()
        last_rects.set_stroke(width=0)

        self.play(FadeIn(last_rects, lag_ratio=0.1))
        self.wait()
        self.play(FadeIn(rects, lag_ratio=0.1), FadeOut(last_rects))
        self.wait()

        # Iterations
        for new_rects in all_rects[1:]:
            self.play(Transform(rects, new_rects))
            self.wait(0.5)

        self.wait(1)

class businessIntegration(Scene):
    def construct(self):
        
        firstLine1 = Tex("Willingness to spend = ")
        firstLine2 = MathTex(r"\int_0^{q_s}")
        firstLine3 = Tex("demand function (q) dq")
        gr1 = VGroup(firstLine1, firstLine2, firstLine3).arrange(RIGHT)
        gr1.move_to(UP * 2)

        secondLine1 = Tex("Consumer expenditure = ")
        secondLine2 = MathTex(r"\int_0^{q_s}p_sdq")
        gr2 = VGroup(secondLine1, secondLine2).arrange(RIGHT)

        thirdLine1 = Tex("Willingness to spend = ")
        thirdLine2 = MathTex(r"\int_0^{q_s}")
        thirdLine3 = Tex("(demand function (q) - ps) dq")
        gr3 = VGroup(thirdLine1, thirdLine2, thirdLine3).arrange(RIGHT)
        gr3.move_to(DOWN * 2)

        self.play(
            Write(firstLine1),
            Write(firstLine2),
            Write(firstLine3),
        )
        self.wait()

        self.play(
            Write(secondLine1),
            Write(secondLine2),
        )
        self.wait()

        self.play(
            Write(thirdLine1),
            Write(thirdLine2),
            Write(thirdLine3),
        )
        self.wait()

class odometerCar(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[0]),
            (top_right[0], bottom_left[0]),
        ]
    
    def construct(self):
        axes = Axes((3, 6), (0, 7))
        axes.add_coordinates()
        distanceGraph = axes.plot(lambda x: x**2 - 5*x + 6)
        distanceLabel = axes.get_graph_label(distanceGraph, "x^2 - 5x + 6")
        distanceGraph.set_color(RED)
        distanceLabel.set_color(RED)

        velGraph = axes.plot(lambda x: 3*x - 10)
        velLabel = axes.get_graph_label(velGraph, "3x - 10")
        velGraph.set_color(BLUE)
        velLabel.set_color(BLUE)
        velLabel.move_to(RIGHT * 2)

        line1 = axes.get_vertical_line(axes.input_to_graph_point(4, distanceGraph), color = YELLOW)
        dot = Dot()
        dot.move_to(axes.input_to_graph_point(4, distanceGraph))

        self.play(
            Create(distanceLabel, run_time = 3, lag_ratio = 0.1),
            Create(axes, run_time = 3, lag_ratio = 0.1),
            Create(distanceGraph, run_time = 3, lag_ratio = 0.1),
        )
        self.wait()

        self.play(
            Create(line1),
            Create(dot),
            Create(velLabel, run_time = 2, lag_ratio = 0.1),
            Create(velGraph, run_time = 2, lag_ratio = 0.1),
        )
        self.wait()

class carDistance(Scene):
    def construct(self):
        time_label = Tex("Time (in seconds): ", "0")
        time_label.shift(2*UP)

        dots = VGroup(*list(map(Dot, [DOWN + 4 * LEFT, DOWN + 4 * RIGHT])))
        line = Line(*dots, buff = 0)
        line.set_color(RED)
        brace = Brace(line, DOWN)
        brace_text = brace.get_text("Distance traveled?")

        self.play(
            Create(time_label),
        )
        dot = Dot()
        dot.move_to(4 * LEFT + DOWN)
        dotPath = TracedPath(dot.get_center, dissipating_time = 1, stroke_opacity = [1, 0])
        self.add(dotPath)

        for i in range(4):
            time_label2 = Tex("Time (in seconds): ", i + 1)
            time_label2.shift(2*UP)
            self.play(
                Transform(time_label, time_label2),
                dot.animate(rate_func = linear).shift(2 * RIGHT),
            )
        
        self.play(*list(map(Create, dots)))
        self.play(Create(line))
        self.play(
            GrowFromCenter(brace),
            Write(brace_text)
        )

        self.wait()

class integrationIntro(Scene):
    def construct(self):
        line1 = Tex("Integration")
        line1.move_to(UP * 2)

        eng, bus, fin = Tex("Engineering", "Business", "Finances")
        gr1 = VGroup(eng, bus, fin).arrange(DOWN, aligned_edge = LEFT)

        deriv, integral, v_t, dt, equals, v_T = formula = MathTex(
            "\\frac{d}{dT}", 
            "\\int_0^T", "v(t)", "\\,dt", 
            "=", "v(T)"
        )
        formula.set_color_by_tex("v", YELLOW)

        self.play(Write(line1))
        self.wait()
        self.play(Write(gr1))
        self.wait()
        self.play(
            FadeOut(eng),
            FadeOut(bus),
            fin.animate.set_color_by_tex(YELLOW),
            fin.animate.next_to(line1, LEFT),
        )
        self.wait()
        self.play(Write(VGroup(integral, v_t, dt)))
        self.wait()
        self.play(Write(VGroup(deriv, equals, v_T)))
        self.wait()
        self.play(
            FadeOut(fin),
            FadeOut(line1),
            FadeOut(formula),
        )
        self.wait()

class lorenzCurve(Scene):
    def construct(self):
        line1 = Tex("Lorenz Curve")
        line2 = Tex("Line of Equality")
        line2.move_to(LEFT * 2.5)
        line2.set_color(YELLOW)

        self.play(Write(line1))
        self.wait()

        axes = Axes(
            x_range=[0, 1.1, 0.2],
            y_range=[0, 1.1, 0.2],
            axis_config={"color": GREEN},
            tips = True,
        )
        axes.add_coordinates()

        lorenzCurve = axes.plot(
            lambda x: x**3,
            x_range = [0, 1],
            color = RED,
        )

        line = DashedLine(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 1),
            dash_length = 0.1,
            color = YELLOW,
        )

        labels = axes.get_axis_labels(
            x_label = Tex("Wealth Rank"),
            y_label = Tex("Cumulative Share of Wealth"),
        )

        self.play(
            Create(axes, run_time = 2, lag_ratio = 0.1),
            Create(labels, run_time = 2, lag_ratio = 0.1),
        )

        self.play(
            # line1.animate.set_fill(RED),
            line1.animate.move_to(5 * RIGHT),
            Write(line2),
            Create(lorenzCurve, run_time = 2, lag_ratio = 0.1),
            Create(line, run_time = 2, lag_ratio = 0.1),
        )

        self.wait()

class consumerProducerSurplus(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[0]),
            (top_right[0], bottom_left[0]),
        ]

    def construct(self):
        consumer0, andProducerSurplus = line1 = Tex("Consumer", " and Producer Surplus")

        self.play(Write(line1))
        self.wait()

        axes = Axes(
            x_range=[0, 1],
            y_range=[0, 1],
            axis_config={"color": GREEN},
            tips = True,
        )
        axes.add_coordinates()

        demandFunc = axes.plot(
            lambda x: 1 / (x + 1)**5,
            x_range = [0, 1],
            color = BLUE,
        )
        demandLabel = axes.get_graph_label(demandFunc, "Demand\\,Function")
        demandLabel.move_to(UP * 2 + LEFT * 3)

        supplyFunc = axes.plot(
            lambda x: x**2,
            x_range = [0, 1],
            color = RED,
        )
        supplyLabel = axes.get_graph_label(supplyFunc, "Supply\\,Function", direction = DL * 3 + LEFT * 3)

        labels = axes.get_axis_labels(
            x_label = Tex("Quantity"),
            y_label = Tex("Price"),
        )


        self.play(
            Create(axes, run_time = 2, lag_ratio = 0.1),
            Create(labels, run_time = 2, lag_ratio = 0.1),
        )

        self.play(
            line1.animate.move_to(UP * 3),
            Create(demandFunc, run_time = 2, lag_ratio = 0.1),
            Write(demandLabel),
            Create(supplyFunc, run_time = 2, lag_ratio = 0.1),
            Write(supplyLabel),
        )

        # self.wait()

        t = ValueTracker(0)

        def get_rectangle():
            polygon = Polygon(
                *[
                    axes.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (0.4178, 0.1746)
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(GREEN, opacity = 0.5)
            polygon.set_stroke(YELLOW)
            return polygon

        polygon = always_redraw(get_rectangle)

        dotTrack = ValueTracker(0.4178)
        dot = Dot(axes.i2gp(dotTrack.get_value(), supplyFunc))
        dot.set_z_index(1001)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(dotTrack.get_value(), supplyFunc)
        )

        eqPtLbl = Tex("Equilibrium Point")
        eqPtLbl.move_to(RIGHT + DOWN * 1.3)

        def get_lines():
            return axes.get_lines_to_point(axes.i2gp(dotTrack.get_value(), supplyFunc), color = YELLOW)
        
        lines = always_redraw(get_lines)

        def get_xLab1():
            return MathTex("q_e").next_to(axes.c2p(dotTrack.get_value(), 0), DOWN)

        def get_yLab1():
            return MathTex("p_e").next_to(axes.c2p(0, dotTrack.get_value() ** 2), LEFT)
        
        yLab1 = always_redraw(get_yLab1)
        xLab1 = always_redraw(get_xLab1)
        yLab2 = MathTex("p_s")
        yLab2.next_to(axes.c2p(0, 0.1746), LEFT)
        xLab2 = MathTex("q_s")
        xLab2.next_to(axes.c2p(dotTrack.get_value(), 0), DOWN)

        self.play(
            Create(dot, run_time = 1, lag_ratio = 0.1),
            Write(eqPtLbl, run_time = 1, lag_ratio = 0.1),
            Create(lines, lag_ratio = 0.1),
            Write(yLab1),
            Write(xLab1),
        )
        self.wait()

        supplyFunc.save_state()
        supplyLabel.save_state()
        demandFunc.save_state()
        demandLabel.save_state()

        self.play(
            Uncreate(supplyFunc),
            Unwrite(supplyLabel, run_time = 1, lag_ratio = 0.1),
            Unwrite(eqPtLbl, run_time = 1, lag_ratio = 0.1),
            Transform(yLab1, yLab2),
            Transform(xLab1, xLab2),
        )
        supplyFunc.restore()
        supplyLabel.restore()

        self.wait()

        def get_lineFake():
            return axes.plot(lambda x: dotTrack.get_value()**2, x_range = [0, 1])
            
        lineFake = always_redraw(get_lineFake)

        def get_area0():
            return axes.get_area(demandFunc, [0, 0.4178], color = PURPLE, opacity = 0.5)

        area0 = always_redraw(get_area0)

        will2Spend = Tex("= Willingness to spend", color = PURPLE)
        integral, v_t, dt = formula = MathTex(
            "\\int_0^{q_s}", "demand\\,function (q)", "\\,dq",
            color = BLUE,
        )
        formula.set_color_by_tex("{q_s}", PURPLE)
        formula.set_color_by_tex("dq", PURPLE)

        self.play(
            DrawBorderThenFill(area0),
            Write(formula),
        )

        self.wait()
        will2Spend.next_to(formula, DOWN)
        self.play(
            Write(will2Spend),
        )

        self.wait()

        consSur = Tex("Consumer Surplus", color = RED)
        consSur.move_to(LEFT * 1.6)
        consExp = Tex("Consumer Expenditure", color = GREEN)
        consExp.move_to(DOWN * 2.5 + RIGHT * 2)

        def get_area():
            return axes.get_area(demandFunc, [0, dotTrack.get_value()], bounded_graph = lineFake, color = RED, opacity = 0.5)

        area = always_redraw(get_area)

        area.save_state()

        integral2, v_t2, dt2 = formula2 = MathTex(
            "\\int_0^{q_s}", "{p_s}", "\\,dq",
            color = GREEN,
        ).move_to(DR + RIGHT)
        eq2 = Tex("=", color = GREEN).next_to(formula2, DOWN)
        formula2.set_color_by_tex("{p_s}", BLUE)

        integral3, v_t3, dt3 = formula3 = MathTex(
            "\\int_0^{q_s}", "demand\\,function (q) - {p_s}", "\\,dq",
            color = RED,
        ).move_to(UL)
        eq3 = Tex("=", color = RED).next_to(consSur, LEFT)
        formula3.set_color_by_tex("demand\\,function (q) - {p_s}", BLUE)

        self.play(
            formula.animate.shift(UP + LEFT * 1.53),
            Unwrite(integral, reverse = False),
            Unwrite(dt, reverse = False),
            Unwrite(will2Spend, run_time = 1, lag_ratio = 0.1, reverse = False),
        )

        self.play(
            FadeOut(area0, run_time = 2, lag_ratio = 0.1),
            DrawBorderThenFill(polygon),
            DrawBorderThenFill(area),
            Write(consSur),
            Write(consExp),
            Write(formula2),
            Write(eq2),
            Write(formula3),
            Write(eq3),
        )

        self.wait()
        self.play(
            Unwrite(formula, run_time = 1, lag_ratio = 0.1),
            Unwrite(formula2, run_time = 1, lag_ratio = 0.1),
            Unwrite(eq2, run_time = 1, lag_ratio = 0.1),
            Unwrite(formula3, run_time = 1, lag_ratio = 0.1),
            Unwrite(eq3, run_time = 1, lag_ratio = 0.1),
            Unwrite(consSur, run_time = 1, lag_ratio = 0.1),
            Unwrite(consExp, run_time = 1, lag_ratio = 0.1),
            # Uncreate(polygon),
            FadeOut(area),
            Unwrite(demandLabel, run_time = 1, lag_ratio = 0.1),
            Transform(demandFunc, supplyFunc),
            Write(supplyLabel),
        )
        demandLabel.restore()

        def get_lineFake2():
            return axes.plot(lambda x: dotTrack.get_value()**2, x_range = [0, dotTrack.get_value() + 0.05])

        def get_area2():
            return axes.get_area(supplyFunc, [0, dotTrack.get_value()], bounded_graph = lineFake2, color = LIGHT_PINK, opacity = 0.5)

        def get_area3():
            return axes.get_area(supplyFunc, x_range = [0, dotTrack.get_value()], color = GREEN, opacity = 0.5)
            
        lineFake2 = always_redraw(get_lineFake2)
        area2 = always_redraw(get_area2)
        area3 = always_redraw(get_area3)
        
        proSur = Tex("Producer Surplus", color = LIGHT_PINK)
        proSur.move_to(LEFT * 3.5 + DOWN * 1.5)
        neededRev = Tex("Needed Producer Revenue", color = GREEN)
        neededRev.move_to(DOWN * 2.5 + RIGHT * 2)

        proRev = Tex("Producer Revenue", color = GREEN)
        proRev.move_to(LEFT * 3.5 + DOWN * 1.5)

        integral4, v_t4, dt4 = proRevEqn = MathTex(
            "\\int_0^{q_s}", "{p_s}", "\\,dq",
            color = GREEN,
        ).move_to(UL)
        proRevEqn.set_color_by_tex("{p_s}", RED)
        eq4 = MathTex("=", color = GREEN).next_to(proRevEqn, DOWN)
        gr4 = VGroup(proRevEqn, eq4).arrange(DOWN)
        gr4.shift(LEFT * 3.5)

        self.play(
            Write(proRev, run_time = 1, lag_ratio = 0.1),
        )

        self.play(
            Write(gr4)
        )

        self.wait()

        integral5, v_t5, dt5 = proSurEqn = MathTex(
            "\\int_0^{q_s}", "{p_s} - supply\\,function (q)", "\\,dq",
            color = LIGHT_PINK,
        ).move_to(LEFT * 1.14 + UP * 0.173)
        proSurEqn.set_color_by_tex("{p_s} - supply\\,function (q)", RED)

        integral6, v_t6, dt6 = neededRevEqn = MathTex(
            "\\int_0^{q_s}", "supply\\,function (q)", "\\,dq",
            color = GREEN,
        ).move_to(LEFT * 1.14 + UP * 0.173)
        neededRevEqn.set_color_by_tex("supply\\,function (q)", RED)
        eq6 = Tex("=").set_color(GREEN).next_to(neededRevEqn, DOWN)
        gr6 = VGroup(neededRevEqn, eq6).arrange(DOWN).move_to(DR + RIGHT)

        self.play(
            FadeOut(integral4, run_time = 1, lag_ratio = 0.1),
            Unwrite(dt4, run_time = 1, lag_ratio = 0.1),
            eq4.animate.set_color(LIGHT_PINK),
            Uncreate(polygon),
            ReplacementTransform(proRev, proSur),
            Write(neededRev),
            DrawBorderThenFill(area2),
            DrawBorderThenFill(area3),
            Write(proSurEqn),
            Write(gr6),
        )

        self.wait()

        demandFunc2 = axes.plot(
            lambda x: 1 / (x + 1)**5,
            x_range = [0, 1],
            color = BLUE,
        )
        proSur.set_z_index(100)

        consSur2 = Tex("Consumer Surplus", color = BLUE)
        consSur2.move_to(LEFT * 1.8)
        area.restore()
        area.set_color(BLUE)
        self.play(
            Unwrite(gr4, run_time = 1, lag_ratio = 0.1, reverse = False),
            Unwrite(gr6, run_time = 1, lag_ratio = 0.1, reverse = False),
            Unwrite(proSurEqn, run_time = 1, lag_ratio = 0.1, reverse = False),
            Unwrite(neededRev, run_time = 1, lag_ratio = 0.1, reverse = False),
            FadeOut(area3),
        )

        def get_area4():
            return axes.get_area(demandFunc2, [0, dotTrack.get_value()], bounded_graph = lineFake2, color = BLUE, opacity = 0.5)

        area4 = always_redraw(get_area4)

        self.play(
            Create(lineFake2),
            Create(demandFunc2),
            Write(demandLabel, run_time = 1, lag_ratio = 0.1),
            proSur.animate.move_to(DOWN * 2.5 + RIGHT * 0.7),
            DrawBorderThenFill(area4),
            Write(consSur2, run_time = 1, lag_ratio = 0.1),
        )

        self.wait()
        consumer, cartel = lineCartel = Tex("Consumer", " Cartel").move_to(UP*3)
        self.play(
            TransformMatchingTex(line1, lineCartel),
            proSur.animate.shift(LEFT + DOWN * 0.3),
            dotTrack.animate.set_value(0.3),
        )

        self.wait()

        self.play(
            AnimationGroup(
                Unwrite(lineCartel),
                Unwrite(labels),
                Unwrite(supplyLabel),
                Unwrite(demandLabel),
                Unwrite(proSur, run_time = 1, lag_ratio = 0.1),
                Unwrite(consSur2, run_time = 1, lag_ratio = 0.1),
                Uncreate(lineFake2, reversed = False),
                Uncreate(area4),
                Uncreate(area2),
                Uncreate(lines),
                Uncreate(dot),
                Uncreate(demandFunc2),
                Uncreate(demandFunc),
                Unwrite(xLab1),
                Unwrite(yLab1),
                Uncreate(axes),
                lag_ratio = 0.2
            )
        )
        
        self.wait()