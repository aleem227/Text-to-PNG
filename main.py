from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text):

    font_size = 60
    font = ImageFont.load_default()  


    temp_img = Image.new("RGB", (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    temp_font = ImageFont.truetype("times.ttf", font_size)  # Times New Roman-like font

    text_width, text_height = temp_draw.textsize(text, font=temp_font)


    padding = 20
    width = text_width + padding
    height = text_height + padding


    img = Image.new("RGB", (width, height), (255, 255, 255))  # White color in RGB


    draw = ImageDraw.Draw(img)


    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2


    draw.text((text_x, text_y), text, fill="black", font=temp_font)


    img.save("text_image.png")


user_text = input("Enter the text you want in the image: ")


create_image_with_text(user_text)
