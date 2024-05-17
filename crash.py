import tkinter as tk

class SystemErrorWindow:
    def __init__(self, remaining):
        self.remaining = remaining
        self.create_window()

    def create_window(self):
        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("System Error")

        # Create a label to display the error message
        self.label = tk.Label(self.root, text="System Error!!!", font=("Arial", 14))
        self.label.pack(padx=20, pady=20)

        # Bind the close event to create a new window if there are remaining windows to create
        if self.remaining > 0:
            self.root.protocol("WM_DELETE_WINDOW", self.create_next_window)

    def create_next_window(self):
        # Create the next window with half the remaining count
        SystemErrorWindow(self.remaining - 1)

if __name__ == "__main__":
    # Number of windows to display
    n = 50

    # Create the first window with all remaining windows
    SystemErrorWindow(n)

    # Start the Tkinter event loop
    tk.mainloop()

