from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

# creating a global variable for the file extension
file=None
#declaring the getFile function 
#this function takes a widget as an argument
def getFile(w):

    global file
    #over writing the existing extension
    file=None
    #opening a window that allows the user to chosse a file
    file=askopenfilename()
    #Setting the file label to display the current files path
    w.config(text=file)
    #If the file is not a .gcode file
    if not file.endswith('.gcode') and file != "":
        #reset the file path
        file=None
        # reset the file path label
        w.config(text=" ")
        # alert the user with a pop out window that the file couldnt be 
        Alert("You entered a file with an incompatible extension.\n Please choose a file with the .gcode extension and try again","Wrong File Extension!!!")
    #if the file path is empty
    elif (file==""):
        # alert the user that they havent selected a file
        Alert("You have not selected any file.","Missing File")

#Defining the alert function
#this function creates an alert pop out and takes a message and window title as arguments
def Alert(notification,title):
    #creating a windo that appears in the foreground
    alert= tk.Toplevel()
    #This window cant be resized
    alert.resizable(False,False)
    # setting the backgroundcolor of the window
    alert.configure(background="#252527")
    #Sets the title to the varibale that was passed
    alert.title(title)
    #sets the body text to the notification and makes the text white
    message=tk.Label(alert, text=notification,foreground="white")
    #sets the background of the text to the color of the window
    message.configure(background="#252527")
    #places the message in the window
    message.pack(side="top",fill="x",pady=20)
    #the ok button that is used to destroy the alert
    okay= Button(alert,text="Okay",command= alert.destroy)
    okay.pack(pady=5)
    alert.mainloop()

# the issueFound function
# this function is depricated as it causes long hangups in run time
IssueFound=None
def isError(code , CurrLine , lineNum, window):
    
    if code in CurrLine:
                window.configure(state="normal")
                window.insert(END,"An ")
                window.insert(END,code,'flag')
                window.insert(END, " command was found on line ")
                window.insert(END, str(lineNum),'flag')
                window.insert(END,".\n\n")
                window.configure(state="disable")
                global IssueFound 
                IssueFound=True
                return(True)
    return()
        
# definintion of the checker function
# this function takes the text window for displaying errors as an argument

def checker(error):
    #defining the main checker function
    #this function will be used to:
    # 1) open the chosen gcode file
    # 2) read the file line by line
    # 3) check each line for gcode that could be potentially harmful to the 3d printer
    # 4) alert the user when harmful gcode is detected by the program
    global IssueFound
    IssueFound = False
    #If there is a file that can be checked run the program
    if file is not None and file!='':
        #Clear the current contents of the output box
        error.configure(state="normal")
        error.delete('1.0',END)
        error.configure(state="disable") 
        #print(file)
        
        #Opening the file that the user has selected to be checked
        #chosenFile=open(file,"r")
            
        ##testLine = ChosenFile.readline()
        ##print(testLine)
        
        #variable initialization for the checker function

        #keeps track of the current line that the program is on 
        currLineNumber=0
        #opens the file that has been chosen
        openedfile=open(file,"r")
        #for every line in that file
        for line in openedfile:
            #keep track of what line we are on 
            currLineNumber+=1
            #set the contents of the line to upper case
            line=line.upper()

            #actually checking the file for the bad commands using if statements rather than a function
            # after testing this was deemed more efficient than running a function for each command on each line

            #checking for the Commands 
            #if the command is found on the current line and the user desires for that command to be searched for
            #display a message saying that the command was found what line it was found on and display a brief description of the commmand

            if "M500" in line and checkM500.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"M500",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"Some settings will save to EEPROM!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE
            elif "M502" in line and checkM502.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"M502",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"Settings will factory reset!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE
            elif "G20" in line and checkG20.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"G20",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"Changes units to inches!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE
            elif "M304" in line and checkM304.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"M304",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"Will change the bed PID tuning!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE
            elif "M149" in line and checkM149.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"M149",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"May change the units for temperature!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE
            elif "M206" in line and checkM206.get()==1:
                error.configure(state="normal")
                error.insert(END,"A ")
                error.insert(END,"M206",'flag')
                error.insert(END, " command was found on line ")
                error.insert(END, str(currLineNumber),'flag')
                error.insert(END,".\n")
                error.insert(END,"Alters the home location!",'Message')
                error.insert(END,"\n\n")
                error.configure(state="disable")
                IssueFound=TRUE


        #if no issues are found in the file
        if not IssueFound:
            #alert the user that no issues have been located
            #Alert("No issues have been located.", "File Validated")
            error.configure(state="normal")
            error.insert(END," No issues have been located.",'Validated')
            error.configure(state="disable")
        
        openedfile.close()   
    #if the user hasnt entered a valid file prompt them too
    else:
        Alert("Please enter a file!!", "")



