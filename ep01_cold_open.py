"""
Episode 1 Cold Open — v3, +4s in first section to sync with voiceover.
Voiceover duration: ~33.5s
"""
from manim import *

class ColdOpen(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # --- Phase 1: Quotes on black (0:00 - ~12s) ---
        # +4s spread across the three quotes and gaps
        
        t1 = Text(
            "\"That's not logical.\"",
            font_size=56, color=WHITE, font="Sans"
        )
        self.play(FadeIn(t1, shift=UP * 0.2), run_time=0.6)
        self.wait(3.5)  # was 2.5
        self.play(FadeOut(t1), run_time=0.4)
        self.wait(0.5)  # was 0.3
        
        t2 = Text(
            "\"Your argument is contradictory.\"",
            font_size=56, color=WHITE, font="Sans"
        )
        self.play(FadeIn(t2, shift=UP * 0.2), run_time=0.6)
        self.wait(3.5)  # was 2.5
        self.play(FadeOut(t2), run_time=0.4)
        self.wait(0.5)  # was 0.3
        
        t3 = Text(
            "\"You're being irrational.\"",
            font_size=56, color=WHITE, font="Sans"
        )
        self.play(FadeIn(t3, shift=UP * 0.2), run_time=0.6)
        self.wait(3.5)  # was 2.5
        self.play(FadeOut(t3), run_time=0.4)
        
        # --- Phase 2: Empty black during "obvious settled thing" ---
        self.wait(6.5)
        
        # --- Phase 3: Questions timed to voiceover ---
        self.wait(2.0)
        
        # "What IS logic?" synced to ~24s
        q1 = Text(
            "What IS logic?",
            font_size=52, color="#f39c12", font="Sans"
        )
        self.play(Write(q1), run_time=1.0)
        self.wait(3.5)
        
        # "Where did it come from?"
        q2 = Text(
            "Where did it come from?",
            font_size=44, color="#f39c12", font="Sans"
        ).next_to(q1, DOWN, buff=0.6)
        self.play(Write(q2), run_time=0.8)
        self.wait(2.0)
        
        # "Is it even ONE thing?"
        q3 = Text(
            "Is it even ONE thing?",
            font_size=44, color="#f39c12", font="Sans"
        ).next_to(q2, DOWN, buff=0.6)
        self.play(Write(q3), run_time=0.8)
        self.wait(2.5)
        
        self.play(
            FadeOut(q1), FadeOut(q2), FadeOut(q3),
            run_time=0.6
        )
        self.wait(0.3)
        
        # --- Phase 4: Title card ---
        title = Text(
            "You Don't Know\nWhat Logic Is",
            font_size=72, color=WHITE, font="Sans",
            line_spacing=1.3
        )
        self.play(FadeIn(title, scale=1.1), run_time=1.2)
        self.wait(0.3)
        
        line = Line(
            title.get_left() + DOWN * 0.3,
            title.get_right() + DOWN * 0.3,
            color="#f39c12", stroke_width=3
        )
        self.play(Create(line), run_time=0.5)
        self.wait(2.0)
        
        self.play(FadeOut(title), FadeOut(line), run_time=0.8)
