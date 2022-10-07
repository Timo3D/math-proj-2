from manim import *
import numpy as np

class GraphExample(Scene):
    def construct(self):
        ax = Axes((-3, 10), (-1, 8))
        
        ax.add_coordinates()

        curve = ax.plot(lambda x: 2 * np.sin(x))

        # self.add(ax, curve)
        self.play(
            Create(ax, run_time=3, lag_ratio=0.1),
            Create(curve, run_time=3, lag_ratio=0.1)
        )

        area = ax.get_area(graph=curve, x_range=(0,2))

        self.play(
            DrawBorderThenFill(area)
        )
        self.wait(1)