from metrics import PSNR
from vectot_quantization.image import load_image, save_image


def add_noise(original_image):
    noise_image = original_image & 254
    return noise_image


if __name__ == "__main__":
    img = load_image("balloon.bmp")
    img_noise = add_noise(img)

    save_image(img_noise, "balloon_noise.bmp")
    print(f"PSNR: {PSNR(img, img_noise)}")