#the main function
def main():
    
    #creating the original window that is not resizable
    window = Tk()
    window.resizable(False,False)
    #window.geometry("500x300")
    #setting the windows background color
    window.configure(background="#252527")
    #setting the title of the window
    window.title("GCODE VALIDATOR")
    
    #making the file path label
    path=tk.Label(window,wraplength=200,anchor=W)
    path.configure(background="#252527",foreground="white")

    #making the file button that allows the user to open a window and select a file
    # this button calls the get path file
    fileBTN = Button( window, text="Choose a File", command= lambda: getFile(path))
    #fileBTN.pack(pady=10,padx=10)
    #placing the button and label in the window
    fileBTN.grid(row=0,column=1,columnspan=1,sticky=S,pady=10)
    path.grid(row=1,column=1,padx=20,sticky=N)

    #making a checkbox option for each command
    #then placing that command in a frame
    # then taking the frame and placing it in a cell in the window
    # the Check[command name] lines are what determines if the command was chosen to be searched for
    buttonArea=Frame(window)
    global checkM500
    checkM500=IntVar()
    M500=Checkbutton(buttonArea,text="M500", variable=checkM500)

    global checkM502
    checkM502=IntVar()
    M502=Checkbutton(buttonArea,text="M502", variable=checkM502)

    global checkG20
    checkG20=IntVar()
    G20=Checkbutton(buttonArea,text="G20", variable=checkG20)

    global checkM304
    checkM304=IntVar()
    M304=Checkbutton(buttonArea,text="M304", variable=checkM304)

    global checkM149
    checkM149=IntVar()
    M149=Checkbutton(buttonArea,text="M149", variable=checkM149)

    global checkM206
    checkM206=IntVar()
    M206=Checkbutton(buttonArea,text="M206", variable=checkM206)

    # creating the output window
    Errorwindow=Text(window,width=45,height=14)
    Errorwindow.insert(END,"This program was designed to check for \nmalicious commands in .GCODE files that have been shared over the internet.\n\n\nJust choose the file and commands that you \nwant to check for. Then press the check \nbutton. \n\nHappy Printing!!")
    Errorwindow.configure(state="disable",background="#333333",foreground="white")
    Errorwindow.tag_config('flag',background="yellow",foreground="red")
    Errorwindow.tag_config('Validated',background="#90ee90",foreground="green")
    Errorwindow.tag_config('Message',foreground="red")

    runChecker = Button (window , text="Check for Malicious G-Code",command=lambda:checker(Errorwindow) )
    runChecker.grid(row=4,column=1,pady=10,padx=10)

    tickLabel=tk.Label(buttonArea)
    tickLabel.configure(text="Select Commands")
    tickLabel.grid(row=0,column=1)

    #greySpace=tk.Label(buttonArea)
    #greySpace.configure(background="#252527")
    #greySpace.grid(row=0,column=0)
    #greySpace.grid(row=0,column=2)

    M500.grid(row=1,column=0,sticky=E)
    M502.grid(row=1,column=1)
    G20.grid(row=1,column=2,sticky=W)
    M304.grid(row=2,column=1)
    M149.grid(row=2,column=0)
    M206.grid(row=2,column=2)


    buttonArea.grid(row=2,column=1,pady=10)

    imageFrame = tk.Frame(window,background="#252527")
    imageFrame.grid(row=0,column=0,sticky=N)
    #logoImage = tk.PhotoImage(file = sys._MEIPASS + "\logo.png")
    logoImage = tk.PhotoImage(file ="logo.png")
    logoImagePack = tk.Label(imageFrame, image = logoImage,background="#252527")
    logoImagePack.grid(row=0,column=0,sticky=N)

    Errorwindow.grid(row=0,column=2,pady=10,padx=10,rowspan=5,sticky=N)
    mainloop()

main()





