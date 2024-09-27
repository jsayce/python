from tkinter import *
window = Tk()
canvas = Canvas(window, width=2000, height=1500)
canvas.pack()
squares = 100
for squarenumber in range(squares):
    blue_value = max(0, 255 - squarenumber * 4)
    green_value = min(255, squarenumber * 4)
    color = f'#{0:02x}{green_value:02x}{blue_value:02x}'
    canvas.create_rectangle(10 + squarenumber * 10, 10 + squarenumber * 10, 200 + squarenumber * 10, 200 + squarenumber * 10, fill=color)
# for squarenumber in range(squares):
#     red_value = max(0, 255 - squarenumber * 4)
#     green_value = min(255, squarenumber * 4)
#     color = f'#{0:02x}{green_value:02x}{blue_value:02x}'
#     canvas.create_rectangle(10 + squarenumber * 10, 10 + squarenumber * 10, 200 + squarenumber * 10, 200 + squarenumber * 10, fill=color)
window.mainloop()
