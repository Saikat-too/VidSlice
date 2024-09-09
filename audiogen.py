#!/usr/bin/python3

from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog


class Music:
    def __init__(self, window, video_title):
        self.window = window
        self.video_title = video_title 
        self.window.title(video_title)
        self.audio = None  # Initialize audio attribute
        
        # Create buttons
        self.load_button = tk.Button(self.window, text="Load video", command=self.load_video)
        self.load_button.pack(pady=20)
        self.play_button = tk.Button(self.window, text="Play Audio", command=self.play_audio)
        self.play_button.pack(pady=20)
    
    def load_video(self):
        # Ask the user to select a video file
        video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if video_path:
            video = VideoFileClip(video_path)
            self.audio = video.audio
            print("Audio loaded.")
    
    def play_audio(self):
        if self.audio:
            self.audio.preview()
        else:
            print("No audio loaded.")

if __name__ == "__main__":
    root = tk.Tk()
    music = Music(root, "Audio Player")
    root.mainloop()
