# -*- coding: utf-8 -*-
"""

@author: mukul kirti verma
"""

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


import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def multiplicative_inverse(e, phi):
	g, x, y = extended_gcd(e, phi)
	if g != 1:
		cipher_dataa.set(("e, phi inverse not possible"))
	return x % phi
 

'''
Tests to see if a number is prime.
'''

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def ENCRYPT():
    p=int(pp.get())
    q=int(qq.get())
    e=int(ee.get())
    plain_text=plain_dataa.get()
    if not (is_prime(p) and is_prime(q)):
        cipher_dataa.set('p,q Both numbers must be prime.')
        return
    elif p == q:
        cipher_dataa.set('p and q cannot be equal')
        return
    #n = pq
    n = p * q
    #Phi is the totient of n
    phi = (p-1) * (q-1)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    if(g!=1):
        cipher_dataa.set("e and phi are not prime Choose another e :" )
        
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    ee.set(str(e))
    d11.set(str(d))
    nn.set(str(n))
    n11.set(str(n))
    n22.set(str(n))
    Pk_ee2.set(str(e))
    phi_nn.set(str(phi))
    c_t=encrypt2((e,n), plain_text)
    cipher_dataa.set(str(c_t))
    
    

def encrypt2(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    cipher=""
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    for char in plaintext:
        cipher=cipher+str((ord(char) ** key) % n)+ " "
    #Return the array of bytes
    return cipher
"""def decrypt():
    plain_dataa.set(" ")
    key=int(d22.get())
    n=int(n33.get())
    
    ciphertext=cipher_dataa.get().split(" ")
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    plain_dataa.set(''.join(plain))"""
    
def decryption():
    plain_dataa.set(" ")
    key=int(d22.get())
    n=int(n33.get())
    
    cipher_t=cipher_dataa.get().split(" ")
    ciphertext=[]
    for i in cipher_t[0:len(cipher_t)-1:1]:
        ciphertext.append(int(i))
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    plain_dataa.set(''.join(plain))
    
sys.stdout.flush()

top=tk.Tk()
top.geometry("911x655+-3+-10")
top.title("AIO")
top.configure(relief="ridge")
top.configure(background="#303030")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

Label1 = tk.Label(top)
Label1.place(relx=0.768, rely=0.015, height=31, width=204)
Label1.configure(activebackground="#303030")
Label1.configure(activeforeground="white")
Label1.configure(activeforeground="black")
Label1.configure(background="#303030")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#1caafc")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
'''global _img0
_img0 = tk.PhotoImage(file="inoneticx.png")
Label1.configure(image=_img0)

'''
TSeparator1 = ttk.Separator(top)
TSeparator1.place(relx=0.0, rely=0.076, relwidth=0.999)

TSeparator2 = ttk.Separator(top)
TSeparator2.place(relx=0.494, rely=0.076, relheight=0.885)
TSeparator2.configure(orient="vertical")

TSeparator3 = ttk.Separator(top)
TSeparator3.place(relx=0.0, rely=0.244, relwidth=0.494)

Label1_1 = tk.Label(top)
Label1_1.place(relx=0.187, rely=0.092, height=21, width=94)
Label1_1.configure(activebackground="#303030")
Label1_1.configure(activeforeground="white")
Label1_1.configure(activeforeground="black")
Label1_1.configure(background="#303030")
Label1_1.configure(disabledforeground="#a3a3a3")
Label1_1.configure(foreground="#1caafc")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''Input :''')

Label1_2 = tk.Label(top)
Label1_2.place(relx=0.022, rely=0.137, height=21, width=154)
Label1_2.configure(activebackground="#303030")
Label1_2.configure(activeforeground="white")
Label1_2.configure(activeforeground="black")
Label1_2.configure(background="#303030")
Label1_2.configure(disabledforeground="#a3a3a3")
Label1_2.configure(foreground="#1caafc")
Label1_2.configure(highlightbackground="#d9d9d9")
Label1_2.configure(highlightcolor="black")
Label1_2.configure(text='''Co-Prime Nubers (p) :''')

Label1_3 = tk.Label(top)
Label1_3.place(relx=0.307, rely=0.137, height=21, width=54)
Label1_3.configure(activebackground="#303030")
Label1_3.configure(activeforeground="white")
Label1_3.configure(activeforeground="black")
Label1_3.configure(background="#303030")
Label1_3.configure(disabledforeground="#a3a3a3")
#Label1_3.configure(font=font12)
Label1_3.configure(foreground="#1caafc")
Label1_3.configure(highlightbackground="#d9d9d9")
Label1_3.configure(highlightcolor="black")
Label1_3.configure(text='''&  (q) :''')
        
pp=tk.StringVar()

p = tk.Entry(top,text=pp)
p.place(relx=0.198, rely=0.137,height=20, relwidth=0.092)
p.configure(background="#1e1e1e")
p.configure(disabledforeground="#a3a3a3")
p.configure(font="TkFixedFont")
p.configure(foreground="#30baff")
p.configure(highlightbackground="#d9d9d9")
p.configure(highlightcolor="black")
p.configure(insertbackground="#33b4ff")
p.configure(selectbackground="#c4c4c4")
p.configure(selectforeground="black")

qq=tk.StringVar()

q = tk.Entry(top,text=qq)
q.place(relx=0.373, rely=0.137,height=20, relwidth=0.092)
q.configure(background="#1e1e1e")
q.configure(disabledforeground="#a3a3a3")
q.configure(font="TkFixedFont")
q.configure(foreground="#30baff")
q.configure(highlightbackground="#d9d9d9")
q.configure(highlightcolor="black")
q.configure(insertbackground="#33b4ff")
q.configure(selectbackground="#c4c4c4")
q.configure(selectforeground="black")

TSeparator4 = ttk.Separator(top)
TSeparator4.place(relx=0.0, rely=0.458, relwidth=0.494)

Label1_1 = tk.Label(top)
Label1_1.place(relx=-0.005, rely=0.183, height=21, width=154)
Label1_1.configure(activebackground="#303030")
Label1_1.configure(activeforeground="white")
Label1_1.configure(activeforeground="black")
Label1_1.configure(background="#303030")
Label1_1.configure(disabledforeground="#a3a3a3")
#Label1_1.configure(font=font12)
Label1_1.configure(foreground="#1caafc")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''Public Key (e) :''')

