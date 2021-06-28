

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import os.path

def egcd(a, b): 
	x,y, u,v = 0,1, 1,0
	while a != 0: 
		q, r = b//a, b%a 
		m, n = x-u*q, y-v*q 
		b,a, x,y, u,v = a,r, u,v, m,n 
	gcd = b 
	return gcd, x, y 

def modinv(a, m): 
	gcd, x, y = egcd(a, m) 
	if gcd != 1: 
		return None # modular inverse does not exist 
	else: 
		return x % m 

def encrypt_fun():

   text= Scrolledtext1.get(1.0,tk.END)
   key=[]
   Scrolledtext1_2.delete(1.0,tk.END)

   try:
       key=[int(Entry1.get()),int(Entry2.get())]
   except:
       Scrolledtext1_2.insert(1.0,":-- key should be interger value --:")
       return
   y=modinv(int(key[0]),26)
   Scrolledtext1_2.delete(1.0,tk.END)

   if(y==None):
       Scrolledtext1_2.insert(1.0,":-- Modulo inv of key1 and 26 is not possible. please try another key1 --:")
       return
   small_list=[]
   for i in range(0,len(text)):
       if(text[i].islower()):
           small_list.append(i)
   text=text.upper()
   c=""
   for i in text:
       if ord(i) in range(ord('A'),ord('Z')):
           c=c+chr((( key[0]*(ord(i) - ord('A')) + key[1] ) % 26)+ ord('A'))
       else:
           c=c+i
   
 
   print(c)
   cipher_text=""
   for j in range(0,len(text)):
       if j in small_list:
           cipher_text+=c[j].lower()
       else:
           cipher_text+=c[j]
   Scrolledtext1_2.insert(1.0,cipher_text)
   

def decrypt_fun(): 
    
    
   text= Scrolledtext1_2.get(1.0,tk.END)
   key=[]
   Scrolledtext1.delete(1.0,tk.END)

   try:
       key=[int(Entry1_1.get()),int(Entry2_2.get())]
   except:
       Scrolledtext1.insert(1.0,":-- key should be interger value --:")
       return

   y=modinv(int(key[0]),26)

   if(y==None):
       Scrolledtext1.insert(1.0,":-- Modulo inv of key1 and 26 is not possible. please try another key1 --:")
       return
   small_list=[]
   for i in range(0,len(text)):
       if(text[i].islower()):
           small_list.append(i)
   text=text.upper()
   c=""
   for i in text:
       if ord(i) in range(ord('A'),ord('Z')):
           c=c+chr((( modinv(key[0], 26)*(ord(i) - ord('A') - key[1]))% 26) + ord('A'))
       else:
           c=c+i
   print(c)
   cipher_text=""
   for j in range(0,len(text)):
       if j in small_list:
           cipher_text+=c[j].lower()
       else:
           cipher_text+=c[j]
   Scrolledtext1.insert(1.0,cipher_text)
	



_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
    " roman -underline 0 -overstrike 0"
font11 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
    "roman -underline 0 -overstrike 0"
style = ttk.Style()
if sys.platform == "win32":
    style.theme_use('winnative')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])
top=tk.Tk()
top.geometry("1035x500")
top.title("New Toplevel")
top.configure(background="#1e1e1e")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

TSeparator1 = ttk.Separator(top)
TSeparator1.place(relx=0.488, rely=0.08, relheight=0.92)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(top)
TSeparator2.place(relx=0.0, rely=0.08, relwidth=0.995)

Additive_encryption = tk.Label(top)
Additive_encryption.place(relx=0.01, rely=0.0, height=31, width=168)

Additive_encryption.configure(activebackground="#f9f9f9")
Additive_encryption.configure(activeforeground="black")
Additive_encryption.configure(background="#1e1e1e")
Additive_encryption.configure(disabledforeground="#176cff")
Additive_encryption.configure(font=font11)
Additive_encryption.configure(foreground="#197dff")
Additive_encryption.configure(highlightbackground="#d9d9d9")
Additive_encryption.configure(highlightcolor="black")
Additive_encryption.configure(text='''Affine Cipher''')

Encryption_label = tk.Label(top)
Encryption_label.place(relx=0.169, rely=0.13, height=21, width=138)
Encryption_label.configure(activebackground="#f9f9f9")
Encryption_label.configure(activeforeground="black")
Encryption_label.configure(background="#1e1e1e")
Encryption_label.configure(disabledforeground="#176cff")
Encryption_label.configure(font=font12)
Encryption_label.configure(foreground="#197dff")
Encryption_label.configure(highlightbackground="#d9d9d9")
Encryption_label.configure(highlightcolor="black")
Encryption_label.configure(text='''Encryption''')

