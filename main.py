from venv import create
from manim import *
import numpy as np

class GraphExample(Scene):
    def construct(self):
        ax = Axes((-3, 10), (-1, 8))
        ax.add_coordinates()
        curve = ax.plot(lambda x: -0.5*x**3 + 2*x**2 + 1)
        area = ax.get_area(graph=curve, x_range=(0,2))
        self.play(
            Create(ax, run_time=3, lag_ratio=0.1),
            Create(curve, run_time=3, lag_ratio=0.1),
        )

        self.play(
            Create(area, lag_ratio=0.5)
        )

        self.wait(1)

class RiemannSums(Scene):
    def construct(self):
        title = Tex("Riemann Sums")
        title.move_to(UP * 3 + RIGHT * 4.5)

        ax = Axes((-3, 10), (-1, 8))
        ax.add_coordinates()
        curve = ax.plot(lambda x: -0.5*x**3 + 2*x**2 + 2)

        self.play(
            Write(title),
            Create(ax, run_time=3, lag_ratio=0.1),
            Create(curve, run_time=3, lag_ratio=0.1),
        )
        
        riemannSettings = {
            "x_min": 0,
            "x_max": 4,
            "fill_opacity": 0.75,
            "stroke_width": 0,
        }

        iterations = 6

        self.rect_list = self.get_riemann_rectangles_list(curve, iterations, start_color = PURPLE, end_color = ORANGE, **riemannSettings)

        flat_rects = self.get_riemann_rectangles(dx = 0.25, start_color = invert_color(PURPLE), end_color = invert_color(ORANGE), **riemannSettings)

        rects = self.rect_list[0]

        self.transform_between_riemann_rects(flat_rects, rects, replace_mobject_with_target_in_scene = True, run_time = 3)
        self.wait(1)