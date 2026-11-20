#task automation with python scripts


import tkinter as tk

from gui.Dashboard import SmartTaskDashboard


def main():

    root = tk.Tk()

    app = SmartTaskDashboard(root)

    root.mainloop()


if __name__ == "__main__":
    main()