ee=tk.StringVar()

e = tk.Entry(top,text=ee)
e.place(relx=0.198, rely=0.183,height=20, relwidth=0.092)
e.configure(background="#1e1e1e")
e.configure(disabledforeground="#a3a3a3")
e.configure(font="TkFixedFont")
e.configure(foreground="#30baff")
e.configure(highlightbackground="#d9d9d9")
e.configure(highlightcolor="black")
e.configure(insertbackground="#33b4ff")
e.configure(selectbackground="#c4c4c4")
e.configure(selectforeground="black")

Label1_4 = tk.Label(top)
Label1_4.place(relx=-0.005, rely=0.305, height=21, width=124)
Label1_4.configure(activebackground="#303030")
Label1_4.configure(activeforeground="white")
Label1_4.configure(activeforeground="black")
Label1_4.configure(background="#303030")
Label1_4.configure(disabledforeground="#a3a3a3")
#Label1_4.configure(font=font12)
Label1_4.configure(foreground="#1caafc")
Label1_4.configure(highlightbackground="#d9d9d9")
Label1_4.configure(highlightcolor="black")
Label1_4.configure(text='''Value of n :''')

nn=tk.StringVar()

n = tk.Entry(top,text=nn)
n.place(relx=0.198, rely=0.305,height=20, relwidth=0.092)
n.configure(background="#1e1e1e")
n.configure(disabledforeground="#a3a3a3")
n.configure(font="TkFixedFont")
n.configure(foreground="#30baff")
n.configure(highlightbackground="#d9d9d9")
n.configure(highlightcolor="black")
n.configure(insertbackground="#33b4ff")
n.configure(selectbackground="#c4c4c4")
n.configure(selectforeground="black")

Label1_5 = tk.Label(top)
Label1_5.place(relx=0.132, rely=0.26, height=21, width=184)
Label1_5.configure(activebackground="#303030")
Label1_5.configure(activeforeground="white")
Label1_5.configure(activeforeground="black")
Label1_5.configure(background="#303030")
Label1_5.configure(disabledforeground="#a3a3a3")
#Label1_5.configure(font=font12)
Label1_5.configure(foreground="#1caafc")
Label1_5.configure(highlightbackground="#d9d9d9")
Label1_5.configure(highlightcolor="black")
Label1_5.configure(text='''Computed Variables :''')

Label1_2 = tk.Label(top)
Label1_2.place(relx=0.307, rely=0.305, height=21, width=54)
Label1_2.configure(activebackground="#303030")
Label1_2.configure(activeforeground="white")
Label1_2.configure(activeforeground="black")
Label1_2.configure(background="#303030")
Label1_2.configure(disabledforeground="#a3a3a3")
#Label1_2.configure(font=font12)
Label1_2.configure(foreground="#1caafc")
Label1_2.configure(highlightbackground="#d9d9d9")
Label1_2.configure(highlightcolor="black")
Label1_2.configure(text='''phi(n) :''')

