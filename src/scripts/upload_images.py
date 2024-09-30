from config import CONFIG
from src.controllers.ImageController import ImageController

if __name__ == "__main__":
    print("Starting Image Upload Process")

    IMAGE_DIR = CONFIG['data'].get('image_dir')
    print(IMAGE_DIR)

    image_controller = ImageController(CONFIG)
    image_controller.upload_images(IMAGE_DIR)

    print("Image Upload Process Completed")
