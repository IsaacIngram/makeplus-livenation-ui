import tkinter as tk


class LightControl(tk.Canvas):

    id: int
    
    def __init__(self, master, id: int, width: int, height: int, background: str) -> None:
        """
        Create new light control
        """
        self.id = id
        # Initialize Tkinter Canvas
        super().__init__(master)
        # Configure properties
        self.config(
            width=width, # Set width
            height=height, # Set height
            bd=0, # Remove border
            highlightthickness=0, # Remove highlight
            background=background # Set background
        )
        
        # Create all buttons
        open_button = LightControlButton(self, "Open skylight %s" % str(self.id), self.open_button_callback)
        diffuse_button = LightControlButton(self, "Diffuse skylight %s" % str(self.id), self.diffuse_button_callback)
        close_button = LightControlButton(self, "Close skylight %s" % str(self.id), self.close_button_callback)

        # Add all buttons to window
        self.create_window(width*0.5, 50, window=open_button, anchor='n', width=width-(0.125*width), height=50)
        self.create_window(width*0.5, 150, window=diffuse_button, anchor='n', width=width-(0.125*width), height=50)
        self.create_window(width*0.5, 250, window=close_button, anchor='n', width=width-(0.125*width), height=50)

    def test_button_callback(self):
        print("Button %s pressed" % str(self.id))

    def open_button_callback(self):
        print("Called function to open skylight %s" % str(self.id))

    def diffuse_button_callback(self):
        print("Called function to diffuse skylight %s" % str(self.id))

    def close_button_callback(self):
        print("Called function to close skylight %s" % str(self.id))
        
class LightControlButton(tk.Button):

    def __init__(self, master, text: str, command) -> None:
        """
        Create new light control button

        Params:
        master: Canvas this button belongs to
        text: Text to go on button
        command: Function callback for button press
        """
        # Initialize Tkinter Button
        super().__init__(master)
        # Configure properties
        self.config(
            bd=0,
            highlightthickness=0,
            text=text,
            command=command
        )
