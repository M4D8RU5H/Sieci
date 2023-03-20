from GUI.app import App
from algorithms.example_algorithm import ExampleAlgorithm
from algorithms.example_algorithm import ExampleAlgorithm1
from algorithms.example_algorithm import MegaAlgorytm

if __name__ == "__main__":
    app = App([ExampleAlgorithm(), ExampleAlgorithm1(), MegaAlgorytm()])
    app.mainloop()