import sys, os
from PIL import Image, ImageOps


def main():
    ext_list = [".jpg", ".jpeg", ".png"]
    
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    ext1 = os.path.splitext(sys.argv[1].strip().lower())
    ext2 = os.path.splitext(sys.argv[2].strip().lower())

    if (ext1[1] not in ext_list) or (ext2[1] not in ext_list):
        sys.exit("Invalid input")
    elif ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")
    else:
        try:
            adjust_image(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            sys.exit("No such File")


def adjust_image(input_img, output_img):
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = Image.open(input_img)
    resized_photo = ImageOps.fit(photo, size)
    resized_photo.paste(shirt, mask=shirt)
    resized_photo.save(output_img)


if __name__ == "__main__":
    main()