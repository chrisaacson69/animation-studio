from manim import *
class TestScene(Scene):
    def construct(self):
        text = Text('Hello from RunPod!', font_size=48, color=BLUE)
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.scale(1.5).set_color(YELLOW))
        self.wait(1)