k1 = tk.Label(top)
k1.place(relx=0.0, rely=0.24, height=21, width=138)
k1.configure(activebackground="#f9f9f9")
k1.configure(activeforeground="black")
k1.configure(background="#1e1e1e")
k1.configure(disabledforeground="#176cff")
k1.configure(foreground="#197dff")
k1.configure(highlightbackground="#d9d9d9")
k1.configure(highlightcolor="black")
k1.configure(text='''First Key ( k1 ) :''')

k2 = tk.Label(top)
k2.place(relx=0.222, rely=0.24, height=21, width=138)
k2.configure(activebackground="#f9f9f9")
k2.configure(activeforeground="black")
k2.configure(background="#1e1e1e")
k2.configure(disabledforeground="#176cff")
k2.configure(foreground="#197dff")
k2.configure(highlightbackground="#d9d9d9")
k2.configure(highlightcolor="black")
k2.configure(text='''Second Key ( k2 ) :''')

plain_text_label = tk.Label(top)
plain_text_label.place(relx=0.024, rely=0.31, height=21, width=168)
plain_text_label.configure(activebackground="#f9f9f9")
plain_text_label.configure(activeforeground="black")
plain_text_label.configure(background="#1e1e1e")
plain_text_label.configure(disabledforeground="#176cff")
plain_text_label.configure(foreground="#197dff")
plain_text_label.configure(highlightbackground="#d9d9d9")
plain_text_label.configure(highlightcolor="black")
plain_text_label.configure(text='''Plain Text  (Orignal Message ) :''')



Entry1 = tk.Entry(top)
Entry1.place(relx=0.135, rely=0.25,height=20, relwidth=0.071)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font=font10)
Entry1.configure(foreground="#000000")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="black")
Entry1.configure(selectbackground="#c4c4c4")
Entry1.configure(selectforeground="black")

Entry2 = tk.Entry(top)
Entry2.place(relx=0.348, rely=0.24,height=20, relwidth=0.071)
Entry2.configure(background="white")
Entry2.configure(disabledforeground="#a3a3a3")
Entry2.configure(font=font10)
Entry2.configure(foreground="#000000")
Entry2.configure(highlightbackground="#d9d9d9")
Entry2.configure(highlightcolor="black")
Entry2.configure(insertbackground="black")
Entry2.configure(selectbackground="#c4c4c4")
Entry2.configure(selectforeground="black")

from tkinter.scrolledtext import ScrolledText
Scrolledtext1 = ScrolledText(top)
Scrolledtext1.place(relx=0.029, rely=0.38, relheight=0.502
        , relwidth=0.436)
Scrolledtext1.configure(background="white")
Scrolledtext1.configure(font=font9)
Scrolledtext1.configure(foreground="black")
Scrolledtext1.configure(highlightbackground="#d9d9d9")
Scrolledtext1.configure(highlightcolor="black")
Scrolledtext1.configure(insertbackground="black")
Scrolledtext1.configure(insertborderwidth="3")
Scrolledtext1.configure(selectbackground="#c4c4c4")
Scrolledtext1.configure(selectforeground="black")
Scrolledtext1.configure(width=10)
Scrolledtext1.configure(wrap="none")

Button1 = tk.Button(top)
Button1.place(relx=0.391, rely=0.92, height=24, width=77)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#0f66d8")
Button1.configure(command=encrypt_fun)
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#f4fcfb")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(relief="flat")
Button1.configure(text='''Encrypt''')

Decryption_label = tk.Label(top)
Decryption_label.place(relx=0.676, rely=0.13, height=21, width=138)
Decryption_label.configure(activebackground="#f9f9f9")
Decryption_label.configure(activeforeground="black")
Decryption_label.configure(background="#1e1e1e")
Decryption_label.configure(disabledforeground="#176cff")
Decryption_label.configure(font=font12)
Decryption_label.configure(foreground="#197dff")
Decryption_label.configure(highlightbackground="#d9d9d9")
Decryption_label.configure(highlightcolor="black")
Decryption_label.configure(text='''Decryption''')

