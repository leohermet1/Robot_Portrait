import imghdr
from tkinter import *
from tkinter import messagebox
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

    """def update_img(event):
        print("updating images")
        return 0"""
    def update_image(event):
        canvas1.itemconfig(imagesprite1,image = photo1update)
        canvas2.itemconfig(imagesprite2,image = photo1update)
        canvas3.itemconfig(imagesprite3,image = photo1update)
        canvas4.itemconfig(imagesprite4,image = photo1update)
        canvas5.itemconfig(imagesprite5,image = photo1update)
        canvas6.itemconfig(imagesprite6,image = photo1update)
        canvas7.itemconfig(imagesprite7,image = photo1update)
        canvas8.itemconfig(imagesprite8,image = photo1update)
        canvas9.itemconfig(imagesprite9,image = photo1update)

        choosenPictures.clear()
        #we need to create a new initial population
    
        

    boutonRefresh.bind("<Button-1>", update_image)
    
    boutonRefresh.grid(row=6, column=4)

    boutonFinish=Button(fenetre, text="Finish", bg="#B5EAD7")
    #when we click on this button it should check that there is 3 pictures that are selected
    #if not: alert message


    def lancerGA(event):
        if(len(choosenPictures)<3):
            messagebox.showinfo('Warning', "You need to choose at least 3 pictures. If you can't, click on refresh")
        print("finish")
        if(len(choosenPictures)>=3):
            messagebox.showinfo('Info', "Computation in progress")
            canvas1.itemconfig(imagesprite1,image = photo2update)
            canvas2.itemconfig(imagesprite2,image = photo2update)
            canvas3.itemconfig(imagesprite3,image = photo2update)
            canvas4.itemconfig(imagesprite4,image = photo2update)
            canvas5.itemconfig(imagesprite5,image = photo2update)
            canvas6.itemconfig(imagesprite6,image = photo2update)
            canvas7.itemconfig(imagesprite7,image = photo2update)
            canvas8.itemconfig(imagesprite8,image = photo2update)
            canvas9.itemconfig(imagesprite9,image = photo2update)
            choosenPictures.clear()


    boutonFinish.bind("<Button-1>", lancerGA)
    boutonFinish.grid(row=8, column=2)

    boutonItsHim=Button(fenetre, text="It's Him/her/them ", bg="#B5EAD7")

    def found(event):
        if(len(choosenPictures)==0):
            messagebox.showinfo('Warning', "You need to choose 1 picture.")
        elif(len(choosenPictures)>1):
            messagebox.showinfo('Warning', "You choose more that one picture, try again")
            choosenPictures.clear()
        else:
            print("found him/her/them")
            fenetre2 = Toplevel()
            fenetre2.title("It's him/her/them")
            fenetre2.configure(bg="white")

            labelConsigne1 = Label(fenetre2, text='And the criminal is', bg="white")
            labelConsigne1.grid(row=1, column=1, columnspan=3)

            boutonExit2=Button(fenetre2, text="Exit", command=fenetre2.destroy, bg="#B5EAD7")
            boutonExit2.grid(row=8, column=4)

            canvas = Canvas(fenetre2, width=400, height=400, bg="white")
            
            #create a canva in which we can put our image
            imageItsHim = Image.open("joker.jpg")#choosenPictures[len(choosenPictures)-1]
            imageItsHim = imageItsHim.resize((400, 400))
            photoItsHim = ImageTk.PhotoImage(imageItsHim)

            

            imagesprite = canvas.create_image(200,200,image=photoItsHim)

            canvas.grid(row=5, column=1)
            #uncomment when the encoder will work

            

            fenetre2.resizable(False, False)
        
            fenetre2.mainloop()


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

    image1update = Image.open('vangogh.jpg')
    image1update = image1update.resize((200, 200))
    photo1update = ImageTk.PhotoImage(image1update)

    image2update = Image.open('alice.jpg')
    image2update = image2update.resize((200, 200))
    photo2update = ImageTk.PhotoImage(image2update)

    canvas1 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    image1 = Image.open('visage_joconde.jpg')
    image1 = image1.resize((200, 200))
    photo1 = ImageTk.PhotoImage(image1)
    imagesprite1 = canvas1.create_image(100,100,image=photo1)
    #canvas1.  

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
    #canvas2.   

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


