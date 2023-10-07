from manim import *


class Squarerootdemo(Scene):
    def construct(self):
        text = Tex(r'How indians approximated $\sqrt{2}$').shift(UP*1.5)
        text2 = Tex(r'in the book called Sulva Sutra')
        self.play(Write(text))
        self.play(Write(text2))
        self.wait(1)
        animations = [
            FadeOut(text),
            FadeOut(text2),
        ]
        self.play(AnimationGroup(*animations))
        text = Tex(r'First we take two squares of side 1').shift(UP*2.5)
        square1 = Square().shift(LEFT*2)
        square2 = Square().shift(RIGHT*2)
        animations = [
            Write(text),
            Create(square1),
            Create(square2),
        ]
        self.play(AnimationGroup(*animations))
        self.wait(1.5)
        biggersquare = Square(side_length=2.8284)
        animations = [
            Transform(text, Tex(r'Our objective will be to create a square of area 2').shift(DOWN*2.5)),
            Create(biggersquare, run_time=1.5),
            FadeOut(square1),
            FadeOut(square2),
        ]
        self.play(AnimationGroup(*animations))
        self.wait(1)
        animations = [
            FadeIn(square1),
            FadeIn(square2),
            Uncreate(biggersquare, run_time=0.5)
        ]
        self.play(AnimationGroup(*animations))
        self.wait(1)
        rectangle1 = Rectangle(height=2.0, width=2.0, grid_xstep=2.0/3).shift(LEFT*2)
        animations = [
            square2.animate.set_fill(BLUE, opacity=0.5),
            Transform(square1, rectangle1),
            Transform(text, Tex(r'We will divide into 3 equal columns one of the squares').shift(DOWN*2.5)),
        ]
        self.play(AnimationGroup(*animations))
        self.wait(1)
        