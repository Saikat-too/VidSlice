#!/usr/bin/python3

from types import FrameType
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


class Video:
    def __init__(self, window, window_title, window_height, window_width):
        self.window = window
        self.window.title(window_title)
        self.window_height = window_height
        self.window_width = window_width

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
            window, width=self.window_width - 160, height=self.window_height - 120
        )

        self.canvas.pack()

        self.photo = None

    def vid_play(self):
        vid_capture = cv2.VideoCapture("test.mkv")

        if not vid_capture.isOpened():
            print("Error Opening The File")

        else:
            fps = vid_capture.get(cv2.CAP_PROP_FPS)
            print("Frame Per  Second : ", fps, "FPS")
            frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
            print("Frame Count : ", frame_count)

            while vid_capture.isOpened():
                ret, frame = vid_capture.read()
                print(FrameType)
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                    self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
                    current_frame = np.asarray(frame)
                    print(current_frame)

                    key = cv2.waitKey(20)

                    if key == ord("q"):
                        break

                else:
                    break

        vid_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    window = tk.Tk()
    app = Video(window, "Anime Watch", 600, 800)
    window.mainloop()