phi_nn=tk.StringVar()

phi_n = tk.Entry(top,text=phi_nn)
phi_n.place(relx=0.373, rely=0.305,height=20, relwidth=0.092)
phi_n.configure(background="#1e1e1e")
phi_n.configure(disabledforeground="#a3a3a3")
phi_n.configure(font="TkFixedFont")
phi_n.configure(foreground="#30baff")
phi_n.configure(highlightbackground="#d9d9d9")
phi_n.configure(highlightcolor="black")
phi_n.configure(insertbackground="#33b4ff")
phi_n.configure(selectbackground="#c4c4c4")
phi_n.configure(selectforeground="black")

Label1_6 = tk.Label(top)
Label1_6.place(relx=-0.027, rely=0.351, height=21, width=184)
Label1_6.configure(activebackground="#303030")
Label1_6.configure(activeforeground="white")
Label1_6.configure(activeforeground="black")
Label1_6.configure(background="#303030")
Label1_6.configure(disabledforeground="#a3a3a3")
#Label1_6.configure(font=font12)
Label1_6.configure(foreground="#1caafc")
Label1_6.configure(highlightbackground="#d9d9d9")
Label1_6.configure(highlightcolor="black")
Label1_6.configure(text='''Public Key (e) :''')

Label1_3 = tk.Label(top)
Label1_3.place(relx=0.296, rely=0.351, height=21, width=64)
Label1_3.configure(activebackground="#303030")
Label1_3.configure(activeforeground="white")
Label1_3.configure(activeforeground="black")
Label1_3.configure(background="#303030")
Label1_3.configure(disabledforeground="#a3a3a3")
#Label1_3.configure(font=font12)
Label1_3.configure(foreground="#1caafc")
Label1_3.configure(highlightbackground="#d9d9d9")
Label1_3.configure(highlightcolor="black")
Label1_3.configure(text='''& (n) :''')

Pk_ee2=tk.StringVar()

Pk_e = tk.Entry(top,text=Pk_ee2)
Pk_e.place(relx=0.198, rely=0.351,height=20, relwidth=0.092)
Pk_e.configure(background="#1e1e1e")
Pk_e.configure(disabledforeground="#a3a3a3")
Pk_e.configure(font="TkFixedFont")
Pk_e.configure(foreground="#30baff")
Pk_e.configure(highlightbackground="#d9d9d9")
Pk_e.configure(highlightcolor="black")
Pk_e.configure(insertbackground="#33b4ff")
Pk_e.configure(selectbackground="#c4c4c4")
Pk_e.configure(selectforeground="black")


n11=tk.StringVar()

n1 = tk.Entry(top,text=n11)
n1.place(relx=0.373, rely=0.351,height=20, relwidth=0.092)
n1.configure(background="#1e1e1e")
n1.configure(disabledforeground="#a3a3a3")
n1.configure(font="TkFixedFont")
n1.configure(foreground="#30baff")
n1.configure(highlightbackground="#d9d9d9")
n1.configure(highlightcolor="black")
n1.configure(insertbackground="#33b4ff")
n1.configure(selectbackground="#c4c4c4")
n1.configure(selectforeground="black")

Label1_7 = tk.Label(top)
Label1_7.place(relx=-0.022, rely=0.397, height=21, width=184)
Label1_7.configure(activebackground="#303030")
Label1_7.configure(activeforeground="white")
Label1_7.configure(activeforeground="black")
Label1_7.configure(background="#303030")
Label1_7.configure(disabledforeground="#a3a3a3")
#Label1_7.configure(font=font12)
Label1_7.configure(foreground="#1caafc")
Label1_7.configure(highlightbackground="#d9d9d9")
Label1_7.configure(highlightcolor="black")
Label1_7.configure(text='''Private Key (d) :''')

Label1_5 = tk.Label(top)
Label1_5.place(relx=0.296, rely=0.397, height=21, width=64)
Label1_5.configure(activebackground="#303030")
Label1_5.configure(activeforeground="white")
Label1_5.configure(activeforeground="black")
Label1_5.configure(background="#303030")
Label1_5.configure(disabledforeground="#a3a3a3")
#Label1_5.configure(font=font12)
Label1_5.configure(foreground="#1caafc")
Label1_5.configure(highlightbackground="#d9d9d9")
Label1_5.configure(highlightcolor="black")
Label1_5.configure(text='''& (n) :''')


d11=tk.StringVar()

