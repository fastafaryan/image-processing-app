import cv2
from PIL import Image, ImageTk
import tkinter as tk

class map:
    def __init__(self, cv) :
        canv = Canvas(self, relief=SUNKEN)
        canv.config(width=400, height=200)
        #canv.config(scrollregion=(0,0,1000, 1000))
        #canv.configure(scrollregion=canv.bbox('all'))
        canv.config(highlightthickness=0)

        sbarV = Scrollbar(self, orient=VERTICAL)
        sbarH = Scrollbar(self, orient=HORIZONTAL)

        sbarV.config(command=canv.yview)
        sbarH.config(command=canv.xview)

        canv.config(yscrollcommand=sbarV.set)
        canv.config(xscrollcommand=sbarH.set)

        sbarV.pack(side=RIGHT, fill=Y)
        sbarH.pack(side=BOTTOM, fill=X)

        canv.pack(side=LEFT, expand=YES, fill=BOTH)
        self.im=Image.open("./assets/map2.png")
        width,height=self.im.size
        canv.config(scrollregion=(0,0,width,height))
        self.im2=ImageTk.PhotoImage(self.im)
        self.imgtag=canv.create_image(0,0,anchor="nw",image=self.im2)