from GUI.app import App

from algorithms.rail_fence import RailFence
from algorithms.example_a import ExampleA
from algorithms.example_b import ExampleB
from algorithms.example_c import ExampleC
from algorithms.ceasar import Ceasar
from algorithms.vigenere import Vigenere

if __name__ == "__main__":
    app = App([
        RailFence(),
        ExampleA(),
        ExampleB(),
        ExampleC(),
        Ceasar(),
        Vigenere()])

    app.mainloop()