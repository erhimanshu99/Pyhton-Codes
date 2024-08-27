import pyfiglet
def create_text_with_heart(name):
    custom_font = pyfiglet.Figlet(font='normal')
    stylized_text = custom_font.renderText(name)
    heart = " ❤️"
    text_with_heart = stylized_text + heart
    return text_with_heart
name = "Rashmi"
result = create_text_with_heart(name)
print(result)
