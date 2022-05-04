from PIL import Image,ImageTk
import tkinter as tk
import ttkbootstrap as ttk

class Caculator(tk.Tk):

    def __init__(self):

        global image_file
        global image

        def cau():
            """
            A function to caculate the future value and insert it into the entry.
            """
            Investment_Amount_var = eval(Investment_Amount_entry.get())
            Years_var = eval(Years_entry.get())
            Annual_Interest_Rate_var = eval(Annual_Interest_Rate_entry.get())
            Result_var = Investment_Amount_var * pow(1 + Annual_Interest_Rate_var/1200 , Years_var*12)
            Result_entry.configure(state = "normal")
            Result_entry.delete(0, tk.END)
            Result_entry.insert(0, str(format(Result_var,".2f")))
            Result_entry.configure(state = "readonly")

        super(Caculator, self).__init__()

        #windows and overall settings
        self.title("Investment Caculator")
        self.font = "Eras Demi ITC"
        self.geometry("750x450")
        self.iconbitmap("icon.ico")

        #style settings
        style = ttk.Style(theme = "dark_pulse")
        style.configure('ButtonStyle.TButton', font=("Berlin Sans FB Demi", 20))
        
        #frames
        frame_L = ttk.Frame()
        frame_R = ttk.Frame()
        frame_B = ttk.Frame()

        #image(personal interest)
        image_file = Image.open("BG.png").resize((361,330))
        image = ImageTk.PhotoImage(image_file)

        #widget settings
        Investment_Amount_label = ttk.Label(frame_R,text = "Investment Amount")
        Investment_Amount_label.configure(font=(self.font, 15))

        Investment_Amount_entry = ttk.Entry(frame_R,bootstyle = 'primary')
        Investment_Amount_entry.configure(font=(self.font, 15),justify = "center")

        Years_label = ttk.Label(frame_R,text = "Years")
        Years_label.configure(font=(self.font, 15))

        Years_entry = ttk.Entry(frame_R, bootstyle = 'primary')
        Years_entry.configure(font=(self.font, 15),justify = "center")
        
        Annual_Interest_Rate_label = ttk.Label(frame_R,text = "Annual Interest Rate")
        Annual_Interest_Rate_label.configure(font=(self.font, 15))

        Annual_Interest_Rate_entry = ttk.Entry(frame_R, bootstyle = 'primary')
        Annual_Interest_Rate_entry.configure(font=(self.font, 15),justify = "center")
        
        Result_label = ttk.Label(frame_R,text = "Result")
        Result_label.configure(font=(self.font, 15))

        Result_entry = ttk.Entry(frame_R, bootstyle = 'primary',state="readonly")
        Result_entry.configure(font=(self.font, 15),justify = "center")
        caculate_button = ttk.Button(frame_B, text="Caculate", style ='ButtonStyle.TButton',command = cau)
        
        #Arrangement
        frame_L.grid(row = 0, column = 0,padx = 50,pady = 30)
        frame_R.grid(row = 0, column = 1)
        frame_B.grid(row = 2, column = 0,columnspan=2,ipadx = 20)
        tk.Label(frame_L,image=image).pack(side = "left")
        Investment_Amount_label.pack(anchor="w")
        Investment_Amount_entry.pack(anchor="w")
        ttk.Label(frame_R).pack(anchor="w")
        Years_label.pack(anchor="w")
        Years_entry.pack(anchor="w")
        ttk.Label(frame_R).pack(anchor="w")
        Annual_Interest_Rate_label.pack(anchor="w")
        Annual_Interest_Rate_entry.pack(anchor="w")
        ttk.Label(frame_R).pack(anchor="w")
        Result_label.pack(anchor="w")
        Result_entry.pack(anchor="w")
        caculate_button.pack(anchor="ne")

Beta = Caculator()
Beta.mainloop()
