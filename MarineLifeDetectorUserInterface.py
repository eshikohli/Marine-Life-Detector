from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win = Tk()

# Set the size of the window

win.geometry("1200x800")
win.title('Marine Life Detector')

win.configure(bg='white')
main_font=('times', 20, 'bold')

# Create a Label to capture the Video frames



def show_frames(event=None):
    if pvid_label:
        pvid_label.destroy()

    """ global x
    if x == 0:
        vid_label.destroy()
    x += 1 """
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    classIds, scores, boxes = model.detect(cv2image, confThreshold=0.6, nmsThreshold=0.4)
    

    for (classId, score, box) in zip(classIds, scores, boxes):
        cv2.rectangle(cv2image, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                    color=(0, 255, 0), thickness=2)

        text = '%s: %.2f' % (classes[classId], score)
        cv2.putText(cv2image, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    color=(0, 255, 0), thickness=2)
    img = Image.fromarray(cv2image)

    width, height = img.size
    img_resized=img.resize((width//2,height//2))
    
    """ imgtk = ImageTk.PhotoImage(image = img)
    vid_label.imgtk = imgtk
    vid_label.configure(image=imgtk)
    vid_label.after(20, show_frames) """

    imgtk = ImageTk.PhotoImage(image = img_resized)
    vid_label.imgtk = imgtk
    vid_label.configure(image=imgtk)
    vid_label.after(20, show_frames)

#show_frames()

def pshow_frames(event=None):

    pcv2image= cv2.cvtColor(capm.read()[1],cv2.COLOR_BGR2RGB)
    pclassIds, pscores, pboxes = model.detect(pcv2image, confThreshold=0.6, nmsThreshold=0.4)
    

    for (pclassId, pscore, pbox) in zip(pclassIds, pscores, pboxes):
        cv2.rectangle(pcv2image, (pbox[0], pbox[1]), (pbox[0] + pbox[2], pbox[1] + pbox[3]),
                    color=(0, 255, 0), thickness=2)

        ptext = '%s: %.2f' % (classes[pclassId], pscore)
        cv2.putText(pcv2image, ptext, (pbox[0], pbox[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    color=(0, 255, 0), thickness=2)
    pimg = Image.fromarray(pcv2image)

    pwidth, pheight = pimg.size
    pimg_resized=pimg.resize((pwidth//3,pheight//3))
    
    """ imgtk = ImageTk.PhotoImage(image = img)
    vid_label.imgtk = imgtk
    vid_label.configure(image=imgtk)
    vid_label.after(20, show_frames) """

    pimgtk = ImageTk.PhotoImage(image = pimg_resized)
    pvid_label.imgtk = pimgtk
    pvid_label.configure(image=pimgtk)
    pvid_label.after(20, pshow_frames)

def downloadData(ci, b):
    with open('/Users/Eshi/Downloads/Data.txt', 'w') as f:
            for o in range(len(ci)):
                line = str(classes[ci[o]]) + ", " + str(b[o]) + "\n"
                f.write(line)

        
def ImageDetection(event=None):
    global img
    #f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png'), ('Jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename()
    #img=Image.open(filename)

    if "mov" not in filename.lower():

    #videocapture if mov file

        img = cv2.imread(filename)
    
        
        
        classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)
        
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                        color=(0, 255, 0), thickness=2)
        
            text = '%s: %.2f' % (classes[classId], score)
            cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        color=(0, 255, 0), thickness=2)
        

        cv2.imwrite('/Users/Eshi/Desktop/detectedopencv.jpg', img)
        #cv2.imshow('Image', img)
        img=Image.open('/Users/Eshi/Desktop/detectedopencv.jpg')
        width, height = img.size
        img_resized=img.resize((5*width//8,5*height//8))

        #Implement YOLO object detection here

        img=ImageTk.PhotoImage(img_resized)
        

        #Implement YOLO object detection here

        #img=ImageTk.PhotoImage(imgtk)
        numFishText = "Number of Fish Detected: " + str(len(boxes))
        #dButton = Button(win,image=img, highlightbackground="white")
        dButton.config(image=img, highlightbackground="white")
        dButton.grid(row = 2, column = 0)
        #numFishLabel = Label(win, text = numFishText, font = main_font, highlightbackground= "white")
        numFishLabel.config(bg = "white", text = numFishText, font = main_font, highlightbackground= "white")
        numFishLabel.grid(row = 3, column = 0)
        ddB.config(text = "Download Data (^d)", command=downloadData(classIds, scores), highlightbackground="white")
        ddB.grid(row = 4, column = 0)
        
        #win.bind('<Control-d>', downloadData(classIds,scores))
        #Edit the text to include variable which will contain number of fish detected


        #stri = ""
        """ for elem in scores:
            percent = elem*100
            percstr = str(percent)
            stri += percstr[:6]
            stri+= "%, "

        #newstri = str[:-2]
        accLabelText = "Confidence Percentages of Fish Detected: " + stri[:-2]
        accLabel = Label(win, text = accLabelText, font = main_font, highlightbackground= "white")
        accLabel.config(bg="white")
        accLabel.grid(row = 4, column = 0) """
    else:
        dButton.destroy()
        numFishLabel.destroy()
        ddB.destroy()
        pshow_frames()




Label(win, text = "Input Image/Video for Fish Detection", font = main_font, background="white").grid(row = 0, column = 0)
Label(win, text = "                                     ", background="white").grid(row = 0, column = 1)
Label(win, text = "Live Video for Fish Detection", font = main_font, background="white").grid(row = 0, column = 3)

with open('/Users/Eshi/Downloads/obj.names', 'r') as f:
    classes = f.read().splitlines()
    
net = cv2.dnn.readNetFromDarknet('/Users/Eshi/Downloads/yolov4-obj (1).cfg', '/Users/Eshi/Downloads/yolov4-obj_last.weights')

model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

Button(win, text='Choose File (^f)', command=ImageDetection, highlightbackground="white").grid(row = 1, column = 0)
win.bind('<Control-f>', ImageDetection)
#cap= cv2.VideoCapture("/Users/Eshi/Downloads/IMG_5282.MOV")
x = 0 
cap= cv2.VideoCapture(1)
capm= cv2.VideoCapture("/Users/Eshi/Desktop/Screen Recording 2022-05-10 at 6.59.15 PM.mov")
vid_label =Label(win)
vid_label.grid(row=2, column=3)
ddB = Button(win) 
numFishLabel = Label(win)
dButton = Button(win)

pvid_label =Label(win)
pvid_label.grid(row=2, column=0)

Button(win, text='Click Here to Start Live Stream (^v)', command=show_frames, highlightbackground="white").grid(row = 1, column = 3)
win.bind('<Control-v>', show_frames)

win.mainloop()