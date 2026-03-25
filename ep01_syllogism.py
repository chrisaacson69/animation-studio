"""
Episode 1: The Syllogism Animation
===================================
The centerpiece of Episode 1 — Aristotle's syllogism, words fading to
reveal abstract structure, different examples flowing through.

To run in Google Colab:
    !pip install manim
    !manim -pql ep01_syllogism.py SyllogismScene

To run locally (if Manim works):
    manim -pql ep01_syllogism.py SyllogismScene

Quality flags:
    -ql  = low quality (480p, fast render — use for testing)
    -qm  = medium quality (720p)
    -qh  = high quality (1080p — use for final render)
    -qk  = 4K
"""

from manim import *


class SyllogismScene(Scene):
    """
    The core animation: syllogism content → abstract structure → examples flowing through.
    This is the "3B1B moment" — the abstraction made visible.
    """

    def construct(self):
        # === Color scheme (series-wide) ===
        IDENTITY_BLUE = "#4A90D9"
        NONCONTRADICTION_RED = "#E74C3C"
        EXCLUDED_GREEN = "#2ECC71"
        STRUCTURE_GOLD = "#F39C12"
        FADE_GRAY = "#666666"

        # ============================================================
        # PART 1: The Classic Syllogism (builds line by line)
        # ============================================================

        title = Text("The Syllogism", font_size=42, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Build the syllogism line by line
        line1 = Text("All men are mortal.", font_size=36)
        line2 = Text("Socrates is a man.", font_size=36)
        line3 = Text("Therefore, Socrates is mortal.", font_size=36, color=STRUCTURE_GOLD)

        lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.4)
        lines.move_to(ORIGIN)

        # Horizontal rule above conclusion
        rule = Line(LEFT * 3, RIGHT * 3, color=WHITE)
        rule.next_to(line2, DOWN, buff=0.15)
        line3.next_to(rule, DOWN, buff=0.15)

        self.play(Write(line1), run_time=1.5)
        self.wait(0.3)
        self.play(Write(line2), run_time=1.5)
        self.wait(0.3)
        self.play(Create(rule), run_time=0.5)
        self.play(Write(line3), run_time=1.5)
        self.wait(2)

        # ============================================================
        # PART 2: Words Fade → Abstract Structure Revealed
        # ============================================================

        self.play(FadeOut(title))

        # Create the abstract version (positioned to match)
        abs1 = Text("All  A  are  B.", font_size=36)
        abs2 = Text("C  is  A.", font_size=36)
        abs3 = Text("Therefore,  C  is  B.", font_size=36, color=STRUCTURE_GOLD)

        abs_lines = VGroup(abs1, abs2, abs3).arrange(DOWN, buff=0.4)
        abs_lines.move_to(ORIGIN)

        abs_rule = Line(LEFT * 3, RIGHT * 3, color=STRUCTURE_GOLD)
        abs_rule.next_to(abs2, DOWN, buff=0.15)
        abs3.next_to(abs_rule, DOWN, buff=0.15)

        # Color the variables
        # We'll highlight A, B, C in the abstract version
        a_color = IDENTITY_BLUE
        b_color = NONCONTRADICTION_RED
        c_color = EXCLUDED_GREEN

        # Fade old lines to gray, then transform to abstract
        self.play(
            line1.animate.set_color(FADE_GRAY),
            line2.animate.set_color(FADE_GRAY),
            line3.animate.set_color(FADE_GRAY),
            rule.animate.set_color(FADE_GRAY),
            run_time=0.8
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(line1, abs1),
            ReplacementTransform(line2, abs2),
            ReplacementTransform(line3, abs3),
            ReplacementTransform(rule, abs_rule),
            run_time=2
        )
        self.wait(1)

        # Add a label
        struct_label = Text("The structure is what matters.", font_size=28,
                           color=STRUCTURE_GOLD, slant=ITALIC)
        struct_label.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(struct_label), run_time=1)
        self.wait(2)

        # ============================================================
        # PART 3: Examples Flow Through the Structure
        # ============================================================

        self.play(FadeOut(struct_label))

        # Example 1: Dogs
        ex1_lines = [
            "All dogs are mammals.",
            "Rex is a dog.",
            "Therefore, Rex is a mammal."
        ]

        # Example 2: Numbers
        ex2_lines = [
            "All primes are integers.",
            "7 is a prime.",
            "Therefore, 7 is an integer."
        ]

        # Example 3: Something silly (to show universality)
        ex3_lines = [
            "All cats are fluffy.",
            "Whiskers is a cat.",
            "Therefore, Whiskers is fluffy."
        ]

        for example in [ex1_lines, ex2_lines, ex3_lines]:
            new1 = Text(example[0], font_size=36)
            new2 = Text(example[1], font_size=36)
            new3 = Text(example[2], font_size=36, color=STRUCTURE_GOLD)

            new_group = VGroup(new1, new2, new3).arrange(DOWN, buff=0.4)
            new_group.move_to(ORIGIN)

            new_rule = Line(LEFT * 3, RIGHT * 3, color=STRUCTURE_GOLD)
            new_rule.next_to(new2, DOWN, buff=0.15)
            new3.next_to(new_rule, DOWN, buff=0.15)

            self.play(
                ReplacementTransform(abs1, new1),
                ReplacementTransform(abs2, new2),
                ReplacementTransform(abs3, new3),
                ReplacementTransform(abs_rule, new_rule),
                run_time=1.5
            )
            self.wait(1.5)

            # Set up for next iteration
            abs1, abs2, abs3, abs_rule = new1, new2, new3, new_rule

        # ============================================================
        # PART 4: Return to Abstract and Float Free
        # ============================================================

        # Return to abstract form
        final_abs1 = Text("All  A  are  B", font_size=40, color=WHITE)
        final_abs2 = Text("C  is  A", font_size=40, color=WHITE)
        final_abs3 = Text("Therefore,  C  is  B", font_size=40, color=STRUCTURE_GOLD)

        final_group = VGroup(final_abs1, final_abs2, final_abs3).arrange(DOWN, buff=0.3)
        final_rule = Line(LEFT * 2.5, RIGHT * 2.5, color=STRUCTURE_GOLD)
        final_rule.next_to(final_abs2, DOWN, buff=0.1)
        final_abs3.next_to(final_rule, DOWN, buff=0.1)

        box = SurroundingRectangle(
            VGroup(final_abs1, final_abs2, final_rule, final_abs3),
            color=STRUCTURE_GOLD,
            buff=0.3,
            corner_radius=0.1
        )

        all_final = VGroup(final_abs1, final_abs2, final_rule, final_abs3, box)
        all_final.move_to(ORIGIN)

        self.play(
            ReplacementTransform(abs1, final_abs1),
            ReplacementTransform(abs2, final_abs2),
            ReplacementTransform(abs3, final_abs3),
            ReplacementTransform(abs_rule, final_rule),
            run_time=1.5
        )
        self.play(Create(box), run_time=1)
        self.wait(0.5)

        # Scale down and move to show it as an independent object
        self.play(
            all_final.animate.scale(0.7).to_edge(UP, buff=1),
            run_time=1.5
        )

        # Add the key insight text
        insight = Text(
            "Form independent of content.\nPlug in anything — the structure holds.",
            font_size=28,
            color=WHITE,
            line_spacing=1.3
        )
        insight.to_edge(DOWN, buff=1)

        self.play(FadeIn(insight), run_time=1.5)
        self.wait(3)

        # Final fade
        self.play(
            FadeOut(all_final),
            FadeOut(insight),
            run_time=1.5
        )
        self.wait(0.5)


