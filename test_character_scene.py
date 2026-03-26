from manim import *

class CharacterDialogue(Scene):
    def construct(self):
        # Load character images
        aristotle = ImageMobject("/workspace/studio/assets/characters/aristotle/base.png")
        socrates = ImageMobject("/workspace/studio/assets/characters/socrates/base.png")
        
        # Scale and position
        aristotle.scale_to_fit_height(4.5)
        socrates.scale_to_fit_height(4.5)
        
        aristotle.to_edge(RIGHT, buff=1)
        socrates.to_edge(LEFT, buff=1)
        
        # Fade in characters
        self.play(FadeIn(socrates, shift=UP*0.5), run_time=1)
        self.play(FadeIn(aristotle, shift=UP*0.5), run_time=1)
        
        # Speech bubble for Socrates
        bubble_s = RoundedRectangle(
            corner_radius=0.3, width=4, height=1.5,
            color=WHITE, fill_color=WHITE, fill_opacity=0.9
        )
        bubble_s.next_to(socrates, UP+RIGHT, buff=0.2)
        
        # Tail triangle pointing to speaker
        tail_s = Triangle(fill_color=WHITE, fill_opacity=0.9, color=WHITE)
        tail_s.scale(0.2)
        tail_s.next_to(bubble_s, DOWN+LEFT, buff=-0.1)
        
        text_s = Text(
            "But what do you\nMEAN by justice?",
            font_size=24, color=BLACK
        )
        text_s.move_to(bubble_s)
        
        self.play(
            FadeIn(bubble_s), FadeIn(tail_s),
            Write(text_s),
            run_time=1.5
        )
        self.wait(2)
        
        # Socrates walks closer (slides toward center)
        self.play(
            socrates.animate.shift(RIGHT * 1.5),
            bubble_s.animate.shift(RIGHT * 1.5),
            tail_s.animate.shift(RIGHT * 1.5),
            text_s.animate.shift(RIGHT * 1.5),
            run_time=1
        )
        
        # Aristotle responds
        self.play(FadeOut(bubble_s), FadeOut(tail_s), FadeOut(text_s))
        
        bubble_a = RoundedRectangle(
            corner_radius=0.3, width=4.5, height=1.5,
            color=WHITE, fill_color=WHITE, fill_opacity=0.9
        )
        bubble_a.next_to(aristotle, UP+LEFT, buff=0.2)
        
        tail_a = Triangle(fill_color=WHITE, fill_opacity=0.9, color=WHITE)
        tail_a.scale(0.2)
        tail_a.next_to(bubble_a, DOWN+RIGHT, buff=-0.1)
        
        text_a = Text(
            "I call this the Organon.\nA tool for correct reasoning.",
            font_size=22, color=BLACK
        )
        text_a.move_to(bubble_a)
        
        self.play(
            FadeIn(bubble_a), FadeIn(tail_a),
            Write(text_a),
            run_time=1.5
        )
        self.wait(2)
        
        # Both fade out
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1)
