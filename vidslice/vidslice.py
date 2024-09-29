import cv2
import os
from tqdm import tqdm


class VIDSLICE:
    def __init__(self, video_file):
        self.video_file = video_file

    def extract_frames(self):
        save_directory = "../images"

        if not os.path.exists(save_directory):
            os.mkdir(save_directory)
        cap = cv2.VideoCapture(self.video_file)

        while True:
            ret, frame = cap.read()

            frame_count = 0

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            with tqdm(
                total=total_frames,
                desc="Extracting Frames",
                unit="frame",
                ncols=100,
                bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt}[{elapsed}<{remaining}]",
            ) as pbar:
                while ret:
                    if frame_count % int(cap.get(cv2.CAP_PROP_FPS)) == 0:
                        output_file = os.path.join(
                            save_directory, f"{self.video_file}_{frame_count}.jpg"
                        )
                        cv2.imwrite(output_file, frame)

                    pbar.update(1)

                    ret, frame = cap.read()

                    frame_count += 1

            cap.release()
            cv2.destroyAllWindows()
            print("Finished")
            break


if __name__ == "__main__":
    video_file = r"sunny_day.mp4"

    vidslice = VIDSLICE(video_file)

    vidslice.extract_frames()
