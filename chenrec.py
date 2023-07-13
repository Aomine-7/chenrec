import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from PIL import Image,ImageTk
from ttkbootstrap import Style
import webbrowser

# ==========================================================================================================================
# Chenrec—————Cultural relic reconstruction system of non-lambertian body based on a defferentiable Monte Carlo renderer
# ===========================================================================================================================

def resize(w, h, w_box, h_box, pil_image):  
  ''' 
  resize a pil_image object so it will fit into 
  a box of size w_box times h_box, but retain aspect ratio 
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
  '''  
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
  f2 = 1.0*h_box/h  
  factor = min([f1, f2])  
  #print(f1, f2, factor) # test  
  # use best down-sizing filter  
  width = int(w*factor)  
  height = int(h*factor)  
  return pil_image.resize((width, height), Image.ANTIALIAS)  

# ==============================================================================================
############################ P2-Information ############################
# ==============================================================================================

# elephant metadata
def btnclick1():
  w2=tk.Toplevel(window)
  w2.title('elephant metadata')
  w2.geometry('800x700+350+150')

  la1=tk.Label(w2,text='Spouted vessel (he) in the form of an elephant with masks (taotie), dragons,\nand snakes',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w2)
  framew2=tk.Frame(w2)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='PERIOD:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img1=Image.open('F:/chenrec/image/elephant.jpg')
  w,h=img1.size
  img1=resize(w,h,550,270,img1)
  photo2=ImageTk.PhotoImage(img1)
  imgLabel=tk.Label(framew1,image=photo2)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Bronze',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x W x D (overall): 17.2 x 10.7 x 21.4 cm (6 3/4 x 4 3/16 x 8 7/16 in)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la12=tk.Label(framew2,text='Vessel',font=("Times New Roman",12),justify="center")
  la12.pack() 
  la13=tk.Label(framew2,text='Anyang, Henan province, China',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='ca. 1100 BCE',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='Late Shang dynasty, late Anyang period',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Freer Gallery of Art and Arthur M. Sackler Gallery',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='http://n2t.net/ark:/65665/ye31d065109-ffb8-4d3f-ba49-7938b4f3f235',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='Elephant ;\nShang dynasty (ca. 1600 - ca. 1050 BCE) ;\nAnyang period, Late Shang dynasty (ca. 1300 - 1050 BCE) ;\nWine ;\nChinese art\n\n',font=("Times New Roman",12),justify="left")
  la19.pack()
  
  img9=Image.open('F:/chenrec/image/elephant2.jpg')
  w,h=img9.size
  img9=resize(w,h,550,270,img9)
  photo10=ImageTk.PhotoImage(img9)
  imgLabel=tk.Label(framew2,image=photo10)
  imgLabel.pack(side='bottom')

  la20=tk.Label(w2,text=' ',font=("Times New Roman",15),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w2.mainloop()
  
# baluster vase metadata
def btnclick2():
  w3=tk.Toplevel(window)
  w3.title('baluster vase metadata')
  w3.geometry('630x750+350+150')

  la1=tk.Label(w3,text='Baluster vase, from a five-piece garniture (F1980.190-.194)',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w3)
  framew2=tk.Frame(w3)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la21=tk.Label(framew1,text='STYLE:',font=("Times New Roman",12),justify="left")
  la21.pack() 
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='PERIOD:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/f191.jpg')
  w,h=img2.size
  img2=resize(w,h,320,370,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(w3,image=photo3)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Porcelain with cobalt pigment under clear colorless glaze',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x Diam (assembled): 46.3 * 17.2 cm (18 1/4 * 6 3/4 in)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la12=tk.Label(framew2,text='Jingdezhen ware',font=("Times New Roman",12),justify="center")
  la12.pack() 
  la13=tk.Label(framew2,text='Vessel',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='Jingdezhen, Jiangxi province, China',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='1662-1722',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Qing dynasty, Kangxi reign',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='Freer Gallery of Art and Arthur M. Sackler Gallery',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/ye33c798d33-dc71-4235-8ee8-e2cd50ba2eab',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='Jingdezhen ware ;\nKangxi reign (1662 - 1722) ;\nCobalt pigment ;\nPorcelain ;\nChinese art',font=("Times New Roman",12),justify="left")
  la22.pack() 

  la20=tk.Label(w3,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w3.mainloop()

# beaker-shaped vase metadata
def btnclick3():
  w4=tk.Toplevel(window)
  w4.title('beaker-shaped vase metadata')
  w4.geometry('600x750+350+150')

  la1=tk.Label(w4,text='Beaker-shaped vase, from a five-piece garniture (F1980.190-.194)',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w4)
  framew2=tk.Frame(w4)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la21=tk.Label(framew1,text='STYLE:',font=("Times New Roman",12),justify="left")
  la21.pack() 
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='PERIOD:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/f194.jpg')
  w,h=img2.size
  img2=resize(w,h,320,370,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(w4,image=photo3)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Porcelain with cobalt pigment under clear colorless glaze',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x Diam: 42.5 * 21.2 cm (16 3/4 * 8 3/8 in)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la12=tk.Label(framew2,text='Jingdezhen ware',font=("Times New Roman",12),justify="center")
  la12.pack() 
  la13=tk.Label(framew2,text='Vessel',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='Jingdezhen, Jiangxi province, China',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='1662-1722',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Qing dynasty, Kangxi reign',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='Freer Gallery of Art and Arthur M. Sackler Gallery',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/ye3d6e97e75-58e7-4353-a93c-fea688ddc14f',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='Jingdezhen ware ;\nKangxi reign (1662 - 1722) ;\nFlute ;\nPorcelain ;\nChinese art',font=("Times New Roman",12),justify="left")
  la22.pack() 

  la20=tk.Label(w4,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w4.mainloop()

# incense metadata
def btnclick4():
  w5=tk.Toplevel(window)
  w5.title('incense metadata')
  w5.geometry('740x750+350+150')

  la1=tk.Label(w5,text='Lidded incense burner (xianglu) with geometric decoration and narrative scenes',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w5)
  framew2=tk.Frame(w5)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='PERIOD:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/incense2.jpg')
  w,h=img2.size
  img2=resize(w,h,300,235,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(framew1,image=photo3)
  imgLabel.pack(side='bottom')
  img3=Image.open('F:/chenrec/image/incense.jpg')
  w,h=img3.size
  img3=resize(w,h,230,275,img3)
  photo4=ImageTk.PhotoImage(img3)
  imgLabel=tk.Label(framew1,image=photo4)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Bronze with gold, silver, turquoise, and carnelian inlay',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x W: 17.9 x 10 cm (7 1/16 x 3 15/16 in)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la13=tk.Label(framew2,text='Vessel',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='Henan or Hebei province, China',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='ca. 2nd century BCE',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Early Western Han dynasty',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='Freer Gallery of Art and Arthur M. Sackler Gallery',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/ye3e4db4f58-a6f7-4578-a51a-3f62430f2242',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='Daoism ;\nWestern Han dynasty (206 BCE - 9 CE) ;\nIncense ;\nChinese art',font=("Times New Roman",12),justify="left")
  la22.pack() 

  img4=Image.open('F:/chenrec/image/incense3.jpg')
  w,h=img4.size
  img4=resize(w,h,300,235,img4)
  photo5=ImageTk.PhotoImage(img4)
  imgLabel=tk.Label(framew2,image=photo5)
  imgLabel.pack(side='bottom')
  img5=Image.open('F:/chenrec/image/incense4.jpg')
  w,h=img5.size
  img5=resize(w,h,300,275,img5)
  photo6=ImageTk.PhotoImage(img5)
  imgLabel=tk.Label(framew2,image=photo6)
  imgLabel.pack(side='bottom')

  la20=tk.Label(w5,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w5.mainloop()

# kylix metadata
def btnclick5():
  w6=tk.Toplevel(window)
  w6.title('kylix metadata')
  w6.geometry('600x650+350+150')

  la1=tk.Label(w6,text='Kylix',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w6)
  framew2=tk.Frame(w6)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack() 
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='Catalogue Status:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/kylix.jpg')
  w,h=img2.size
  img2=resize(w,h,500,600,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(w6,image=photo3)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Painted earthenware',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x W x D: 7.3 x 22 x 18 cm (2 7/8 x 8 11/16 x 7 1/16 in.)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la13=tk.Label(framew2,text='Ceramics',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='Greece',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='ca. 800 BC',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Research in Progress',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='Cooper Hewitt, Smithsonian Design Museum',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/kq4b4739920-0b22-4bb0-aabd-5f7196b916ad',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='Ceramics ;\nDecorative Arts ;\nKylix\n',font=("Times New Roman",12),justify="left")
  la22.pack() 

  la20=tk.Label(w6,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w6.mainloop()

# pottery metadata
def btnclick6():
  w7=tk.Toplevel(window)
  w7.title('pottery metadata')
  w7.geometry('800x700+350+150')

  la1=tk.Label(w7,text='Colonoware pot from Cooper River, Charleston County, SC',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w7)
  framew2=tk.Frame(w7)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='PLACE MADE:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img1=Image.open('F:/chenrec/image/pottery.jpg')
  w,h=img1.size
  img1=resize(w,h,350,320,img1)
  photo2=ImageTk.PhotoImage(img1)
  imgLabel=tk.Label(framew1,image=photo2)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Clay , glue , plaster of Paris and paint',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x W: 9 1/16 * 10 1/2 in. (23 * 26.7 cm)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la12=tk.Label(framew2,text='Pottery',font=("Times New Roman",12),justify="center")
  la12.pack() 
  la13=tk.Label(framew2,text='Charleston County, South Carolina, United States',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='18th century',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la16=tk.Label(framew2,text='National Museum of African American History and Culture',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='http://n2t.net/ark:/65665/fd5be845410-4985-4095-bf70-f4c4cba40235',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='African American ;\nCooking and dining ;\nDomestic life ;\nFolklife ;\nFoodways\n',font=("Times New Roman",12),justify="left")
  la19.pack()
  
  img9=Image.open('F:/chenrec/image/pottery2.jpg')
  w,h=img9.size
  img9=resize(w,h,350,320,img9)
  photo10=ImageTk.PhotoImage(img9)
  imgLabel=tk.Label(framew2,image=photo10)
  imgLabel.pack(side='bottom')

  la20=tk.Label(w7,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w7.mainloop()

# stoneware metadata
def btnclick7():
  w8=tk.Toplevel(window)
  w8.title('stoneware metadata')
  w8.geometry('740x750+350+150')

  la1=tk.Label(w8,text='Stoneware jug created by Thomas Commeraw',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w8)
  framew2=tk.Frame(w8)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='PLACE MADE:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/stoneware4.jpg')
  w,h=img2.size
  img2=resize(w,h,300,255,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(framew1,image=photo3)
  imgLabel.pack(side='bottom')
  img3=Image.open('F:/chenrec/image/stoneware2.jpg')
  w,h=img3.size
  img3=resize(w,h,300,255,img3)
  photo4=ImageTk.PhotoImage(img3)
  imgLabel=tk.Label(framew1,image=photo4)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Ceramic and glaze',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='15 1/4 x 9 3/4 x 9 3/4 x 31 5/8 in. (38.7 x 24.8 x 24.8 x 80.3 cm)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la13=tk.Label(framew2,text='Jugs',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='New York City, New York, United States',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='ca. 1797 - 1819',font=("Times New Roman",12),justify="center")
  la15.pack()
  la17=tk.Label(framew2,text='National Museum of African American History and Culture',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/fd53a08830f-aa72-4c7d-9ddf-4effa4808f73',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='African American ;\nCraftsmanship ;\nDesign ;\nFree communities of color ;\nLabor',font=("Times New Roman",12),justify="left")
  la22.pack() 

  img4=Image.open('F:/chenrec/image/stoneware3.jpg')
  w,h=img4.size
  img4=resize(w,h,300,255,img4)
  photo5=ImageTk.PhotoImage(img4)
  imgLabel=tk.Label(framew2,image=photo5)
  imgLabel.pack(side='bottom')
  img5=Image.open('F:/chenrec/image/stoneware.jpg')
  w,h=img5.size
  img5=resize(w,h,300,255,img5)
  photo6=ImageTk.PhotoImage(img5)
  imgLabel=tk.Label(framew2,image=photo6)
  imgLabel.pack(side='bottom')

  la20=tk.Label(w8,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w8.mainloop()

# wine_container metadata
def btnclick8():
  w9=tk.Toplevel(window)
  w9.title('wine_container metadata')
  w9.geometry('625x750+350+150')

  la1=tk.Label(w9,text='Ritual wine container (fangyi) with masks(taotie), serpents, and birds',font=("Times New Roman",15),justify="left")
  la1.pack()

  framew1=tk.Frame(w9)
  framew2=tk.Frame(w9)

  la2=tk.Label(framew1,text='MEDIUM:',font=("Times New Roman",12),justify="left")
  la2.pack() 
  la3=tk.Label(framew1,text='DIMENSIONS:',font=("Times New Roman",12),justify="left")
  la3.pack()
  la4=tk.Label(framew1,text='TYPE:',font=("Times New Roman",12),justify="left")
  la4.pack() 
  la5=tk.Label(framew1,text='ORIGIN:',font=("Times New Roman",12),justify="left")
  la5.pack()
  la6=tk.Label(framew1,text='DATE:',font=("Times New Roman",12),justify="left")
  la6.pack() 
  la7=tk.Label(framew1,text='PERIOD:',font=("Times New Roman",12),justify="left")
  la7.pack()
  la8=tk.Label(framew1,text='DATA SOURCE:',font=("Times New Roman",12),justify="left")
  la8.pack() 
  la9=tk.Label(framew1,text='GUID:',font=("Times New Roman",12),justify="left")
  la9.pack()
  la18=tk.Label(framew1,text='TOPIC:\n\n\n\n',font=("Times New Roman",12),justify="left")
  la18.pack()
  
  img2=Image.open('F:/chenrec/image/wine_container.jpg')
  w,h=img2.size
  img2=resize(w,h,250,212,img2)
  photo3=ImageTk.PhotoImage(img2)
  imgLabel=tk.Label(framew1,image=photo3)
  imgLabel.pack(side='bottom')
  img3=Image.open('F:/chenrec/image/wine_container3.jpg')
  w,h=img3.size
  img3=resize(w,h,250,212,img3)
  photo4=ImageTk.PhotoImage(img3)
  imgLabel=tk.Label(framew1,image=photo4)
  imgLabel.pack(side='bottom')
  
  la10=tk.Label(framew2,text='Bronze',font=("Times New Roman",12),justify="center")
  la10.pack() 
  la11=tk.Label(framew2,text='H x W x D: 35.3 x 24.8 x 23.3 cm (13 7/8 x 9 3/4 x 9 3/16 in)',font=("Times New Roman",12),justify="center")
  la11.pack()
  la13=tk.Label(framew2,text='Vessel',font=("Times New Roman",12),justify="center")
  la13.pack()
  la14=tk.Label(framew2,text='Luoyang, Henan province, China',font=("Times New Roman",12),justify="center")
  la14.pack() 
  la15=tk.Label(framew2,text='ca. 1100 BCE',font=("Times New Roman",12),justify="center")
  la15.pack()
  la16=tk.Label(framew2,text='Early Western Zhou period',font=("Times New Roman",12),justify="center")
  la16.pack() 
  la17=tk.Label(framew2,text='Freer Gallery of Art and Arthur M. Sackler Gallery',font=("Times New Roman",12),justify="center")
  la17.pack()
  la19=tk.Label(framew2,text='http://n2t.net/ark:/65665/ye335879a27-d65c-4ae1-a94e-ee0429770c86',font=("Times New Roman",12),justify="center")
  la19.pack()
  la22=tk.Label(framew2,text='Dragon ;\nTaotie ;\nWestern Zhou dynasty (ca. 1050 - 771 BCE) ;\nWine ;\nChinese art',font=("Times New Roman",12),justify="left")
  la22.pack() 

  img4=Image.open('F:/chenrec/image/wine_container4.jpg')
  w,h=img4.size
  img4=resize(w,h,250,212,img4)
  photo5=ImageTk.PhotoImage(img4)
  imgLabel=tk.Label(framew2,image=photo5)
  imgLabel.pack(side='bottom')
  img5=Image.open('F:/chenrec/image/wine_container2.jpg')
  w,h=img5.size
  img5=resize(w,h,250,212,img5)
  photo6=ImageTk.PhotoImage(img5)
  imgLabel=tk.Label(framew2,image=photo6)
  imgLabel.pack(side='bottom')

  la20=tk.Label(w9,text=' ',font=("Times New Roman",10),justify="left")
  la20.pack(side='bottom')
  framew1.pack(side=tk.LEFT)
  framew2.pack(side=tk.RIGHT)

  w9.mainloop()

# ==============================================================================================
############################ P3-Process ############################
# ==============================================================================================

# 选择文件夹
def selectFile():
  global filepath
  filepath=askopenfilename()
  filename.set(filepath)        # 选择打开什么文件，返回文件名
  w1=tk.Toplevel(window)             # 设置变量filename的值
  w1.geometry('520x520+350+100')
  w1.title('Diffuse Map')          
  img = Image.open(filename.get())    
  w,h=img.size
  img=resize(w,h,500,500,img)
  photo=ImageTk.PhotoImage(img)
  la=tk.Label(w1, image=photo,width=500,height=500)
  la.pack()
  w1.mainloop()
  filepath=os.path.basename(os.path.dirname(filepath))

#开始重建
def reconstruct():
  os.system('start cmd.exe /K C:\\Windows\\System32\\cmd.exe')
 
# ==============================================================================================
############################ P4-reault show ############################
# ==============================================================================================

def btnclick9():
  webbrowser.open('http://127.0.0.1:5502/show/elephant.html')

def btnclick10():
  webbrowser.open('http://127.0.0.1:5502/show/baluster_vase.html')

def btnclick11():
  webbrowser.open('http://127.0.0.1:5502/show/beaker-shaped_vase.html')

def btnclick12():
  webbrowser.open('http://127.0.0.1:5502/show/incense.html')

def btnclick13():
  webbrowser.open('http://127.0.0.1:5502/show/kylix.html')

def btnclick14():
  webbrowser.open('http://127.0.0.1:5502/show/pottery.html')

def btnclick15():
  webbrowser.open('http://127.0.0.1:5502/show/stoneware.html')

def btnclick16():
  webbrowser.open('http://127.0.0.1:5502/show/wine_container.html')

window=tk.Tk()
w_box=800
h_box=600
window.title('基于可微蒙特卡洛渲染器的非朗伯体文物重建系统')
window.geometry('800x700+350+100')
#设置窗体的宽高和在屏幕上出现的位置 格式：宽x高+水平+垂直
filename = tk.StringVar()
outputpath = tk.StringVar()
filenewname = tk.StringVar()
#分页
note=ttk.Notebook()
note.place(relx=0.02,rely=0.02,relwidth=0.88,relheight=0.88)

# ==============================================================================================
#  第一模块
# ==============================================================================================

frame1=tk.Frame()
frame11=tk.Frame(frame1)
frame12=tk.Frame(frame1)
note.add(frame1,text="系统介绍")

canvas = tk.Canvas(frame11, width=800,height=300)
global photo66
photo66 = ImageTk.PhotoImage(file='F:/chenrec/image/back.jpg')

canvas.create_image(355, 100, image=photo66)
canvas.create_text(345,30,text='基于可微蒙特卡洛渲染器的非朗伯体文物重建系统',font=("黑体",16))
canvas.create_text(345,90,text='文物是人类文明发展过程中历史、艺术、科学价值的结晶，\n蕴含着丰富的历史文化信息，具有重要的政治、文化、\n科学价值，是全人类宝贵的历史文化遗产。',justify="center",font=("宋体",11))
canvas.create_text(345,160,text='文物三维数字化是实现文物由物质形态到数字形态转化的基础，\n通过数字化展示，可有效减少展品展出过程中的损耗，\n同时对文物材质等细节信息的提取，可用于指导文物修复工作，\n提高修复效率，一定程度上节省了文物修复的成本。',justify="center",font=("宋体",11))
canvas.create_text(345,230,text='本项目使用文物模拟数据，设计了基于可微蒙特卡洛渲染器的非朗伯体文物重建系统，\n支撑了非朗伯体文物三维模型SVBRDF和BSSRDF光学材质的高效恢复，\n旨在通过数字化展现文物的精神内核，传达文明的智慧与艺术的魅力。',justify="center",font=("Times New Roman",11))
canvas.pack()

photo1=ImageTk.PhotoImage(file='F:/chenrec/image/interface.jpg')
imgLabel=tk.Label(frame12,image=photo1,width=700,height=582)
imgLabel.pack()
frame11.pack()
frame12.pack(side=tk.BOTTOM)

# ==============================================================================================
#  第二模块
# ==============================================================================================

frame2=tk.Frame()
frame21=tk.Frame(frame2)
frame22=tk.Frame(frame2)
note.add(frame2,text="文物元数据")

img1=Image.open('F:/chenrec/image/elephant.jpg')
w,h=img1.size
img1=resize(w,h,340,110,img1)
photo2=ImageTk.PhotoImage(img1)
imgLabel=tk.Label(frame21,image=photo2,width=340,height=110)
imgLabel.pack()
bu1=ttk.Button(frame21,text='Document-elephant',bootstyle='dark',command=btnclick1)
bu1.pack()

img2=Image.open('F:/chenrec/image/f191.jpg')
w,h=img2.size
img2=resize(w,h,340,110,img2)
photo3=ImageTk.PhotoImage(img2)
imgLabel=tk.Label(frame21,image=photo3,width=340,height=110)
imgLabel.pack()
bu2=ttk.Button(frame21,text='Document-baluster_vase',bootstyle='dark',command=btnclick2)
bu2.pack()

img3=Image.open('F:/chenrec/image/f194.jpg')
w,h=img3.size
img3=resize(w,h,340,110,img3)
photo4=ImageTk.PhotoImage(img3)
imgLabel=tk.Label(frame21,image=photo4,width=340,height=110)
imgLabel.pack()
bu3=ttk.Button(frame21,text='Document-beaker-shaped vase',bootstyle='dark',command=btnclick3)
bu3.pack()

img4=Image.open('F:/chenrec/image/incense.jpg')
w,h=img4.size
img4=resize(w,h,340,110,img4)
photo5=ImageTk.PhotoImage(img4)
imgLabel=tk.Label(frame21,image=photo5,width=340,height=110)
imgLabel.pack()
bu4=ttk.Button(frame21,text='Document-incense',bootstyle='dark',command=btnclick4)
bu4.pack()

img5=Image.open('F:/chenrec/image/kylix.jpg')
w,h=img5.size
img5=resize(w,h,340,110,img5)
photo6=ImageTk.PhotoImage(img5)
imgLabel=tk.Label(frame22,image=photo6,width=340,height=110)
imgLabel.pack()
bu5=ttk.Button(frame22,text='Document-kylix',bootstyle='dark',command=btnclick5)
bu5.pack()

img6=Image.open('F:/chenrec/image/pottery.jpg')
w,h=img6.size
img6=resize(w,h,340,110,img6)
photo7=ImageTk.PhotoImage(img6)
imgLabel=tk.Label(frame22,image=photo7,width=340,height=110)
imgLabel.pack()
bu6=ttk.Button(frame22,text='Document-pottery',bootstyle='dark',command=btnclick6)
bu6.pack()

img7=Image.open('F:/chenrec/image/stoneware.jpg')
w,h=img7.size
img7=resize(w,h,340,110,img7)
photo8=ImageTk.PhotoImage(img7)
imgLabel=tk.Label(frame22,image=photo8,width=340,height=110)
imgLabel.pack()
bu7=ttk.Button(frame22,text='Document-stoneware',bootstyle='dark',command=btnclick7)
bu7.pack()

img8=Image.open('F:/chenrec/image/wine_container.jpg')
w,h=img8.size
img8=resize(w,h,340,110,img8)
photo9=ImageTk.PhotoImage(img8)
imgLabel=tk.Label(frame22,image=photo9,width=340,height=110)
imgLabel.pack()
bu8=ttk.Button(frame22,text='Document-wine_container',bootstyle='dark',command=btnclick8)
bu8.pack()

frame21.pack(side=tk.LEFT)
frame22.pack(side=tk.RIGHT)

# ==============================================================================================
#  第三模块
# ==============================================================================================

frame3=tk.Frame()
note.add(frame3,text="文物重建")
frame31=tk.Frame(frame3)
frame32=tk.Frame(frame3)

canvas = tk.Canvas(frame31, width=320,height=600)
global photo77
photo77 = ImageTk.PhotoImage(file='F:/chenrec/image/back2.jpg')
canvas.create_image(250, 100, image=photo77)
canvas.pack()

la5=ttk.Label(frame31,text='选择贴图文件',bootstyle='Light',font=("黑体",16),background='#8B4513')
la5.place(relx=0.23,rely=0.25)
bu5=ttk.Button(frame31, text='打开文件',bootstyle='dark',command=selectFile,width=10)
bu5.place(relx=0.3,rely=0.35)

la8=ttk.Label(frame31,text='开始重建',bootstyle='Light',font=("黑体",16),background='#8B4513')
la8.place(relx=0.3,rely=0.55)
bu10=ttk.Button(frame31,text='确定',bootstyle='dark',command=reconstruct,width=10)
bu10.place(relx=0.3,rely=0.65)

photo10=ImageTk.PhotoImage(file='F:/chenrec/image/background.jpg')
imgLabel=tk.Label(frame32,image=photo10,width=700,height=582,compound=tk.CENTER)
imgLabel.pack()

frame31.pack(side=tk.LEFT)
frame32.pack(side=tk.RIGHT)

# ==============================================================================================
#  第四模块
# ==============================================================================================

frame4=tk.Frame()
note.add(frame4,text="结果展示")

canvas = tk.Canvas(frame4, width=800,height=600)
photo = ImageTk.PhotoImage(file='F:/chenrec/image/back.jpg')
canvas.create_image(250, 100, image=photo)
canvas.pack()

la16=ttk.Label(frame4,text='Elephant',bootstyle='Inverse',font=('Times New Roman',18))
la16.place(relx=0.3,rely=0.1)
bu17=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick9)
bu17.place(relx=0.6,rely=0.1)

la17=ttk.Label(frame4,text='Baluster vase',bootstyle='Inverse',font=('Times New Roman',18))
la17.place(relx=0.27,rely=0.2)
bu18=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick10)
bu18.place(relx=0.6,rely=0.2)

la18=ttk.Label(frame4,text='Beaker-shaped vase',bootstyle='Inverse',font=('Times New Roman',18))
la18.place(relx=0.225,rely=0.3)
bu19=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick11)
bu19.place(relx=0.6,rely=0.3)

la19=ttk.Label(frame4,text='Incense',bootstyle='Inverse',font=('Times New Roman',18))
la19.place(relx=0.31,rely=0.4)
bu20=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick12)
bu20.place(relx=0.6,rely=0.4)

la20=ttk.Label(frame4,text='Kylix',bootstyle='Inverse',font=('Times New Roman',18))
la20.place(relx=0.324,rely=0.5)
bu21=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick13)
bu21.place(relx=0.6,rely=0.5)

la21=ttk.Label(frame4,text='Pottery',bootstyle='Inverse',font=('Times New Roman',18))
la21.place(relx=0.313,rely=0.6)
bu22=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick14)
bu22.place(relx=0.6,rely=0.6)

la22=ttk.Label(frame4,text='Stoneware',bootstyle='Inverse',font=('Times New Roman',18))
la22.place(relx=0.292,rely=0.7)
bu23=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick15)
bu23.place(relx=0.6,rely=0.7)

la23=ttk.Label(frame4,text='Wine-container',bootstyle='Inverse',font=('Times New Roman',18))
la23.place(relx=0.255,rely=0.8)
bu24=ttk.Button(frame4,text='SHOW',bootstyle='light',command=btnclick16)
bu24.place(relx=0.6,rely=0.8)

window.mainloop()