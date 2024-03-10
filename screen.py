import tkinter as tk

class FirstScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="First Screen")
        label.pack(pady=10)

        button = tk.Button(self, text="Go to Second Screen", command=lambda: controller.show_frame(SecondScreen))
        button.pack(pady=10)

class SecondScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Second Screen")
        label.pack(pady=10)

        button = tk.Button(self, text="Go to First Screen", command=lambda: controller.show_frame(FirstScreen))
        button.pack(pady=10)

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstScreen, SecondScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x200")
    app.title("Tkinter Screen Navigation Example")
    app.mainloop()
