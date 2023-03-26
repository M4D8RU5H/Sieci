from GUI.app import App
from algorithms.rail_fence import RailFence

if __name__ == "__main__":
    app = App([RailFence()])
    app.mainloop()