class ThreeLawsScene(Scene):
    """
    The Three Laws — workspace/results layout.
    Left side: workspace where each law is built (English → structured → symbolic)
    Right side: results column where completed laws stack
    Final: results zoom in centered with cracks.
    """

    def construct(self):
        IDENTITY_BLUE = "#4A90D9"
        NONCONTRADICTION_RED = "#E74C3C"
        EXCLUDED_GREEN = "#2ECC71"
        STRUCTURE_GOLD = "#F39C12"

        title = Text("The Three Laws", font_size=42)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Dividing line — subtle separator between workspace and results
        divider = DashedLine(
            UP * 3, DOWN * 3,
            color=GRAY, stroke_width=1, dash_length=0.1
        ).shift(RIGHT * 3)
        results_label = Text("Results", font_size=20, color=GRAY)
        results_label.next_to(divider, UP).shift(RIGHT * 1.5)

        self.play(Create(divider), FadeIn(results_label), run_time=0.8)

        # Track results as they accumulate on the right
        results_items = []
        result_start_y = 1.5  # top of results column

        # ============================================================
        # LAW 1: IDENTITY (Blue)
        # ============================================================

        # Step 1: Plain English — big, centered in workspace
        eng1 = Text("A thing is what it is.", font_size=38, color=WHITE)
        eng1.move_to(LEFT * 1.5)

        law1_title = Text("Law of Identity", font_size=26, color=IDENTITY_BLUE)
        law1_title.next_to(eng1, UP, buff=0.4)

        self.play(Write(law1_title), run_time=0.8)
        self.play(Write(eng1), run_time=1.5)
        self.wait(1.5)

        # Step 2: Structured English
        struct1 = Text("A  =  A", font_size=48, color=IDENTITY_BLUE, weight=BOLD)
        struct1.move_to(LEFT * 1.5)

        self.play(
            ReplacementTransform(eng1, struct1),
            run_time=1.5
        )
        self.wait(1.5)

        # Step 3: Fade out workspace, fade in result on right
        result1_label = Text("Identity", font_size=18, color=IDENTITY_BLUE)
        result1_formula = Text("A = A", font_size=24, color=IDENTITY_BLUE, weight=BOLD)
        result1 = VGroup(result1_label, result1_formula).arrange(DOWN, buff=0.08)
        result1_box = SurroundingRectangle(result1, color=IDENTITY_BLUE, buff=0.15, corner_radius=0.05)
        result1_group = VGroup(result1, result1_box)
        result1_group.move_to(RIGHT * 5 + UP * result_start_y)

        self.play(
            FadeOut(law1_title),
            FadeOut(struct1),
            run_time=0.8
        )
        self.play(
            FadeIn(result1_group),
            run_time=1
        )
        results_items.append(result1_group)
        self.wait(0.5)

        # ============================================================
        # LAW 2: NON-CONTRADICTION (Red)
        # ============================================================

        # Step 1: Plain English
        eng2 = Text("A thing cannot be both\ntrue and not true.", font_size=36,
                     color=WHITE, line_spacing=1.2)
        eng2.move_to(LEFT * 1.5)

        law2_title = Text("Law of Non-Contradiction", font_size=26, color=NONCONTRADICTION_RED)
        law2_title.next_to(eng2, UP, buff=0.4)

        self.play(Write(law2_title), run_time=0.8)
        self.play(Write(eng2), run_time=1.5)
        self.wait(1.5)

        # Step 2: Structured English
        struct2 = Text("NOT ( P  AND  NOT P )", font_size=36,
                       color=NONCONTRADICTION_RED, weight=BOLD)
        struct2.move_to(LEFT * 1.5)

        self.play(
            ReplacementTransform(eng2, struct2),
            run_time=1.5
        )
        self.wait(1.5)

        # Step 3: Fade out workspace, fade in result on right
        result2_label = Text("Non-Contradiction", font_size=18, color=NONCONTRADICTION_RED)
        result2_formula = Text("NOT (P AND NOT P)", font_size=20,
                               color=NONCONTRADICTION_RED, weight=BOLD)
        result2 = VGroup(result2_label, result2_formula).arrange(DOWN, buff=0.08)
        result2_box = SurroundingRectangle(result2, color=NONCONTRADICTION_RED, buff=0.15, corner_radius=0.05)
        result2_group = VGroup(result2, result2_box)
        result2_group.move_to(RIGHT * 5 + UP * (result_start_y - 1.2))

        self.play(
            FadeOut(law2_title),
            FadeOut(struct2),
            run_time=0.8
        )
        self.play(
            FadeIn(result2_group),
            run_time=1
        )
        results_items.append(result2_group)
        self.wait(0.5)

        # ============================================================
        # LAW 3: EXCLUDED MIDDLE (Green)
        # ============================================================

        # Step 1: Plain English
        eng3 = Text("Either it's true or it's not.\nNo third option.", font_size=36,
                     color=WHITE, line_spacing=1.2)
        eng3.move_to(LEFT * 1.5)

        law3_title = Text("Law of Excluded Middle", font_size=26, color=EXCLUDED_GREEN)
        law3_title.next_to(eng3, UP, buff=0.4)

        self.play(Write(law3_title), run_time=0.8)
        self.play(Write(eng3), run_time=1.5)
        self.wait(1.5)

        # Step 2: Structured English
        struct3 = Text("P   OR   NOT P", font_size=42,
                       color=EXCLUDED_GREEN, weight=BOLD)
        struct3.move_to(LEFT * 1.5)

        self.play(
            ReplacementTransform(eng3, struct3),
            run_time=1.5
        )
        self.wait(1.5)

        # Step 3: Fade out workspace, fade in result on right
        result3_label = Text("Excluded Middle", font_size=18, color=EXCLUDED_GREEN)
        result3_formula = Text("P OR NOT P", font_size=22,
                               color=EXCLUDED_GREEN, weight=BOLD)
        result3 = VGroup(result3_label, result3_formula).arrange(DOWN, buff=0.08)
        result3_box = SurroundingRectangle(result3, color=EXCLUDED_GREEN, buff=0.15, corner_radius=0.05)
        result3_group = VGroup(result3, result3_box)
        result3_group.move_to(RIGHT * 5 + UP * (result_start_y - 2.4))

        self.play(
            FadeOut(law3_title),
            FadeOut(struct3),
            run_time=0.8
        )
        self.play(
            FadeIn(result3_group),
            run_time=1
        )
        results_items.append(result3_group)
        self.wait(1)

        # ============================================================
        # FINAL: Zoom results to center, large
        # ============================================================

        # Fade workspace elements
        self.play(FadeOut(title), FadeOut(divider), FadeOut(results_label), run_time=0.8)

        # Group all results and animate to center + scale up
        all_results = VGroup(*results_items)

        self.play(
            all_results.animate.arrange(DOWN, buff=0.4).move_to(ORIGIN).scale(1.4),
            run_time=2
        )
        self.wait(1)

        # ============================================================
        # THE CRACKS — subtle hairline fractures appear on the boxes
        # ============================================================

        # Find the boxes (they're the SurroundingRectangles inside each group)
        final_box1 = result1_box
        final_box2 = result2_box
        final_box3 = result3_box

        crack1 = Line(
            final_box1.get_corner(UR) + LEFT * 0.2,
            final_box1.get_corner(UR) + LEFT * 0.2 + DOWN * 0.2 + LEFT * 0.1,
            color=WHITE, stroke_width=1.5
        )
        crack2 = Line(
            final_box2.get_corner(DR) + LEFT * 0.4,
            final_box2.get_corner(DR) + LEFT * 0.4 + UP * 0.2 + LEFT * 0.08,
            color=WHITE, stroke_width=1.5
        )
        crack3 = Line(
            final_box3.get_corner(UL) + RIGHT * 0.3,
            final_box3.get_corner(UL) + RIGHT * 0.3 + DOWN * 0.25 + RIGHT * 0.08,
            color=WHITE, stroke_width=1.5
        )

        self.play(
            Create(crack1),
            Create(crack2),
            Create(crack3),
            run_time=2
        )

        subtitle = Text(
            "2,400 years. Still standing. But not unbreakable.",
            font_size=24, color=GRAY, slant=ITALIC
        )
        subtitle.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)


