from tkinter import *
window = Tk()
canvas = Canvas(window, width=2000, height=1500)
canvas.pack()
squares = 50
for squarenumber in range(squares):
    blue_value = max(0, 255 - squarenumber * 5)
    green_value = min(255, squarenumber * 5)
    color = f'#{0:02x}{green_value:02x}{blue_value:02x}'
    canvas.create_rectangle(10 + squarenumber * 10, 10 + squarenumber * 10, 200 + squarenumber * 10, 200 + squarenumber * 10, fill=color)
for squarenumber in range(squares):
    red_value = min(0, 255 - squarenumber * 5)
    green_value = max(255, squarenumber * 5)
    blue_value = max(0, 255 - squarenumber * 5)
    color = f'#{red_value:02x}{green_value:02x}{blue_value:02x}'
    canvas.create_rectangle(510 + squarenumber * 10, 10 + squarenumber * 10, 700 + squarenumber * 10, 200 + squarenumber * 10, fill=color)
for squarenumber in range(squares):
    red_value = max(0, squarenumber * 5)
    green_value = max(0, squarenumber * 5)
    blue_value = max(0, squarenumber * 5)
    color = f'#{255:02x}{green_value:02x}{0:02x}'
    canvas.create_rectangle(10 + squarenumber * 10, 510 - squarenumber * 10, 200 + squarenumber * 10, 700 - squarenumber * 10, fill=color)
window.mainloop()
