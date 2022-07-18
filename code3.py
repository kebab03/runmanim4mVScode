from manim import *
from pathlib import Path
import os
print("HELOO")
FLAGS = f"-pqm"
SCENE = "CreateCircle"

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    print(script_name)
    # 
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
    # os.system(f"manim {C:\Users\user\Desktop\manid\code3.py}{SCENE}{FLAGS}")