class LightSwitchDimmerScene(Scene):
    """
    The excluded middle visualization:
    Light switch (binary) → Dimmer (continuous)
    """

    def construct(self):
        EXCLUDED_GREEN = "#2ECC71"

        title = Text("Excluded Middle: True or False?", font_size=36, color=EXCLUDED_GREEN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Binary: light switch
        switch_label = Text("Classical Logic", font_size=28)
        switch_label.shift(LEFT * 3 + UP * 1)

        on_box = Rectangle(width=1.2, height=0.6, color=GREEN, fill_opacity=0.8)
        on_text = Text("TRUE", font_size=18, color=WHITE)
        on_group = VGroup(on_box, on_text)

        off_box = Rectangle(width=1.2, height=0.6, color=RED, fill_opacity=0.8)
        off_text = Text("FALSE", font_size=18, color=WHITE)
        off_group = VGroup(off_box, off_text)

        switch = VGroup(on_group, off_group).arrange(DOWN, buff=0.3)
        switch.next_to(switch_label, DOWN, buff=0.3)

        no_middle = Text("Nothing in between.", font_size=20, color=GRAY)
        no_middle.next_to(switch, DOWN, buff=0.3)

        self.play(FadeIn(switch_label), FadeIn(switch), FadeIn(no_middle))
        self.wait(2)

        # Question: "Is that person tall?"
        question = Text('"Is that person tall?"', font_size=32)
        question.shift(RIGHT * 2.5 + UP * 1.5)
        self.play(Write(question))

        # Height lineup — simple rectangles of different heights
        heights = [1.0, 1.3, 1.6, 1.9, 2.2]
        labels = ["5'2\"", "5'6\"", "5'10\"", "6'0\"", "6'4\""]
        people = VGroup()

        for i, (h, label) in enumerate(zip(heights, labels)):
            rect = Rectangle(width=0.4, height=h, color=WHITE, fill_opacity=0.3)
            rect.align_to(ORIGIN, DOWN)
            lbl = Text(label, font_size=14)
            lbl.next_to(rect, DOWN, buff=0.1)
            person = VGroup(rect, lbl)
            people.add(person)

        people.arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        people.shift(RIGHT * 2.5 + DOWN * 0.5)

        self.play(FadeIn(people))
        self.wait(1)

        # Red line trying to find the boundary
        # Position the boundary line to span across the lineup
        # Start at the middle height (5'10" bar)
        line_y_start = people.get_bottom()[1] + 1.6  # roughly at 5'10"
        boundary = DashedLine(
            people.get_left() + LEFT * 0.3,
            people.get_right() + RIGHT * 0.3,
            color=RED
        )
        boundary.set_y(line_y_start)

        tall_label = Text("TALL", font_size=16, color=GREEN).next_to(boundary, UP, buff=0.1)
        not_tall_label = Text("NOT TALL", font_size=16, color=RED).next_to(boundary, DOWN, buff=0.1)

        labels_group = VGroup(tall_label, not_tall_label)

        self.play(Create(boundary), FadeIn(tall_label), FadeIn(not_tall_label))
        self.wait(0.5)

        # Line sweeps through the full range — from the shortest to the tallest
        # Use the actual bar tops as reference points
        bar_tops = [people[i][0].get_top()[1] for i in range(5)]
        # bar_tops[0]=5'2", [1]=5'6", [2]=5'10", [3]=6'0", [4]=6'4"

        stops = [
            (bar_tops[3] + bar_tops[4]) / 2,   # between 6'0" and 6'4" — too high?
            (bar_tops[1] + bar_tops[2]) / 2,   # between 5'6" and 5'10" — too low?
            (bar_tops[2] + bar_tops[3]) / 2,   # between 5'10" and 6'0" — maybe here?
            bar_tops[4] + 0.15,                 # above 6'4" — everyone is "not tall"?
            (bar_tops[0] + bar_tops[1]) / 2,   # between 5'2" and 5'6" — everyone is "tall"?
            (bar_tops[2] + bar_tops[3]) / 2,   # back to the middle — still arbitrary
        ]

        for target_y in stops:
            delta = target_y - boundary.get_y()
            self.play(
                boundary.animate.shift(UP * delta),
                tall_label.animate.shift(UP * delta),
                not_tall_label.animate.shift(UP * delta),
                run_time=0.7
            )
            self.wait(0.3)

        where_line = Text("Where's the line?", font_size=24, color=RED, slant=ITALIC)
        where_line.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(where_line))
        self.wait(2)

        # Transition to dimmer
        self.play(
            *[FadeOut(mob) for mob in [question, people, boundary,
              tall_label, not_tall_label, where_line]],
            run_time=1
        )

        # Dimmer: continuous gradient
        dimmer_label = Text("Fuzzy Logic", font_size=28)
        dimmer_label.shift(RIGHT * 3 + UP * 1)

        # Gradient bar
        gradient = Rectangle(width=4, height=0.6, color=WHITE)
        gradient.shift(RIGHT * 3 + DOWN * 0.3)

        # Fill with gradient effect (approximate with many thin rectangles)
        gradient_bars = VGroup()
        n_bars = 40
        for i in range(n_bars):
            t = i / n_bars
            color = interpolate_color(RED, GREEN, t)
            bar = Rectangle(
                width=4 / n_bars, height=0.6,
                color=color, fill_opacity=0.8,
                stroke_width=0
            )
            bar.move_to(gradient.get_left() + RIGHT * (4 * t + 2 / n_bars))
            gradient_bars.add(bar)

        false_label = Text("0", font_size=20, color=RED)
        false_label.next_to(gradient, LEFT, buff=0.2)
        true_label = Text("1", font_size=20, color=GREEN)
        true_label.next_to(gradient, RIGHT, buff=0.2)

        dimmer_note = Text("Truth is a spectrum, not a switch.", font_size=20, color=GRAY)
        dimmer_note.next_to(gradient_bars, DOWN, buff=0.4)

        self.play(
            FadeIn(dimmer_label),
            FadeIn(gradient_bars),
            FadeIn(false_label),
            FadeIn(true_label),
            FadeIn(dimmer_note),
            run_time=2
        )
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
