from shutil import move
from tkinter import CENTER
from typing_extensions import runtime
from venv import create
from manim import *
import numpy as np

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