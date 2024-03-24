from tkinter import *
from Diagram import *;

options = ["Intersection", "Union", "Complement", "Difference"]

def visualization():
    try:
        set_a = set(map(str,first_text_entry.get().split()))
        set_b = set(map(str,second_text_entry.get().split()))

        diagram = Diagram()
        if x.get() == 0:
            diagram.draw_venn(set_a, set_b, "intersection")
        elif x.get() == 1:
            diagram.draw_venn(set_a, set_b, "union")
        elif x.get() == 2:
            diagram.draw_venn(set_a,set_b, "complement")
        elif x.get() == 3:
            diagram.draw_venn(set_a,set_b, "difference")
    except:
        Label(window, text="Invalid input entered. Try again and look at the example above",font=('Arial', 40, 'bold'),fg='#D36135',bg="#CACAAA",border=50).grid()

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



first_text = Label(window, text="Enter elments of Set 1 seperated by a space: ",bg="#CACAAA",fg="#D36135",font=('Arial', 15, 'bold')).grid() #Creates label
first_text_entry = Entry(window)
first_text_entry.grid()#Creates a new entry widget (a single line input field)

second_text = Label(window, text="Enter elments of Set 2 seperated by a space: ",bg="#CACAAA",fg="#D36135",font=('Arial', 15, 'bold')).grid()
second_text_entry = Entry(window) #Creates a new entry widget (a single line input field)
second_text_entry.grid()

submitButton = Button(window, text="Visualise",width=10,bg="#25CED1",fg='white',command=visualization).grid() #Creates a submit button


window.mainloop() # places window on computer screen and listens for events