d1 = tk.Entry(top,text=d11)
d1.place(relx=0.198, rely=0.397,height=20, relwidth=0.092)
d1.configure(background="#1e1e1e")
d1.configure(disabledforeground="#a3a3a3")
d1.configure(font="TkFixedFont")
d1.configure(foreground="#30baff")
d1.configure(highlightbackground="#d9d9d9")
d1.configure(highlightcolor="black")
d1.configure(insertbackground="#33b4ff")
d1.configure(selectbackground="#c4c4c4")
d1.configure(selectforeground="black")

n22=tk.StringVar()

n2 = tk.Entry(top,text=n22)
n2.place(relx=0.373, rely=0.397,height=20, relwidth=0.092)
n2.configure(background="#1e1e1e")
n2.configure(disabledforeground="#a3a3a3")
n2.configure(font="TkFixedFont")
n2.configure(foreground="#30baff")
n2.configure(highlightbackground="#d9d9d9")
n2.configure(highlightcolor="black")
n2.configure(insertbackground="#33b4ff")
n2.configure(selectbackground="#c4c4c4")
n2.configure(selectforeground="black")

plain_dataa=tk.StringVar()

plain_data = tk.Entry(top,text=plain_dataa)
plain_data.place(relx=0.022, rely=0.55, relheight=0.337, relwidth=0.44)
plain_data.configure(background="white")
plain_data.configure(font="TkTextFont")
plain_data.configure(foreground="black")
plain_data.configure(highlightbackground="#d9d9d9")
plain_data.configure(highlightcolor="black")
plain_data.configure(insertbackground="black")
plain_data.configure(insertborderwidth="3")
plain_data.configure(selectbackground="#c4c4c4")
plain_data.configure(selectforeground="black")
plain_data.configure(width=10)

Label1_8 = tk.Label(top)
Label1_8.place(relx=0.132, rely=0.489, height=21, width=184)
Label1_8.configure(activebackground="#303030")
Label1_8.configure(activeforeground="white")
Label1_8.configure(activeforeground="black")
Label1_8.configure(background="#303030")
Label1_8.configure(disabledforeground="#a3a3a3")
#Label1_8.configure(font=font12)
Label1_8.configure(foreground="#1caafc")
Label1_8.configure(highlightbackground="#d9d9d9")
Label1_8.configure(highlightcolor="black")
Label1_8.configure(text='''Plain Text :''')

encrypt = tk.Button(top)
encrypt.place(relx=0.351, rely=0.916, height=24, width=97)
encrypt.configure(activebackground="#ececec")
encrypt.configure(activeforeground="#000000")
encrypt.configure(background="#303030")
encrypt.configure(command=ENCRYPT)
encrypt.configure(disabledforeground="#a3a3a3")
encrypt.configure(foreground="#29b8ff")
encrypt.configure(highlightbackground="#d9d9d9")
encrypt.configure(highlightcolor="black")
encrypt.configure(pady="0")
encrypt.configure(relief="groove")
encrypt.configure(text='''Encrypt''')

Label1_5 = tk.Label(top)
Label1_5.place(relx=0.692, rely=0.092, height=21, width=94)
Label1_5.configure(activebackground="#303030")
Label1_5.configure(activeforeground="white")
Label1_5.configure(activeforeground="black")
Label1_5.configure(background="#303030")
Label1_5.configure(disabledforeground="#a3a3a3")
#Label1_5.configure(font=font12)
Label1_5.configure(foreground="#1caafc")
Label1_5.configure(highlightbackground="#d9d9d9")
Label1_5.configure(highlightcolor="black")
Label1_5.configure(text='''Input :''')

Label1_6 = tk.Label(top)
Label1_6.place(relx=0.516, rely=0.153, height=21, width=114)
Label1_6.configure(activebackground="#303030")
Label1_6.configure(activeforeground="white")
Label1_6.configure(activeforeground="black")
Label1_6.configure(background="#303030")
Label1_6.configure(disabledforeground="#a3a3a3")
#Label1_6.configure(font=font12)
Label1_6.configure(foreground="#1caafc")
Label1_6.configure(highlightbackground="#d9d9d9")
Label1_6.configure(highlightcolor="black")
Label1_6.configure(text='''Private Key (d) :''')


d22=tk.StringVar()
d2 = tk.Entry(top,text=d22)
d2.place(relx=0.681, rely=0.153,height=20, relwidth=0.092)
d2.configure(background="#1e1e1e")
d2.configure(disabledforeground="#a3a3a3")
d2.configure(font="TkFixedFont")
d2.configure(foreground="#30baff")
d2.configure(highlightbackground="#d9d9d9")
d2.configure(highlightcolor="black")
d2.configure(insertbackground="#33b4ff")
d2.configure(selectbackground="#c4c4c4")
d2.configure(selectforeground="black")

