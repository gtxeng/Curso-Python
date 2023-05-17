import tkinter as tk
import random

class Tamagotchi:
    def __init__(self, master):
        self.master = master
        master.title("Tamagotchi")

        self.hunger_level = 50
        self.happiness_level = 50

        self.hunger_label = tk.Label(master, text="Hunger: {}".format(self.hunger_level))
        self.happiness_label = tk.Label(master, text="Happiness: {}".format(self.happiness_level))

        # Botão para alimentar o Tamagotchi
        self.feed_button = tk.Button(master, text="Feed", command=self.feed)

        # Botão para brincar com o Tamagotchi
        self.play_button = tk.Button(master, text="Play", command=self.play)

        # Botão para levar o Tamagotchi para passear
        self.walk_button = tk.Button(self, text='Passear', command=self.walk)
        
        self.walk_button.pack(side='left')
        self.hunger_label.pack()
        self.happiness_label.pack()
        self.feed_button.pack()
        self.play_button.pack()

    def walk(self):
        self.tamagotchi.walk()
        self.update_display()

    def feed(self):
        self.hunger_level -= 10
        self.update_hunger_label()
    
    def play(self):
        self.happiness_level += 10
        self.update_happiness_label()
    
    def update_hunger_label(self):
        self.hunger_label.config(text="Hunger: {}".format(self.hunger_level))
    
    def update_happiness_label(self):
        self.happiness_label.config(text="Happiness: {}".format(self.happiness_level))

    def tick(self):
        self.hunger_level += 1
        self.happiness_level -= 1

        self.update_hunger_label()
        self.update_happiness_label()

        if self.hunger_level >= 100 or self.happiness_level <= 0:
            self.master.quit()
            print("Game over!")

        self.master.after(1000, self.tick)
    
    def walk(self):
        if self.is_alive:
            self.energy -= 5
            self.happiness += 5
            self.hunger += 10

root = tk.Tk()
tamagotchi = Tamagotchi(root)
tamagotchi.tick()
root.mainloop()
