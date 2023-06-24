###############################################################################
#                                  IMPORTS
###############################################################################

from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

###############################################################################
#                                  FONTS
###############################################################################

AmountWon = ImageFont.truetype("fonts/FontsFree-Net-Proxima-Nova-Bold.otf", 45)
MainBet = ImageFont.truetype("fonts/FontsFree-Net-Proxima-Nova-Bold.otf", 55)
AmountWagered = ImageFont.truetype( "fonts/FontsFree-Net-proxima_nova_reg-webfont.ttf", 45)
BetDescription2 = ImageFont.truetype("fonts/FontsFree-Net-Proxima-Nova-Cond-Reg.otf", 40)
ProximaNova = ImageFont.truetype("fonts/FontsFree-Net-proxima_nova_reg-webfont.ttf",43)
ProximaNovaThin = ImageFont.truetype("fonts/FontsFree-Net-Proxima-Nova-Cond-Reg.otf",40)


###############################################################################
#                       IMAGE CANVAS & Tk DEFAULTS
###############################################################################

original_image = Image.open("SingleTemplate.jpg").convert("RGBA")
image_to_draw_on = original_image.copy() 
draw = ImageDraw.Draw(image_to_draw_on)

root = Tk()
root.title("🎰💰Fanduel Individual BetSlip Maker by Connor Saunders")

canvas_width = image_to_draw_on.width
canvas_height = image_to_draw_on.height
canvas = Canvas(root, width=canvas_width, height=canvas_height)
tk_image = ImageTk.PhotoImage(image_to_draw_on)
canvas_image = canvas.create_image(0, 0, anchor=NW, image=tk_image)
canvas.pack()


button = Button(None)
keys = button.keys()

for key in keys:
    print(key)

###############################################################################
#                               SAVE IMAGE
###############################################################################

def save_image():
    global image_to_draw_on
    file_name = "Bet_Slip.png"
    image_to_draw_on.save(file_name)
    print(f"Image saved as {file_name} in directory: {os.getcwd()}")

###############################################################################
#                               DECLARE FIELDS
###############################################################################
save_button = Button(root, text="Save image", command=save_image, font=('Helvetica', '20'))
save_button.configure(highlightbackground='yellow')
save_button.place(x=800, y=50)



main_bet = Entry(root)
main_bet.place(x=400, y=210)
main_bet.insert(0, "Under 255.5") 

bet_description = Entry(root)
bet_description.place(x = 600, y = 260)
bet_description.insert(0, "ALTERNATE TOTAL POINTS") 

sub_bet = Entry(root)
sub_bet.place(x = 900, y = 375)
sub_bet.insert(0, "Minnesota Timberwolves @ Denver Nuggets") 

amount_wagered = Entry(root)
amount_wagered.place(x = 50, y = 550)
amount_wagered.insert(0, "$5") 

entry_amount_won = Entry(root)
entry_amount_won.place(x=1400, y=550)
entry_amount_won.insert(0, "$40.00")

bet_id = Entry(root)
bet_id.place(x=300, y=660)
bet_id.insert(0,"0/1030095/0000111")

date_placed = Entry(root)
date_placed.place(x=1400, y=660)
date_placed.insert(0, "2/11/2023 6:01PM ET")

bet_odds = Entry(root)
bet_odds.place(x=1400, y=300)
bet_odds.insert(0, "+3000")

###############################################################################
#                               ON KEYS
###############################################################################

def on_key(event):
    global canvas_image, tk_image, image_to_draw_on, draw
    image_to_draw_on = original_image.copy()

    draw = ImageDraw.Draw(image_to_draw_on)
    draw.text((1400, 465), entry_amount_won.get(), fill=(83, 173, 93), font=AmountWon)
    draw.text((60, 200), main_bet.get(), fill=(75, 78, 80), font=MainBet)
    draw.text((55, 465), amount_wagered.get(), fill=(75, 78, 80), font=AmountWagered)
    draw.text((55, 355), sub_bet.get(), fill=(75, 78, 80), font=ProximaNova)
    draw.text((1453, 200), bet_odds.get(), fill=(75, 78, 80), font=MainBet)


    bet_id_text = bet_id.get()

    for x in range(0, len(bet_id_text)):
        if bet_id_text[x] == "/":
            draw.text((190 + (x * 21) + 2, 615), bet_id_text[x], fill=(131, 142, 148), font=ProximaNovaThin)
        else:
            draw.text((190 + (x * 21), 615), bet_id_text[x], fill=(131, 142, 148), font=ProximaNovaThin)

    bet_description_text = bet_description.get()

    draw.text((55, 265), bet_description_text, fill=(131, 142, 148), font=BetDescription2)
        
    date_placed_text = date_placed.get()

    for x in range(0, len(date_placed_text)):
        if date_placed_text[x] == "/" or date_placed_text[x] == ":":
            draw.text((1213 + (x * 20) + 3, 616), date_placed_text[x], fill=(131, 142, 148), font=ProximaNovaThin)
        else:
            draw.text((1213 + (x * 20), 616), date_placed_text[x], fill=(131, 142, 148), font=ProximaNovaThin)

    canvas.delete(canvas_image)
    tk_image = ImageTk.PhotoImage(image_to_draw_on)
    canvas_image = canvas.create_image(0, 0, anchor=NW, image=tk_image)

###############################################################################
#                               BUILDS
###############################################################################
root.bind("<Key>", on_key, add='+')

on_key(None)
root.mainloop()

'''
    for x in range(0, len(bet_description_text)):
        if bet_description_text[x] in Vowels:
            draw.text((55 + (x * 23) - 1, 265), bet_description_text[x], fill=(131, 142, 148), font=BetDescription2)
        elif bet_description_text[x] == "I" or bet_description_text[x] == "i":
            draw.text((55 + (x * 23)+5, 265), bet_description_text[x], fill=(131, 142, 148), font=BetDescription2)
        elif bet_description_text[x] == "W":
            draw.text((55 + (x * 23)-5, 265), bet_description_text[x], fill=(131, 142, 148), font=BetDescription2)
            filler = filler + 3
        elif bet_description_text[x] == " ":
            draw.text((55 + (x * 23) - 7, 265), bet_description_text[x], fill=(131, 142, 148), font=BetDescription2)
        else:
            draw.text((55 + (x * 23), 265), bet_description_text[x], fill=(131, 142, 148), font=BetDescription2)
'''