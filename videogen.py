#!/usr/bin/python3

import cv2


def vid_play():
    vid_capture = cv2.VideoCapture("test.mkv")

    if not vid_capture.isOpened():
        print("Error Opening The File")

    else:
        fps = vid_capture.get(5)
        print("Frame Per  Second : ", fps, "FPS")

        frame_count = vid_capture.get(7)
        print("Frame Count : ", frame_count)

        while vid_capture.isOpened():
            ret, frame = vid_capture.read()
            if ret:
                cv2.imshow("Frame", frame)

                key = cv2.waitKey(20)

                if key == ord("q"):
                    break

                else:
                    break

    vid_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    vid_play()