k1_1 = tk.Label(top)
k1_1.place(relx=0.498, rely=0.24, height=21, width=128)
k1_1.configure(activebackground="#f9f9f9")
k1_1.configure(activeforeground="black")
k1_1.configure(background="#1e1e1e")
k1_1.configure(disabledforeground="#176cff")
k1_1.configure(foreground="#197dff")
k1_1.configure(highlightbackground="#d9d9d9")
k1_1.configure(highlightcolor="black")
k1_1.configure(text='''First Key ( k1 ) :''')

Entry1_1 = tk.Entry(top)
Entry1_1.place(relx=0.633, rely=0.24,height=20, relwidth=0.071)
Entry1_1.configure(background="white")
Entry1_1.configure(disabledforeground="#a3a3a3")
Entry1_1.configure(font=font10)
Entry1_1.configure(foreground="#000000")
Entry1_1.configure(highlightbackground="#d9d9d9")
Entry1_1.configure(highlightcolor="black")
Entry1_1.configure(insertbackground="black")
Entry1_1.configure(selectbackground="#c4c4c4")
Entry1_1.configure(selectforeground="black")

k2_2 = tk.Label(top)
k2_2.place(relx=0.725, rely=0.23, height=21, width=138)
k2_2.configure(activebackground="#f9f9f9")
k2_2.configure(activeforeground="black")
k2_2.configure(background="#1e1e1e")
k2_2.configure(disabledforeground="#176cff")
k2_2.configure(foreground="#197dff")
k2_2.configure(highlightbackground="#d9d9d9")
k2_2.configure(highlightcolor="black")
k2_2.configure(text='''Second Key ( k2 ) :''')

Entry2_2 = tk.Entry(top)
Entry2_2.place(relx=0.86, rely=0.24,height=20, relwidth=0.071)
Entry2_2.configure(background="white")
Entry2_2.configure(disabledforeground="#a3a3a3")
Entry2_2.configure(font=font10)
Entry2_2.configure(foreground="#000000")
Entry2_2.configure(highlightbackground="#d9d9d9")
Entry2_2.configure(highlightcolor="black")
Entry2_2.configure(insertbackground="black")
Entry2_2.configure(selectbackground="#c4c4c4")
Entry2_2.configure(selectforeground="black")

plain_text_label_10 = tk.Label(top)
plain_text_label_10.place(relx=0.507, rely=0.31, height=21
        , width=208)
plain_text_label_10.configure(activebackground="#f9f9f9")
plain_text_label_10.configure(activeforeground="black")
plain_text_label_10.configure(background="#1e1e1e")
plain_text_label_10.configure(disabledforeground="#176cff")
plain_text_label_10.configure(foreground="#197dff")
plain_text_label_10.configure(highlightbackground="#d9d9d9")
plain_text_label_10.configure(highlightcolor="black")
plain_text_label_10.configure(text='''Cipher Text ( Encrypted Message ) :''')

Scrolledtext1_2 = ScrolledText(top)
Scrolledtext1_2.place(relx=0.522, rely=0.38, relheight=0.502
        , relwidth=0.445)
Scrolledtext1_2.configure(background="white")
Scrolledtext1_2.configure(font=font9)
Scrolledtext1_2.configure(foreground="black")
Scrolledtext1_2.configure(highlightbackground="#d9d9d9")
Scrolledtext1_2.configure(highlightcolor="black")
Scrolledtext1_2.configure(insertbackground="black")
Scrolledtext1_2.configure(insertborderwidth="3")
Scrolledtext1_2.configure(selectbackground="#c4c4c4")
Scrolledtext1_2.configure(selectforeground="black")
Scrolledtext1_2.configure(width=10)
Scrolledtext1_2.configure(wrap="none")

Button1_11 = tk.Button(top)
Button1_11.place(relx=0.889, rely=0.92, height=24, width=77)
Button1_11.configure(activebackground="#ececec")
Button1_11.configure(activeforeground="#000000")
Button1_11.configure(background="#2172ff")
Button1_11.configure(command=decrypt_fun)
Button1_11.configure(disabledforeground="#1269a3")
Button1_11.configure(foreground="#fafbff")
Button1_11.configure(highlightbackground="#d9d9d9")
Button1_11.configure(highlightcolor="black")
Button1_11.configure(pady="0")
Button1_11.configure(relief="flat")
Button1_11.configure(text='''Decrypt''')

Label1 = tk.Label(top,text="Inoneticx Technologies Pvt Ltd,Lucknow")
Label1.place(relx=0.760, rely=0.0, height=41, width=250)
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="black")
Label1.configure(background="#1c1c1c")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="white")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")


top.mainloop()