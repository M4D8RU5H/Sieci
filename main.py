from GUI.app import App

from algorithms.rail_fence import RailFence
from algorithms.example_a import ExampleA

if __name__ == "__main__":
    app = App([
        RailFence(),
        ExampleA()])

    app.mainloop()