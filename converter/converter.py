import cv2

# Для импорта (товаров с Китая) пропиши ***pip install opencv-python*** ################
##### Для теста (бездрожжевого) пропиши в терминал эту команду #########################
# python converter/converter.py converter/media/image.png converter/media/video.mp4 20 #
########################################################################################

def create_video_from_image(image_path, output_path, duration, fps=1):
    image = cv2.imread(image_path)

    height, width, layers = image.shape

    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for _ in range(num_frames):
        video.write(image)

    video.release()



if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python create_video.py <input_image> <output_video> <duration> <fps>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_video = sys.argv[2]
    duration = float(sys.argv[3])
    fps = 5

    create_video_from_image(input_image, output_video, duration, fps)
