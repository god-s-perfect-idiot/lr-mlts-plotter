from tkinter import *
from PIL import Image
from PIL import ImageTk

plotter = Tk()

plotter.state('zoomed')
plotter.title('LR-mLTS-plotter')
plotter.geometry("1366x768")
plotter.configure(background='#ffffff')
photo = PhotoImage(file = "gui.png")
plotter.iconphoto(False, photo)

menu = Menu(plotter)
plotter.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=plotter.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

windowframe = Frame(plotter, width=1000, height=600, bg = '#ffffff')
windowframe.pack(side = LEFT , pady=(50,0), padx=(50,0))

canvas = Canvas(windowframe, width = 800, height = 500, background='#ffffff', highlightcolor='#000000', highlightbackground='#000000', highlightthickness=1)
canvas.pack(side=TOP, padx = (100,100), pady=(50,50))
img = Image.open("gray matter/No Noise - LR.PNG")
img = img.resize((700,450), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
currentImg = canvas.create_image(50,30, anchor=NW, image=photoImg)

selectframe = Frame(plotter, width=250, height=600, bg = '#ffffff')
selectframe.config(highlightbackground="#000000", highlightcolor="#000000", highlightthickness=1)
selectframe.pack(side = RIGHT, padx = (0,30), pady=(50,0))

settingframe = Frame(selectframe, width = 200, height = 380, bg = '#ffffff' )
settingframe.pack(side = TOP, padx = (25,25), pady=(20,0))

optionframe = Frame(selectframe, width = 200, height = 380, bg = '#ffffff')
optionframe.pack(side= BOTTOM, padx=(25,25), pady=(0,20))

noiseframe = Frame(settingframe, width = 200, height =100, bg = '#ffffff' )
noiseframe.pack(side=TOP, padx = (10,10), pady = (0, 20))
modeframe = Frame(settingframe, width = 200, height =100, bg = '#ffffff' )
modeframe.pack(side=TOP, padx = (10,10), pady = (10, 10))
matterframe = Frame(settingframe, width = 200, height =100, bg = '#ffffff' )
matterframe.pack(side=BOTTOM, padx = (10,10), pady = (10, 10))

Label(optionframe, text = 'Tweaks' ,bg = '#ffffff').pack(side=TOP, pady=(10,0))
scrutFrame = Frame(optionframe, width = 200, height = 200,bg = '#ffffff')
scrutFrame.pack(side=TOP, padx = (10,10), pady = (0,10))
allframe = Frame(optionframe, width=200, height = 100, bg = '#ffffff')
allframe.pack(side=BOTTOM, padx =(10,10), pady =(0,10))

noise_var = StringVar(plotter)
noise_var.set('0.00')
Label(noiseframe, text = 'Noise Value:' ,bg = '#ffffff').pack(side=LEFT, pady=(10,0))
noiseopt = OptionMenu(noiseframe, noise_var, '0.00','0.05','0.10','0.15','0.20','0.25','0.30')
noiseopt.config(bg='#ffffff')
noiseopt["menu"].config(bg='#ffffff')
noiseopt.pack(side=RIGHT)

modevar = IntVar(plotter)
modevar.set(1)
Radiobutton(modeframe, text="LR", variable=modevar, value=1 ,bg = '#ffffff').pack(side=LEFT, pady=(20,20))
Radiobutton(modeframe, text="mLTS", variable=modevar, value=2 ,bg = '#ffffff').pack(side=LEFT)

mattervar = IntVar(plotter)
mattervar.set(1)
Radiobutton(matterframe, text="Grey Matter", variable=mattervar, value=1 ,bg = '#ffffff').grid(sticky=W, pady=(20,0))
Radiobutton(matterframe, text="White Matter", variable=mattervar, value=2,bg = '#ffffff').grid(sticky=W, pady=(0,50))

scrutvar = IntVar(plotter)
scrutvar.set(3)
Radiobutton(scrutFrame, text="Uncorrected value", variable=scrutvar, value=1,bg = '#ffffff').grid(sticky=W, pady=(50,0))
Radiobutton(scrutFrame, text="Corrected value", variable=scrutvar, value=2,bg = '#ffffff').grid(sticky=W)
Radiobutton(scrutFrame, text="Both", variable=scrutvar, value=3,bg = '#ffffff').grid(sticky=W)

allvar = IntVar(plotter)
allvar.set(0)
Checkbutton(allframe, text='Show All graphs', variable=allvar,bg = '#ffffff').grid(row=0, sticky=W, pady=(20,20))


def re_render():
    global canvas,photoImg

    noise = noise_var.get()
    mode = modevar.get()
    matter = mattervar.get()
    scrutiny = scrutvar.get()
    all = allvar.get()
    if(all==0):
        if(scrutiny==3):
            if(noise=="0.00" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/No Noise - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/No Noise - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.05 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.05 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.1 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.1 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.15 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.15 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.2 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.2 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.25 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.25 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==1 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.3 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==2 and matter==1 and scrutiny==3):
                img = Image.open("gray matter/Noise = 0.3 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/No Noise - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/No Noise - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.05 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.05 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.1 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.1 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.15 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.15 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.2 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.2 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.25 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.25 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==1 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.3 - LR.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==2 and matter==2 and scrutiny==3):
                img = Image.open("white matter/Noise = 0.3 - mLTS.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
        elif(scrutiny==1):
            if(noise=="0.00" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/No Noise.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.05.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.1.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.15.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.2.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.25.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and matter==1 and scrutiny==1):
                img = Image.open("gray matter/Noise = 0.3.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and matter==2 and scrutiny==1):
                img = Image.open("white matter/No Noise.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.05.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.1.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.15.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.2.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.25.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and matter==2 and scrutiny==1):
                img = Image.open("white matter/Noise = 0.3.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
        elif(scrutiny==2):
            if(noise=="0.00" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/No Noise - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/No Noise - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.05 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.05 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.1 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.1 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.15 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.15 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.2 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.2 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.25 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.25 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==1 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.3 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==2 and matter==1 and scrutiny==2):
                img = Image.open("gray matter/Noise = 0.3 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/No Noise - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.00" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/No Noise - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
                img = Image.open("white matter/Noise = 0.05 - LR single.PNG")
            elif(noise=="0.05" and mode==1 and matter==2 and scrutiny==2):
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.05" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.05 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.1 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.10" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.1 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.15 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.15" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.15 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.2 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.20" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.2 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.25 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.25" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.25 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==1 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.3 - LR single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)
            elif(noise=="0.30" and mode==2 and matter==2 and scrutiny==2):
                img = Image.open("white matter/Noise = 0.3 - mLTS single.PNG")
                img = img.resize((700,450), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                canvas.itemconfig(currentImg, image=photoImg)


Button(allframe, text = 'Render',bg = '#ffffff', command=re_render).grid( sticky=S, pady=(20,0))


plotter.mainloop()
