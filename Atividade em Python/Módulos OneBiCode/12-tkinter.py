import tkinter as tk

#criando a janela
window = tk.Tk()
window.geometry('300x150')
window.title('Somando números') 

#adicionando frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

#adicionando o label
label = tk.Label(frame,text='Soma')
label.pack(fill='x', expand=True)

#adicionando o input 
frase_lab = tk.Label(frame, text='Insira seus números:')
frase_lab.pack(fill='x', expand = True)

num_inp1 = tk.Entry(frame)
num_inp1.pack(fill='x', expand=True)

num_inp2 = tk.Entry(frame)
num_inp2.pack(fill='x', expand=True)

def click():
    try:
        n2 = float(num_inp1.get()) 
        n1 = float(num_inp2.get())
        resultado = n1 + n2
        label.config(text=f'soma: {resultado}')
    except:
        label.config(text='Valores invalidos')

#Criando botão

button = tk.Button(frame, text='trocar', command=click)
button.pack()


window.mainloop()