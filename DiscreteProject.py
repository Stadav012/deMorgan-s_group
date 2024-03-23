from tkinter import *

options = ["Intersection", "Union", "Complement", "Difference"]

def visualization():
    if x.get() == 0:
        print("somet")
    elif x.get() == 1:
        print("someth")
    elif x.get() == 2:
        print("somethin")
    elif x.get() == 3:
        print("something")

window = Tk() #Instantiate an instance of a window
window.geometry("1020x700")
window.config(background="#CACAAA")
window.title("Set Visualizer")


Welcome_label = Label(window, text="Welcome to Set Visualizer",font=('Arial', 40, 'bold'),fg='#D36135',bg="#CACAAA",border=50) #Creates a text label on the window
User_action = Label(window,text="Choose one of the set operators below",font=('Arial', 40, 'bold'),fg='#D36135',bg="#CACAAA",padx=20)
Welcome_label.grid() #Center the label variable
User_action.grid()

# label.place(x = 100,y = 0 ) #Place label variable in coordinate chosen by the computer programmer

x = IntVar()
for i in range(len(options)):
    radiobutton = Radiobutton(window, 
                              text=options[i], #Adds text to radio buttons
                              variable=x, #Groups radio buttons together if they share the same variable
                              value=i, #Assigns each radio button a different value
                              bg="#CACAAA",
                              fg='purple',
                            #   padx=50,
                              font=("Impact",30,'underline')
                              
                              )
    radiobutton.grid()
    # radiobutton.grid(side=LEFT,anchor=CENTER)



first_text = Label(window, text="Enter Set 1: ",bg="#CACAAA",fg="#D36135",font=('Arial', 15, 'bold')).grid() #Creates label 
first_text_entry = Entry(window).grid() #Creates a new entry widget (a single line input field)

second_text = Label(window, text="Enter Set 2: ",bg="#CACAAA",fg="#D36135",font=('Arial', 15, 'bold')).grid()
second_text_entry = Entry(window).grid() #Creates a new entry widget (a single line input field)

submitButton = Button(window, text="Visualise",width=10,bg="#25CED1",fg='white',command=visualization).grid() #Creates a submit button





window.mainloop() # places window on computer screen and listens for events
