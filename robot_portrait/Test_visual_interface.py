import imghdr
from tkinter import *
import string
from turtle import bgcolor, position
import PIL
from PIL import Image
from PIL import ImageTk
from GA import *

def visualInterface(encodedVectors):

    fenetre = Tk()
    fenetre.title('Robot Portrait group 1')
    fenetre.configure(bg="white")

    

    boutonExit=Button(fenetre, text="Exit", command=fenetre.quit, bg="#B5EAD7")
    boutonExit.grid(row=8, column=4)

    boutonRefresh=Button(fenetre, text="Refresh", bg="#B5EAD7")#, command=creationPop(encodedVectors)

    def update_img(event):
        print("updating images")
        return 0
        """canvas1 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image
        image1 = Image.open('logo.png')
        image1 = image1.resize((200, 200))
        photo1 = ImageTk.PhotoImage(image1)
        imagesprite1 = canvas1.create_image(100,100,image=photo1)
        canvas1.focus_set()

        def clavier(event):
            #photochoisie[i]=1
            #i=i+1
            print("photo 1 choisie")
            if(1 not in choosenPictures):
                choosenPictures.append(1)

        canvas1.bind("<Button-1>", clavier)
        #canvas1.pack(side=LEFT, padx=20, pady=20)
        canvas1.grid(row=5, column=1)

        ####### Image 2
        canvas2 = Canvas(fenetre, width=200, height=200, )
        #create a canva in which we can put our image
        image2 = Image.open('logo.png')
        image2 = image2.resize((200, 200))
        photo2 = ImageTk.PhotoImage(image2)
        imagesprite2 = canvas2.create_image(100,100,image=photo2)
        canvas2.focus_set()

        def clavier2(event):
            #photochoisie[i]=2
            #i=i+1
            print("photo 2 choisie")
            if(2 not in choosenPictures):
                choosenPictures.append(2)

        canvas2.bind("<Button-1>", clavier2)
        #canvas2.pack(side=RIGHT, padx=20, pady=20)
        canvas2.grid(row=5, column=2)


        ####### Image 3
        canvas3 = Canvas(fenetre, width=200, height=200, )
        #create a canva in which we can put our image

        image3 = Image.open('logo.png')
        image3 = image3.resize((200, 200))
        photo3 = ImageTk.PhotoImage(image3)
        imagesprite3 = canvas3.create_image(100,100,image=photo3)
        canvas3.focus_set()

        def clavier3(event):
            #photochoisie[i]=2
            #i=i+1
            print("photo 3 choisie")
            if(3 not in choosenPictures):
                choosenPictures.append(3)
        
        canvas3.bind("<Button-1>", clavier3)
        #canvas3.pack(side=RIGHT, padx=20, pady=20)
        canvas3.grid(row=5, column=3)

        ####### Image 4
        canvas4 = Canvas(fenetre, width=200, height=200 )
        #create a canva in which we can put our image

        image4 = Image.open('logo.png')
        image4 = image4.resize((200, 200))
        photo4 = ImageTk.PhotoImage(image4)
        imagesprite4 = canvas4.create_image(100,100,image=photo4)
        canvas4.focus_set()

        def clavier4(event):
            #photochoisie[i]=2
            #i=i+1
            print("photo 4 choisie")
            if(4 not in choosenPictures):
                choosenPictures.append(4)

        canvas4.bind("<Button-1>", clavier4)
        canvas4.grid(row=6, column=1)
    
        ####### Image 5
        canvas5 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image

        image5 = Image.open('logo.png')
        image5 = image5.resize((200, 200))
        photo5 = ImageTk.PhotoImage(image5)
        imagesprite5 = canvas5.create_image(100,100,image=photo5)
        canvas5.focus_set()

        def clavier5(event):
            #photochoisie[i]=2
            #i=i+1
            print("photo 5 choisie")
            if(5 not in choosenPictures):
                choosenPictures.append(5)

        canvas5.bind("<Button-1>", clavier5)
        canvas5.grid(row=6, column=2)


        ####### Image 6
        canvas6 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image

        image6 = Image.open('logo.png')
        image6 = image6.resize((200, 200))
        photo6 = ImageTk.PhotoImage(image6)
        imagesprite6 = canvas6.create_image(100,100,image=photo6)
        canvas6.focus_set()

        def clavier6(event):
            #photochoisie[i]=2
            #i=i+1
            print("photo 6 choisie")
            if(6 not in choosenPictures):
                choosenPictures.append(6)

        canvas6.bind("<Button-1>", clavier6)
        canvas6.grid(row=6, column=3)

        ####### Image 7
        canvas7 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image

        image7 = Image.open('logo.png')
        image7 = image7.resize((200, 200))
        photo7 = ImageTk.PhotoImage(image7)
        imagesprite7 = canvas7.create_image(100,100,image=photo7)
        canvas7.focus_set()

        def clavier7(event):
            print("photo 7 choisie")
            if(7 not in choosenPictures):
                choosenPictures.append(7)

        canvas7.bind("<Button-1>", clavier7)
        canvas7.grid(row=7, column=1)

        ####### Image 8
        canvas8 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image

        image8 = Image.open('logo.png')
        image8 = image8.resize((200, 200))
        photo8 = ImageTk.PhotoImage(image8)
        imagesprite8 = canvas8.create_image(100,100,image=photo8)
        canvas8.focus_set()

        def clavier8(event):
            print("photo 8 choisie")
            if(8 not in choosenPictures):
                choosenPictures.append(8)

        canvas8.bind("<Button-1>", clavier8)
        canvas8.grid(row=7, column=2)

        ####### Image 9
        canvas9 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image

        image9 = Image.open('logo.png')
        image9 = image9.resize((200, 200))
        photo9 = ImageTk.PhotoImage(image9)
        imagesprite9 = canvas9.create_image(100,100,image=photo9)
        canvas9.focus_set()

        def clavier9(event):
            print("photo 9 choisie")
            if(9 not in choosenPictures):
                choosenPictures.append(9)

        canvas9.bind("<Button-1>", clavier9)
        canvas9.grid(row=7, column=3)

        img2=ImageTk.PhotoImage(Image.open("logo.png"))
        imagesprite1 = canvas1.create_image(100,100,image=img2)
        imagesprite2 = canvas2.create_image(100,100,image=img2)
        imagesprite3 = canvas3.create_image(100,100,image=img2)
        imagesprite4 = canvas4.create_image(100,100,image=img2)
        imagesprite5 = canvas5.create_image(100,100,image=img2)
        imagesprite6 = canvas6.create_image(100,100,image=img2)
        imagesprite7 = canvas7.create_image(100,100,image=img2)
        imagesprite8 = canvas8.create_image(100,100,image=img2)
        imagesprite9 = canvas9.create_image(100,100,image=img2)"""

    boutonRefresh.bind("<Button-1>", update_img)
    
    boutonRefresh.grid(row=6, column=4)

    boutonFinish=Button(fenetre, text="Finish", bg="#B5EAD7")
    boutonFinish.focus_set()

    def lancerGA(event):
        print("finish")

    boutonFinish.bind("<Button-1>", lancerGA)
    boutonFinish.grid(row=8, column=2)

    boutonItsHim=Button(fenetre, text="It's Him/her/them ", bg="#B5EAD7")

    def found(event):
        print("found him/her/them")

    boutonItsHim.bind("<Button-1>", found)

    boutonItsHim.grid(row=5, column=4)

    labelConsigne1 = Label(fenetre, text='Choose at least 3 photos that look like the person you saw and click on Finish.', bg="white")
    labelConsigne1.grid(row=1, column=1, columnspan=3)

    labelConsigne2 = Label(fenetre, text='If there are less than 3, click on the refresh button to get new photos.', bg="white")
    labelConsigne2.grid(row=2, column=1, columnspan=3)

    labelConsigne3 = Label(fenetre, text="If you see a photo that is very close, click on the photo and then on It's him.", bg="white")
    labelConsigne3.grid(row=3, column=1, columnspan=3)

    labelGauche= Label(fenetre, text="            ", bg="white")
    labelGauche.grid(row=0, column=0)

    labelDessusPhoto= Label(fenetre, text="            ", bg="white")
    labelDessusPhoto.grid(row=4, column=0)

    choosenPictures=[]

    


    ####### Image 1
    """def createCanvas1(img):
        canvas1 = Canvas(fenetre, width=200, height=200)
        #create a canva in which we can put our image
        image1 = Image.open(img)
        image1 = image1.resize((200, 200))
        photo1 = ImageTk.PhotoImage(image1)
        imagesprite1 = canvas1.create_image(100,100,image=photo1)
        canvas1.focus_set()

        def clavier(event):
            #photochoisie[i]=1
            #i=i+1
            print("photo 1 choisie")
            if(1 not in choosenPictures):
                choosenPictures.append(1)

        canvas1.bind("<Button-1>", clavier)
        #canvas1.pack(side=LEFT, padx=20, pady=20)
        canvas1.grid(row=5, column=1)
        return 0"""


    canvas1 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    image1 = Image.open('visage_joconde.jpg')
    image1 = image1.resize((200, 200))
    photo1 = ImageTk.PhotoImage(image1)
    imagesprite1 = canvas1.create_image(100,100,image=photo1)
    canvas1.focus_set()

    def clavier(event):
        #photochoisie[i]=1
        #i=i+1
        print("photo 1 choisie")
        if(1 not in choosenPictures):
            choosenPictures.append(1)

    canvas1.bind("<Button-1>", clavier)
    #canvas1.pack(side=LEFT, padx=20, pady=20)
    canvas1.grid(row=5, column=1)

    ####### Image 2
    canvas2 = Canvas(fenetre, width=200, height=200, )
    #create a canva in which we can put our image
    image2 = Image.open('visage_joconde.jpg')
    image2 = image2.resize((200, 200))
    photo2 = ImageTk.PhotoImage(image2)
    imagesprite2 = canvas2.create_image(100,100,image=photo2)
    canvas2.focus_set()

    def clavier2(event):
        #photochoisie[i]=2
        #i=i+1
        print("photo 2 choisie")
        if(2 not in choosenPictures):
            choosenPictures.append(2)

    canvas2.bind("<Button-1>", clavier2)
    #canvas2.pack(side=RIGHT, padx=20, pady=20)
    canvas2.grid(row=5, column=2)


    ####### Image 3
    canvas3 = Canvas(fenetre, width=200, height=200, )
    #create a canva in which we can put our image

    image3 = Image.open('visage_joconde.jpg')
    image3 = image3.resize((200, 200))
    photo3 = ImageTk.PhotoImage(image3)
    imagesprite3 = canvas3.create_image(100,100,image=photo3)
    canvas3.focus_set()

    def clavier3(event):
        #photochoisie[i]=2
        #i=i+1
        print("photo 3 choisie")
        if(3 not in choosenPictures):
            choosenPictures.append(3)
    
    canvas3.bind("<Button-1>", clavier3)
    #canvas3.pack(side=RIGHT, padx=20, pady=20)
    canvas3.grid(row=5, column=3)

    ####### Image 4
    canvas4 = Canvas(fenetre, width=200, height=200 )
    #create a canva in which we can put our image

    image4 = Image.open('visage_joconde.jpg')
    image4 = image4.resize((200, 200))
    photo4 = ImageTk.PhotoImage(image4)
    imagesprite4 = canvas4.create_image(100,100,image=photo4)
    canvas4.focus_set()

    def clavier4(event):
        #photochoisie[i]=2
        #i=i+1
        print("photo 4 choisie")
        if(4 not in choosenPictures):
            choosenPictures.append(4)

    canvas4.bind("<Button-1>", clavier4)
    canvas4.grid(row=6, column=1)
 
    ####### Image 5
    canvas5 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image

    image5 = Image.open('visage_joconde.jpg')
    image5 = image5.resize((200, 200))
    photo5 = ImageTk.PhotoImage(image5)
    imagesprite5 = canvas5.create_image(100,100,image=photo5)
    canvas5.focus_set()

    def clavier5(event):
        #photochoisie[i]=2
        #i=i+1
        print("photo 5 choisie")
        if(5 not in choosenPictures):
            choosenPictures.append(5)

    canvas5.bind("<Button-1>", clavier5)
    canvas5.grid(row=6, column=2)


    ####### Image 6
    canvas6 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image

    image6 = Image.open('visage_joconde.jpg')
    image6 = image6.resize((200, 200))
    photo6 = ImageTk.PhotoImage(image6)
    imagesprite6 = canvas6.create_image(100,100,image=photo6)
    canvas6.focus_set()

    def clavier6(event):
        #photochoisie[i]=2
        #i=i+1
        print("photo 6 choisie")
        if(6 not in choosenPictures):
            choosenPictures.append(6)

    canvas6.bind("<Button-1>", clavier6)
    canvas6.grid(row=6, column=3)

    ####### Image 7
    canvas7 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image

    image7 = Image.open('visage_joconde.jpg')
    image7 = image7.resize((200, 200))
    photo7 = ImageTk.PhotoImage(image7)
    imagesprite7 = canvas7.create_image(100,100,image=photo7)
    canvas7.focus_set()

    def clavier7(event):
        print("photo 7 choisie")
        if(7 not in choosenPictures):
            choosenPictures.append(7)

    canvas7.bind("<Button-1>", clavier7)
    canvas7.grid(row=7, column=1)

    ####### Image 8
    canvas8 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image

    image8 = Image.open('visage_joconde.jpg')
    image8 = image8.resize((200, 200))
    photo8 = ImageTk.PhotoImage(image8)
    imagesprite8 = canvas8.create_image(100,100,image=photo8)
    canvas8.focus_set()

    def clavier8(event):
        print("photo 8 choisie")
        if(8 not in choosenPictures):
            choosenPictures.append(8)

    canvas8.bind("<Button-1>", clavier8)
    canvas8.grid(row=7, column=2)

    ####### Image 9
    canvas9 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image

    image9 = Image.open('visage_joconde.jpg')
    image9 = image9.resize((200, 200))
    photo9 = ImageTk.PhotoImage(image9)
    imagesprite9 = canvas9.create_image(100,100,image=photo9)
    canvas9.focus_set()

    def clavier9(event):
        print("photo 9 choisie")
        if(9 not in choosenPictures):
            choosenPictures.append(9)

    canvas9.bind("<Button-1>", clavier9)
    canvas9.grid(row=7, column=3)

    
    #createCanvas1('visage_joconde.jpg')

    fenetre.resizable(False, False)
    
    fenetre.mainloop()

    return choosenPictures


