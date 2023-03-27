from GUI.app import App
from algorithms.rail_fence import RailFence
from algorithms.ceasar import Ceasar
from algorithms.vigenere import Vigenere

if __name__ == "__main__":
    app = App([Vigenere()])
    app.mainloop()
