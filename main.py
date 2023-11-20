import tkinter as tk
from light_control import LightControl

# Matches 7in Raspberry Pi screen dimensions
window_width = 800
window_height = 480

num_controls = 4

def setup_window():
    # Create window
    root = tk.Tk()
    root.title('Skylight Control')
    root.geometry(f'{window_width}x{window_height}')
    root.configure(bg='white')

    # List of colors to use
    background_list = ['red', 'purple', 'pink', 'blue', 'green', 'orange']

    # Create x 
    for i in range(num_controls):
        control = LightControl(
            root, # master
            i+1, # id
            window_width//num_controls, # width
            window_height, # height
            background_list[i%len(background_list)] # background color
            )
        control.grid(row=0, column=i, padx=0, pady=0)

    # Start mainloop
    root.mainloop()

if __name__ == "__main__":
    setup_window()