#!/usr/bin/python3
import sys
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


class Video:
    def __init__(self, window, window_title):
        self.vid_capture = cv2.VideoCapture("Sasuke.mp4")
        self.window = window
        self.window.title(window_title)
        self.window_height = 1080

        self.window_width = 1920
        self.screenheight = window.winfo_screenheight()
        self.screenwidth = window.winfo_screenwidth()

        self.alignstr = "%dx%d+%d+%d" % (
            self.window_width,
            self.window_height,
            (self.screenwidth - self.window_width) / 2,
            (self.screenheight - self.window_height) / 2,
        )
        self.window.geometry(self.alignstr)

        self.canvas = tk.Canvas(
            window, width=self.window_width, height=self.window_height
        )

        self.canvas.pack()

        self.photo = None

        if not self.vid_capture:
            print("Error Opening The File")

        self.vid_play()

    def vid_play(self):
        ret, frame = self.vid_capture.read()

        if ret:
            frame = cv2.resize(frame, (1920, 1080))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            current_frame = np.asarray(frame)
            print(current_frame)

            self.window.after(30, self.vid_play)

        else:
            self.vid_capture.release()

    def __del__(self):
        if self.vid_capture.isOpened():
            self.vid_capture.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    window = tk.Tk()
    app = Video(window, "Anime Watch")
    window.mainloop()
