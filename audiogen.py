#!/usr/bin/python3

from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class Music:
    def __init__(self, window, video_title):
        self.window = window
        self.video_title = video_title
        self.window.title(video_title)
        self.window.geometry("600x400")
        self.video = None
        self.playing = False
        self.paused = False
        self.playback_time = 0
        # Create buttons
        self.load_button = tk.Button(
            self.window, text="Load video", command=self.load_video
        )
        self.load_button.pack(pady=20)
        self.play_button = tk.Button(
            self.window, text="Play Audio", command=self.play_audio
        )
        self.play_button.pack(pady=20)
        self.pause_button = tk.Button(
            self.window, text="Pause Audio", command=self.pause_audio
        )
        self.pause_button.pack(pady=20)
        self.stop_button = tk.Button(
            self.window, text="Stop Audio", command=self.stop_audio
        )
        self.stop_button.pack(pady=20)
        self.exit_button = tk.Button(self.window, text="Exit", command=self.exit)
        self.exit_button.pack(pady=20)

    def load_video(self):
        # Ask the user to select a video file
        video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if video_path:
            mixer.music.load(video_path)
            print("Audio loaded.")

    def play_audio(self):
        if self.paused:
            mixer.music.unpause()

        else:
            mixer.music.play(-1)

    def pause_audio(self):
        if self.playing:
            self.playing = False
            self.paused = True

        mixer.music.pause()

    def stop_audio(self):
        self.playing = False
        self.paused = False
        mixer.music.stop()
        print("Audio Stopped")

    def exit(self):
        self.window.quit()
        self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    music = Music(root, "Audio Player")
    root.mainloop()
