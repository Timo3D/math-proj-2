from typing_extensions import runtime
from venv import create
from manim import *
import numpy as np

class RiemannSums(Scene):
    def construct(self):
        title = Tex("Riemann Sums")
        subtitle = Tex("0-4?")
        title.move_to(UP * 3 + RIGHT * 4.5)
        subtitle.next_to(title, DOWN)

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinates()
        graph = axes.plot(lambda x: -0.5*x**3 + 2*x**2 + 2)
        graph.set_color(YELLOW)
        self.play(
            Write(title),
            Write(subtitle),
            Create(axes, run_time = 3, lag_ratio = 0.1),
            Create(graph, run_time = 3, lag_ratio = 0.1)
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