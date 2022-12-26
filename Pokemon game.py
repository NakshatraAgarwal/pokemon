from tkinter import * 
from PIL import ImageTk, Image
import random
root = Tk()
root.geometry("600x600")
root.title("Pokemon Game")
root.configure( background = "cyan")


name1_l = Label(root, text = "Player 1", fg = "black", bg = 'red')
name1_l.place(relx = 0.1, rely = 0.3, anchor = CENTER)

name2_l = Label(root, text = "Player 2", fg = "black", bg = 'red')
name2_l.place(relx = 0.9, rely = 0.3, anchor = CENTER)

img1 = ImageTk.PhotoImage(Image.open("abra.jpg"))
img2 = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img3 = ImageTk.PhotoImage(Image.open("charmender.jpg"))
img4 = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
img5 = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img6 = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img7 = ImageTk.PhotoImage(Image.open("meowth.jpg"))
img8 = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img9 = ImageTk.PhotoImage(Image.open("paras.jpg"))
img10 = ImageTk.PhotoImage(Image.open("persion.jpg"))
img11 = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
img12 = ImageTk.PhotoImage(Image.open("ratata.jpg"))
img13 = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))

score1_l = Label(root, fg = "black")
score1_l.place(relx = 0.1, rely = 0.4, anchor = CENTER)

score2_l = Label(root, fg = "black")
score2_l.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_img = Label(root)
random_img.place(relx = 0.5, rely = 0.5, anchor = CENTER)


pokemon_names = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13]
pokemon_power = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

player_score1 = 0

def player1():
    global player_score1
    random_name = random.randint(0, 12)
    random_pokemon = pokemon_names[random_name]
    random_img["image"] = random_pokemon
    power = pokemon_power[random_name]
    
    player_score1 = player_score1 + power
    score1_l["text"] = str(player_score1)
    
button_1 = Button(root, image = button, command = player1)
button_1.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player_score2 = 0

def player2():
    global player_score2
    random_name2 = random.randint(0, 12)
    random_pokemon2 = pokemon_names[random_name2]
    random_img["image"] = random_pokemon2
    power2 = pokemon_power[random_name2]
    
    player_score2 = player_score2 + power2
    score2_l["text"] = str(player_score2)
    
button_2 = Button(root, image = button, command = player2)
button_2.place(relx = 0.9, rely = 0.6, anchor = CENTER)

root.mainloop()