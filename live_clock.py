"""A simple live digital clock built with Python's standard library."""

import tkinter as tk
from datetime import datetime
from tkinter import ttk


class LiveClock(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Live Clock")
        self.geometry("360x150")
        self.resizable(False, False)

        container = ttk.Frame(self, padding=20)
        container.pack(expand=True, fill="both")

        self.time_label = ttk.Label(
            container,
            font=("Segoe UI", 32, "bold"),
            anchor="center",
        )
        self.time_label.pack(expand=True, fill="both")

        self.date_label = ttk.Label(
            container,
            font=("Segoe UI", 12),
            anchor="center",
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self) -> None:
        now = datetime.now()
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.date_label.config(text=now.strftime("%A, %B %d, %Y"))
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    LiveClock().mainloop()
