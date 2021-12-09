# Basic tkinter template
from tkinter import *
root=Tk()
root.title("Fibonacci Series")
root.geometry("450x250")

inputvar=Entry(root)
label_series=Label(root, text="Fibonacci Series: ")
label_flower=Label(root)
label_spiral=Label(root)

def fibonacci():
    number=int(inputvar.get())
    print(number)
    first_num=0
    second_num=1
    sum=0
    counter=1
    while(counter<=number):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        first_num=second_num
        second_num=sum
        sum=first_num+second_num
    label_flower["text"]="Flower is fully bloomed"
    label_spiral["text"]="Total spirals are "+str(sum)

btn=Button(root,text="Show Fibonacci Series", command=fibonacci)
label_series.pack()
inputvar.pack()
btn.pack()
label_flower.pack()
label_spiral.pack()
# tkinter basic template end statement
root.mainloop()