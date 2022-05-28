from random import shuffle
from PIL import Image,ImageTk
import tkinter as tk
import ttkbootstrap as ttk

class Shuffle_cards(tk.Tk):

    def __init__(self) -> None:

        def card_shuffle():
            """
            a function to pick four random cards
            """
            shuffle(poker_cards_img_list)
            card_1.configure(image = poker_cards_img_list[0])
            card_2.configure(image = poker_cards_img_list[1])
            card_3.configure(image = poker_cards_img_list[2])
            card_4.configure(image = poker_cards_img_list[3])
            
        super().__init__()
    
        #windows and overall settings
        self.title("Pick Four cards randomly")
        self.geometry("900x600")
        style = ttk.Style(theme = "dark_pulse")
        style.configure('ButtonStyle.TButton', font=("Berlin Sans FB Demi", 20))

        #process images
        poker_cards_img_list = []
        for i in range(1,14):
            imagefile = Image.open(f"poker_imgs\{i}.png").resize((200,280))
            image = ImageTk.PhotoImage(imagefile)
            poker_cards_img_list.append(image)
        
        #widget settings
        card_1 = ttk.Label(self,image=poker_cards_img_list[0])
        card_2 = ttk.Label(self,image=poker_cards_img_list[1])
        card_3 = ttk.Label(self,image=poker_cards_img_list[2])
        card_4 = ttk.Label(self,image=poker_cards_img_list[3])
        shuffle_button = ttk.Button(self, text="SHUFFLE!", style ='ButtonStyle.TButton', command = card_shuffle)

        #arrangement
        card_1.place(x = 20,y = 100)
        card_2.place(x = 240,y = 100)
        card_3.place(x = 460,y = 100)
        card_4.place(x = 680,y = 100)
        shuffle_button.place(x = 450, y = 500,anchor = tk.CENTER)

if __name__ == "__main__":
    s = Shuffle_cards()
    s.mainloop()

