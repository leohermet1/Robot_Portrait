import imghdr
from tkinter import *
from tkinter import messagebox
import string
from turtle import bgcolor, position
import PIL
from PIL import Image
from PIL import ImageTk
from GA import *
import decoder
from PIL import Image as im
import keras


def visualInterface(encodedVectors, decoderModel, popCreated, indexPop, randomseed):

    fenetre = Tk()
    fenetre.title('Robot Portrait group 1')
    fenetre.configure(bg="white")
    

    boutonExit=Button(fenetre, text="Exit", command=fenetre.quit, bg="#B5EAD7")
    boutonExit.grid(row=8, column=4)

    boutonRefresh=Button(fenetre, text="Refresh", bg="#B5EAD7")#, command=creationPop(encodedVectors)

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
    imageToShow2=[]
    def FunctionimageToShow2(imageToShow2):
        for i in range(9):
            image=Image.open("ImageUpdated\image"+str(i)+".jpg")
            image.resize((200, 200))
            photo=ImageTk.PhotoImage(image)
            #imageToShow2[i]=photo
            imageToShow2.append(photo)
    
    def lancerGA(event):
        if(len(choosenPictures)<3):
            messagebox.showinfo('Warning', "You need to choose at least 3 pictures. If you can't, click on refresh")
        print("finish")
        if(len(choosenPictures)>=3):
            messagebox.showinfo('Info', "Computation in progress")
            population=[]
            for i in range (len(choosenPictures)):
                if(len(popCreated)!=0):
                    print("len avant delete")
                    print(len(popCreated))
                    print()
                    pos = choosenPictures[i]-1
                    population.append(popCreated[pos])
                    print("dans le if")
                else:
                    pos = choosenPictures[i]-1
                    population.append(completePop[pos])
                    print("dans le else")

            for i in range(len(popCreated)):
                for j in range(len(popCreated[i])):
                    np.delete(popCreated[i][j], 0)
            
            print()
            print("len après delete")
            print(len(popCreated))

            completePop=completePopulation(population, encodedVectors, indexPop, randomseed) # this will be the input of the decoder

            decodedPictures = decoder.decoderFunction(completePop, decoderModel)

            for i in range (len(decodedPictures)):
                image = im.fromarray(np.uint8(decodedPictures[i]))
                image.save("ImageUpdated\image" +str(i)+ ".jpg")
            
            choosenPictures.clear()

            FunctionimageToShow2(imageToShow2)

            canvas1.itemconfig(imagesprite1,image = imageToShow2[0])

            ####### Image 2
            canvas2.itemconfig(imagesprite2,image = imageToShow2[1])

            ####### Image 3
            canvas3.itemconfig(imagesprite3,image = imageToShow2[2])

            ####### Image 4
            canvas4.itemconfig(imagesprite4,image = imageToShow2[3])
        
            ####### Image 5
            canvas5.itemconfig(imagesprite5,image = imageToShow2[4])

            ####### Image 6
            canvas6.itemconfig(imagesprite6,image = imageToShow2[5])

            ####### Image 7
            canvas7.itemconfig(imagesprite7,image = imageToShow2[6])

            ####### Image 8
            canvas8.itemconfig(imagesprite8,image = imageToShow2[7])

            ####### Image 9
            canvas9.itemconfig(imagesprite9,image = imageToShow2[8])

    
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
            imageItsHim = Image.open("ImageUpdated\image"+str(choosenPictures[0]-1)+".jpg")#choosenPictures[len(choosenPictures)-1]
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
    imageToShow=[]
    for i in range(9):
        image=Image.open("ImageBeginning\image"+str(i)+".jpg")
        image.resize((200, 200))
        photo=ImageTk.PhotoImage(image)
        imageToShow.append(photo)         
        
        
    
    image1update = Image.open('vangogh.jpg')
    image1update = image1update.resize((200, 200))
    photo1update = ImageTk.PhotoImage(image1update)

    image2update = Image.open('alice.jpg')
    image2update = image2update.resize((200, 200))
    photo2update = ImageTk.PhotoImage(image2update)

    canvas1 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite1 = canvas1.create_image(100,100,image=imageToShow[0])
    def clavier(event):
            print("photo 1 choisie")
            if(1 not in choosenPictures):
                choosenPictures.append(1)
    canvas1.bind("<Button-1>", clavier)
    canvas1.grid(row=5, column=1)

    ####### Image 2
    canvas2 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite2 = canvas2.create_image(100,100,image=imageToShow[1])
    def clavier2(event):
        print("photo 2 choisie")
        if(2 not in choosenPictures):
            choosenPictures.append(2)
    canvas2.bind("<Button-1>", clavier2)
    canvas2.grid(row=5, column=2)


    ####### Image 3
    canvas3 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite3 = canvas3.create_image(100,100,image=imageToShow[2])
    def clavier3(event):
        print("photo 3 choisie")
        if(3 not in choosenPictures):
            choosenPictures.append(3)
    canvas3.bind("<Button-1>", clavier3)
    canvas3.grid(row=5, column=3)

    ####### Image 4
    canvas4 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite4 = canvas4.create_image(100,100,image=imageToShow[3])
    def clavier4(event):
        print("photo 4 choisie")
        if(4 not in choosenPictures):
            choosenPictures.append(4)
    canvas4.bind("<Button-1>", clavier4)
    canvas4.grid(row=6, column=1)
 
    ####### Image 5
    canvas5 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite5 = canvas5.create_image(100,100,image=imageToShow[4])
    def clavier5(event):
        print("photo 5 choisie")
        if(5 not in choosenPictures):
            choosenPictures.append(5)
    canvas5.bind("<Button-1>", clavier5)
    canvas5.grid(row=6, column=2)


    ####### Image 6
    canvas6 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite6 = canvas6.create_image(100,100,image=imageToShow[5])
    def clavier6(event):
        print("photo 6 choisie")
        if(6 not in choosenPictures):
            choosenPictures.append(6)
    canvas6.bind("<Button-1>", clavier6)
    canvas6.grid(row=6, column=3)

    ####### Image 7
    canvas7 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite7 = canvas7.create_image(100,100,image=imageToShow[6])       
    def clavier7(event):
        print("photo 7 choisie")
        if(7 not in choosenPictures):
            choosenPictures.append(7)
    canvas7.bind("<Button-1>", clavier7)
    canvas7.grid(row=7, column=1)

    ####### Image 8
    canvas8 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite8 = canvas8.create_image(100,100,image=imageToShow[7])       
    def clavier8(event):
        print("photo 8 choisie")
        if(8 not in choosenPictures):
            choosenPictures.append(8)
    canvas8.bind("<Button-1>", clavier8)
    canvas8.grid(row=7, column=2)

    ####### Image 9
    canvas9 = Canvas(fenetre, width=200, height=200)
    #create a canva in which we can put our image
    imagesprite9 = canvas9.create_image(100,100,image=imageToShow[8])          
    def clavier9(event):
        print("photo 9 choisie")
        if(9 not in choosenPictures):
            choosenPictures.append(9)
    canvas9.bind("<Button-1>", clavier9)
    canvas9.grid(row=7, column=3)

    fenetre.resizable(False, False)
    
    fenetre.mainloop()

    return 0


