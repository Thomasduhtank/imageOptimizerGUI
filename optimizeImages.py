from PIL import Image
import PIL
import os
import glob
import sys
from resizeimage import resizeimage
import ctypes
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog as fd 


MessageBox = ctypes.windll.user32.MessageBoxW

maxWidth = 1000
maxWidthThumbnail = 300
optimizedPrefix = 'optimized_'
ThumbnailPrefix = 'thumb_'
OptimizationLevel = 80

configWindow = tk.Tk()
imageOptimizeDirectory = os.getcwd()
imageOptimizeDirectory= fd.askdirectory()
def handle_click():
    for root,dirs,file in os.walk(imageOptimizeDirectory):
        for image in file:
            if image.endswith(('jpg', 'png' )) and not "optimized_" in image and not "thumb_" in image :
                
                img = Image.open(os.path.join(root,image))
                img = resizeimage.resize_width(img, int(maxWidth), validate=False)
                img.save(os.path.join(root,optimizedPrefix+image),
                        optimize=True,
                        quality=int(OptimizationLevel))
                img = resizeimage.resize_width(img, int(maxWidthThumbnail), validate=False)
                img.save(os.path.join(root,ThumbnailPrefix+image))
    MessageBox(None, 'All images optimized!', 'Success!', 0) 
    sys.exit(0)

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=1, column=1)
labelMaxWidth = tk.Label(master=frame,text="Maximum Image Width")
labelMaxWidth.pack()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=1, column=2)
inputMaxWidth = tk.Entry(master=frame,width=30)
inputMaxWidth.pack()
inputMaxWidth.insert(0,str(maxWidth))

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=2, column=1)
labelImagePrefix = tk.Label(master=frame,text="Image Prefix")
labelImagePrefix.pack()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=2, column=2)
inputImagePrefix = tk.Entry(master=frame,width=30)
inputImagePrefix.pack()
inputImagePrefix.insert(0,str(optimizedPrefix))

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=3, column=1)
labelThumbnailMaxWidth = tk.Label(master=frame,text="Thumbnail Max Width")
labelThumbnailMaxWidth.pack()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=3, column=2)
inputThumbnailMaxWidth = tk.Entry(master=frame,width=30)
inputThumbnailMaxWidth.pack()
inputThumbnailMaxWidth.insert(0,str(maxWidthThumbnail))

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=4, column=1)
labelThumbnailPrefix = tk.Label(master=frame,text="Thumbnail Prefix")
labelThumbnailPrefix.pack()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=4, column=2)
inputThumbnailPrefix = tk.Entry(master=frame,width=30)
inputThumbnailPrefix.pack()
inputThumbnailPrefix.insert(0,str(ThumbnailPrefix))

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=5, column=1)
labelOptimizationLevel = tk.Label(master=frame,text="Optimization Level in %")
labelOptimizationLevel.pack()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=5, column=2)
inputOptimizationLevel = tk.Entry(master=frame,width=30)
inputOptimizationLevel.pack()
inputOptimizationLevel.insert(0,str(OptimizationLevel))

maxWidth = inputMaxWidth.get()
maxWidthThumbnail = inputThumbnailMaxWidth.get()
OptimizationLevel = inputOptimizationLevel.get()
optimizedPrefix = inputImagePrefix.get()
ThumbnailPrefix = inputThumbnailPrefix.get()

frame = tk.Frame(
            master=configWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=6, column=1)
button = tk.Button(master=frame,text="Start Optimizing!",command=handle_click).pack(fill=tk.X)




configWindow.mainloop()