Label1_7 = tk.Label(top)
Label1_7.place(relx=0.79, rely=0.153, height=21, width=54)
Label1_7.configure(activebackground="#303030")
Label1_7.configure(activeforeground="white")
Label1_7.configure(activeforeground="black")
Label1_7.configure(background="#303030")
Label1_7.configure(disabledforeground="#a3a3a3")
#Label1_7.configure(font=font12)
Label1_7.configure(foreground="#1caafc")
Label1_7.configure(highlightbackground="#d9d9d9")
Label1_7.configure(highlightcolor="black")
Label1_7.configure(text='''& (n) :''')

n33=tk.StringVar()

n3 = tk.Entry(top,text=n33)
n3.place(relx=0.867, rely=0.153,height=20, relwidth=0.092)
n3.configure(background="#1e1e1e")
n3.configure(disabledforeground="#a3a3a3")
n3.configure(font="TkFixedFont")
n3.configure(foreground="#30baff")
n3.configure(highlightbackground="#d9d9d9")
n3.configure(highlightcolor="black")
n3.configure(insertbackground="#33b4ff")
n3.configure(selectbackground="#c4c4c4")
n3.configure(selectforeground="black")

TSeparator4_7 = ttk.Separator(top)
TSeparator4_7.place(relx=0.494, rely=0.244, relwidth=0.549)

Label1_9 = tk.Label(top)
Label1_9.place(relx=0.648, rely=0.29, height=21, width=184)
Label1_9.configure(activebackground="#303030")
Label1_9.configure(activeforeground="white")
Label1_9.configure(activeforeground="black")
Label1_9.configure(background="#303030")
Label1_9.configure(disabledforeground="#a3a3a3")
#Label1_9.configure(font=font12)
Label1_9.configure(foreground="#1caafc")
Label1_9.configure(highlightbackground="#d9d9d9")
Label1_9.configure(highlightcolor="black")
Label1_9.configure(text='''Cipher Text :''')


decrypt = tk.Button(top,command=decryption)
decrypt.place(relx=0.867, rely=0.916, height=24, width=97)
decrypt.configure(activebackground="#ececec")
decrypt.configure(activeforeground="#000000")
decrypt.configure(background="#303030")
#decrypt.configure(command=RSAEncNew_support.ENCRYPT(pp.get(),qq.get(),ee.get(),plain_dataa.get()))
decrypt.configure(disabledforeground="#a3a3a3")
decrypt.configure(foreground="#29b8ff")
decrypt.configure(highlightbackground="#d9d9d9")
decrypt.configure(highlightcolor="black")
decrypt.configure(pady="0")
decrypt.configure(relief="groove")
decrypt.configure(text='''Decrypt''')

cipher_dataa=tk.StringVar()

cipher_data = tk.Entry(top,text=cipher_dataa)
cipher_data.place(relx=0.527, rely=0.366, relheight=0.521
        , relwidth=0.443)
cipher_data.configure(background="white")
cipher_data.configure(font="TkTextFont")
cipher_data.configure(foreground="black")
cipher_data.configure(highlightbackground="#d9d9d9")
cipher_data.configure(highlightcolor="black")
cipher_data.configure(insertbackground="black")
cipher_data.configure(selectbackground="#c4c4c4")
cipher_data.configure(selectforeground="black")

Label1_6 = tk.Label(top)
Label1_6.place(relx=0.0, rely=0.031, height=21, width=154)
Label1_6.configure(activebackground="#303030")
Label1_6.configure(activeforeground="white")
Label1_6.configure(activeforeground="black")
Label1_6.configure(background="#303030")
Label1_6.configure(disabledforeground="#a3a3a3")
#Label1_6.configure(font=font12)
Label1_6.configure(foreground="#1caafc")
Label1_6.configure(highlightbackground="#d9d9d9")
Label1_6.configure(highlightcolor="black")
Label1_6.configure(text='''RSA Encryption :''')

Label1_7 = tk.Label(top)
Label1_7.place(relx=0.494, rely=0.031, height=21, width=154)
Label1_7.configure(activebackground="#303030")
Label1_7.configure(activeforeground="white")
Label1_7.configure(activeforeground="black")
Label1_7.configure(background="#303030")
Label1_7.configure(disabledforeground="#a3a3a3")
#Label1_7.configure(font=font12)
Label1_7.configure(foreground="#1caafc")
Label1_7.configure(highlightbackground="#d9d9d9")
Label1_7.configure(highlightcolor="black")
Label1_7.configure(text='''RSA Decryption :''')
top.mainloop()
