import tkinter as tk
from tkinter import filedialog
# import cv2

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.video_path = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Video Player")
        self.label.pack()
        
        self.button = tk.Button(self.root, text="Open Video", command=self.open_video)
        self.button.pack()
        
        self.button = tk.Button(self.root, text="Play Video", command=self.play_video)
        self.button.pack()
        