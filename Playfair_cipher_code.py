
import sys
from tkinter.scrolledtext import ScrolledText


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
    
my_matrix=[]

import os.path
def keyArrange():
    global my_matrix
    try:
        key=Entry_key.get()
        print(key)
    except:
        pass
    TextCipherText.delete(1.0,tk.END)
    if(not key.isalpha()):
        TextCipherText.insert(1.0,":----Enter valid key----:")
        return
    key=key.replace(" ", "")
    key=key.upper()
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)]
    
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0) #initialize matrix
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    count=1
    for i in range(0,5):
        for j in range(0,5):
            xx=str('Entry'+str(count)+'.delete(0,last=1)')
            exec(xx)
            print(xx)
            count+=1
    count=1
     
    for i in range(0,5):
        for j in range(0,5):
            x=str(my_matrix[i][j])
            xx=str('Entry'+str(count)+'.insert(1,'+"'"+x+"'"+')')
            print(xx)
            exec(xx)
            count+=1

    
def locindex(c): #get location of each character
    loc=list()
    if c==EntryKeyFrom.get().upper():
        c=EntryKeyTo.get().upper()
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
    return loc


my_matrix2=[]

import os.path
def keyArrange2():
    global my_matrix2
    try:
        key=EntryKeyD.get()
        print(key)
    except:
        pass
    TextCipherText.delete(1.0,tk.END)
    if(not key.isalpha()):
        TextCipherText.insert(1.0,":----Enter valid key----:")
        return
    key=key.replace(" ", "")
    key=key.upper()
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)]
    
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix2=matrix(5,5,0) #initialize matrix
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix2[i][j]=result[k]
            k+=1
    count=1
    for i in range(0,5):
        for j in range(0,5):
            xx=str('d'+str(count)+'.delete(0,last=1)')
            exec(xx)
            print(xx)
            count+=1
    count=1
     
    for i in range(0,5):
        for j in range(0,5):
            x=str(my_matrix2[i][j])
            xx=str('d'+str(count)+'.insert(1,'+"'"+x+"'"+')')
            print(xx)
            exec(xx)
            count+=1 
def locindex2(c): #get location of each character
    loc=list()
    if c==EntryKeyFrom.get().upper():
        c=EntryKeyTo.get().upper()
    for i ,j in enumerate(my_matrix2):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc



def ENCRYPT():
    msg=text_plain.get(1.0,tk.END)[:-1]
    TextCipherText.delete(1.0,tk.END)

    Lower_index=[]
    spetial_char={}
    for i in range(len(msg)):
        if(msg[i].islower()):
           Lower_index.append(i)
    x=len(msg)
    msgN=""
    for i in range(x):
        if(msg[i]==" "):
            spetial_char[i]=msg[i]
        elif(not msg[i].isalpha()):
            spetial_char[i]=msg[i]
            
        else:
            msgN=msgN+msg[i]
     
    msg=msgN.upper()  
    
              
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",msg,end=' ')
    c=""
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            c=c+my_matrix[(loc[0]+1)%5][loc[1]]+my_matrix[(loc1[0]+1)%5][loc1[1]]
            
        elif loc[0]==loc1[0]:
            c=c+my_matrix[loc[0]][(loc[1]+1)%5]+my_matrix[loc1[0]][(loc1[1]+1)%5] 
            
        else:
            c=c+my_matrix[loc[0]][loc1[1]]+my_matrix[loc1[0]][loc[1]]
        i=i+2
    cc=list(c)
    for i in spetial_char:
        
        cc.insert(i,spetial_char[i])
    for i in Lower_index:
        cc[i]=cc[i].lower()
    c_t=""
    for i in cc:
        c_t=c_t+i
    TextCipherText.insert(1.0,c_t)
    
   
    
def DECRYPT():
    
    msg=TextCipherText.get(1.0,tk.END)
    text_plain.delete(1.0,tk.END)
    
    Lower_index=[]
    spetial_char={}
    for i in range(len(msg)):
        if(msg[i].islower()):
           Lower_index.append(i)
    x=len(msg)
    msgN=""
    for i in range(x):
        if(msg[i]==" "):
            spetial_char[i]=msg[i]
        elif(not msg[i].isalpha()):
            spetial_char[i]=msg[i]
            
        else:
            msgN=msgN+msg[i]
     
    msg=msgN.upper()  
    
    i=0
    c=""
    while i<len(msg):
        loc=list()
        loc=locindex2(msg[i])
        loc1=list()
        loc1=locindex2(msg[i+1])
        if loc[1]==loc1[1]:
            c+=my_matrix2[(loc[0]-1)%5][loc[1]]+my_matrix2[(loc1[0]-1)%5][loc1[1]]
        elif loc[0]==loc1[0]:
            c+=my_matrix2[loc[0]][(loc[1]-1)%5]+my_matrix2[loc1[0]][(loc1[1]-1)%5]  
        else:
            c+=my_matrix2[loc[0]][loc1[1]]+my_matrix2[loc1[0]][loc[1]]    
        i=i+2        
    cc=list(c)

    for i in spetial_char:
        cc.insert(i,spetial_char[i])
    for i in Lower_index:
        cc[i]=cc[i].lower()
    c_t=""
    for i in cc:
        c_t=c_t+i
    
    text_plain.insert(1.0,c_t[:c_t.find('\\n')])


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Courier New} -size 10 -weight bold -slant"  \
    " roman -underline 0 -overstrike 0"
font11 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'

top=tk.Tk()
top.geometry("911x641+306+11")
top.title("AIO")
top.configure(relief="ridge")
top.configure(background="#303030")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

Inoneticx_Logo = tk.Label(top,text="Inoneticx Technologies Pvt Ltd")
Inoneticx_Logo.place(relx=0.600, rely=0.0, height=41, width=400)
Inoneticx_Logo.configure(activebackground="#303030")
Inoneticx_Logo.configure(activeforeground="white")
Inoneticx_Logo.configure(activeforeground="black")
Inoneticx_Logo.configure(background="#303030")
Inoneticx_Logo.configure(disabledforeground="#a3a3a3")
Inoneticx_Logo.configure(font=font11)
Inoneticx_Logo.configure(foreground="white")
Inoneticx_Logo.configure(highlightbackground="#d9d9d9")
Inoneticx_Logo.configure(highlightcolor="black")

TSeparator1 = ttk.Separator(top)
TSeparator1.place(relx=0.0, rely=0.078, relwidth=0.999)

encrypt_label = tk.Label(top)
encrypt_label.place(relx=0.187, rely=0.094, height=21, width=134)
encrypt_label.configure(activebackground="#303030")
encrypt_label.configure(activeforeground="white")
encrypt_label.configure(activeforeground="black")
encrypt_label.configure(background="#303030")
encrypt_label.configure(disabledforeground="#a3a3a3")
encrypt_label.configure(font=font12)
encrypt_label.configure(foreground="#1caafc")
encrypt_label.configure(highlightbackground="#d9d9d9")
encrypt_label.configure(highlightcolor="black")
encrypt_label.configure(text='''Encryption Input :''')

key_label = tk.Label(top)
key_label.place(relx=-0.005, rely=0.156, height=21, width=94)
key_label.configure(activebackground="#303030")
key_label.configure(activeforeground="white")
key_label.configure(activeforeground="black")
key_label.configure(background="#303030")
key_label.configure(disabledforeground="#a3a3a3")
key_label.configure(font=font12)
key_label.configure(foreground="#1caafc")
key_label.configure(highlightbackground="#d9d9d9")
key_label.configure(highlightcolor="black")
key_label.configure(text='''Key :''')

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: keyArrange())

Entry_key = tk.Entry(top,textvariable=sv)
Entry_key.place(relx=0.137, rely=0.148,height=20, relwidth=0.312)
Entry_key.configure(background="#1e1e1e")
Entry_key.configure(disabledforeground="#a3a3a3")
Entry_key.configure(font="TkFixedFont")
Entry_key.configure(foreground="#30baff")
Entry_key.configure(highlightbackground="#d9d9d9")
Entry_key.configure(highlightcolor="black")
Entry_key.configure(insertbackground="#33b4ff")
Entry_key.configure(selectbackground="#c4c4c4")
Entry_key.configure(selectforeground="black")

ButtonEncrypt = tk.Button(top)
ButtonEncrypt.place(relx=0.335, rely=0.936, height=24, width=97)
ButtonEncrypt.configure(activebackground="#ececec")
ButtonEncrypt.configure(activeforeground="#000000")
ButtonEncrypt.configure(background="#303030")
ButtonEncrypt.configure(command=ENCRYPT)
ButtonEncrypt.configure(disabledforeground="#a3a3a3")
ButtonEncrypt.configure(foreground="#29b8ff")
ButtonEncrypt.configure(highlightbackground="#d9d9d9")
ButtonEncrypt.configure(highlightcolor="black")
ButtonEncrypt.configure(pady="0")
ButtonEncrypt.configure(relief="groove")
ButtonEncrypt.configure(text='''Encrypt''')

Button_Decrypt = tk.Button(top)
Button_Decrypt.place(relx=0.856, rely=0.928, height=24, width=97)
Button_Decrypt.configure(activebackground="#ececec")
Button_Decrypt.configure(activeforeground="#000000")
Button_Decrypt.configure(background="#303030")
Button_Decrypt.configure(command=DECRYPT)
Button_Decrypt.configure(disabledforeground="#a3a3a3")
Button_Decrypt.configure(foreground="#29b8ff")
Button_Decrypt.configure(highlightbackground="#d9d9d9")
Button_Decrypt.configure(highlightcolor="black")
Button_Decrypt.configure(pady="0")
Button_Decrypt.configure(relief="groove")
Button_Decrypt.configure(text='''Decrypt''')

LabelPlayFairLogo = tk.Label(top)
LabelPlayFairLogo.place(relx=0.011, rely=0.008, height=31
        , width=214)
LabelPlayFairLogo.configure(activebackground="#303030")
LabelPlayFairLogo.configure(activeforeground="white")
LabelPlayFairLogo.configure(activeforeground="black")
LabelPlayFairLogo.configure(background="#303030")
LabelPlayFairLogo.configure(disabledforeground="#a3a3a3")
LabelPlayFairLogo.configure(foreground="#1caafc")
LabelPlayFairLogo.configure(highlightbackground="#d9d9d9")
LabelPlayFairLogo.configure(highlightcolor="black")
LabelPlayFairLogo.configure(text='''Playfair Encryption''')
LabelPlayFairLogo.configure(width=214)
LabelPlayFairLogo.configure(font=font12)


TSeparator2 = ttk.Separator(top)
TSeparator2.place(relx=0.494, rely=0.078, relheight=0.92)
TSeparator2.configure(orient="vertical")

Label_Matrix = tk.Label(top)
Label_Matrix.place(relx=0.016, rely=0.257, height=21, width=104)
Label_Matrix.configure(activebackground="#303030")
Label_Matrix.configure(activeforeground="white")
Label_Matrix.configure(activeforeground="black")
Label_Matrix.configure(background="#303030")
Label_Matrix.configure(disabledforeground="#a3a3a3")
Label_Matrix.configure(font=font12)
Label_Matrix.configure(foreground="#1caafc")
Label_Matrix.configure(highlightbackground="#d9d9d9")
Label_Matrix.configure(highlightcolor="black")
Label_Matrix.configure(text='''Key Matrix :''')

Entry1 = tk.Entry(top)
Entry1.place(relx=0.187, rely=0.265,height=20, relwidth=0.026)
Entry1.configure(background="#1e1e1e")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#30baff")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="#33b4ff")
Entry1.configure(selectbackground="#c4c4c4")
Entry1.configure(selectforeground="black")

Entry2 = tk.Entry(top)
Entry2.place(relx=0.231, rely=0.265,height=20, relwidth=0.026)
Entry2.configure(background="#1e1e1e")
Entry2.configure(disabledforeground="#a3a3a3")
Entry2.configure(font="TkFixedFont")
Entry2.configure(foreground="#30baff")
Entry2.configure(highlightbackground="#d9d9d9")
Entry2.configure(highlightcolor="black")
Entry2.configure(insertbackground="#33b4ff")
Entry2.configure(selectbackground="#c4c4c4")
Entry2.configure(selectforeground="black")

Entry3 = tk.Entry(top)
Entry3.place(relx=0.269, rely=0.265,height=20, relwidth=0.026)
Entry3.configure(background="#1e1e1e")
Entry3.configure(disabledforeground="#a3a3a3")
Entry3.configure(font="TkFixedFont")
Entry3.configure(foreground="#30baff")
Entry3.configure(highlightbackground="#d9d9d9")
Entry3.configure(highlightcolor="black")
Entry3.configure(insertbackground="#33b4ff")
Entry3.configure(selectbackground="#c4c4c4")
Entry3.configure(selectforeground="black")

Entry4 = tk.Entry(top)
Entry4.place(relx=0.313, rely=0.265,height=20, relwidth=0.026)
Entry4.configure(background="#1e1e1e")
Entry4.configure(disabledforeground="#a3a3a3")
Entry4.configure(font="TkFixedFont")
Entry4.configure(foreground="#30baff")
Entry4.configure(highlightbackground="#d9d9d9")
Entry4.configure(highlightcolor="black")
Entry4.configure(insertbackground="#33b4ff")
Entry4.configure(selectbackground="#c4c4c4")
Entry4.configure(selectforeground="black")

Entry5 = tk.Entry(top)
Entry5.place(relx=0.351, rely=0.265,height=20, relwidth=0.026)
Entry5.configure(background="#1e1e1e")
Entry5.configure(disabledforeground="#a3a3a3")
Entry5.configure(font="TkFixedFont")
Entry5.configure(foreground="#30baff")
Entry5.configure(highlightbackground="#d9d9d9")
Entry5.configure(highlightcolor="black")
Entry5.configure(insertbackground="#33b4ff")
Entry5.configure(selectbackground="#c4c4c4")
Entry5.configure(selectforeground="black")

Entry6 = tk.Entry(top)
Entry6.place(relx=0.187, rely=0.312,height=20, relwidth=0.026)
Entry6.configure(background="#1e1e1e")
Entry6.configure(disabledforeground="#a3a3a3")
Entry6.configure(font="TkFixedFont")
Entry6.configure(foreground="#30baff")
Entry6.configure(highlightbackground="#d9d9d9")
Entry6.configure(highlightcolor="black")
Entry6.configure(insertbackground="#33b4ff")
Entry6.configure(selectbackground="#c4c4c4")
Entry6.configure(selectforeground="black")

Entry7 = tk.Entry(top)
Entry7.place(relx=0.231, rely=0.312,height=20, relwidth=0.026)
Entry7.configure(background="#1e1e1e")
Entry7.configure(disabledforeground="#a3a3a3")
Entry7.configure(font="TkFixedFont")
Entry7.configure(foreground="#30baff")
Entry7.configure(highlightbackground="#d9d9d9")
Entry7.configure(highlightcolor="black")
Entry7.configure(insertbackground="#33b4ff")
Entry7.configure(selectbackground="#c4c4c4")
Entry7.configure(selectforeground="black")

Entry8 = tk.Entry(top)
Entry8.place(relx=0.269, rely=0.312,height=20, relwidth=0.026)
Entry8.configure(background="#1e1e1e")
Entry8.configure(disabledforeground="#a3a3a3")
Entry8.configure(font="TkFixedFont")
Entry8.configure(foreground="#30baff")
Entry8.configure(highlightbackground="#d9d9d9")
Entry8.configure(highlightcolor="black")
Entry8.configure(insertbackground="#33b4ff")
Entry8.configure(selectbackground="#c4c4c4")
Entry8.configure(selectforeground="black")

Entry9 = tk.Entry(top)
Entry9.place(relx=0.313, rely=0.312,height=20, relwidth=0.026)
Entry9.configure(background="#1e1e1e")
Entry9.configure(disabledforeground="#a3a3a3")
Entry9.configure(font="TkFixedFont")
Entry9.configure(foreground="#30baff")
Entry9.configure(highlightbackground="#d9d9d9")
Entry9.configure(highlightcolor="black")
Entry9.configure(insertbackground="#33b4ff")
Entry9.configure(selectbackground="#c4c4c4")
Entry9.configure(selectforeground="black")

Entry10 = tk.Entry(top)
Entry10.place(relx=0.351, rely=0.312,height=20, relwidth=0.026)
Entry10.configure(background="#1e1e1e")
Entry10.configure(disabledforeground="#a3a3a3")
Entry10.configure(font="TkFixedFont")
Entry10.configure(foreground="#30baff")
Entry10.configure(highlightbackground="#d9d9d9")
Entry10.configure(highlightcolor="black")
Entry10.configure(insertbackground="#33b4ff")
Entry10.configure(selectbackground="#c4c4c4")
Entry10.configure(selectforeground="black")

Entry11 = tk.Entry(top)
Entry11.place(relx=0.187, rely=0.359,height=20, relwidth=0.026)
Entry11.configure(background="#1e1e1e")
Entry11.configure(disabledforeground="#a3a3a3")
Entry11.configure(font="TkFixedFont")
Entry11.configure(foreground="#30baff")
Entry11.configure(highlightbackground="#d9d9d9")
Entry11.configure(highlightcolor="black")
Entry11.configure(insertbackground="#33b4ff")
Entry11.configure(selectbackground="#c4c4c4")
Entry11.configure(selectforeground="black")

Entry12 = tk.Entry(top)
Entry12.place(relx=0.231, rely=0.359,height=20, relwidth=0.026)
Entry12.configure(background="#1e1e1e")
Entry12.configure(disabledforeground="#a3a3a3")
Entry12.configure(font="TkFixedFont")
Entry12.configure(foreground="#30baff")
Entry12.configure(highlightbackground="#d9d9d9")
Entry12.configure(highlightcolor="black")
Entry12.configure(insertbackground="#33b4ff")
Entry12.configure(selectbackground="#c4c4c4")
Entry12.configure(selectforeground="black")

Entry13 = tk.Entry(top)
Entry13.place(relx=0.269, rely=0.359,height=20, relwidth=0.026)
Entry13.configure(background="#1e1e1e")
Entry13.configure(disabledforeground="#a3a3a3")
Entry13.configure(font="TkFixedFont")
Entry13.configure(foreground="#30baff")
Entry13.configure(highlightbackground="#d9d9d9")
Entry13.configure(highlightcolor="black")
Entry13.configure(insertbackground="#33b4ff")
Entry13.configure(selectbackground="#c4c4c4")
Entry13.configure(selectforeground="black")

Entry14 = tk.Entry(top)
Entry14.place(relx=0.313, rely=0.359,height=20, relwidth=0.026)
Entry14.configure(background="#1e1e1e")
Entry14.configure(disabledforeground="#a3a3a3")
Entry14.configure(font="TkFixedFont")
Entry14.configure(foreground="#30baff")
Entry14.configure(highlightbackground="#d9d9d9")
Entry14.configure(highlightcolor="black")
Entry14.configure(insertbackground="#33b4ff")
Entry14.configure(selectbackground="#c4c4c4")
Entry14.configure(selectforeground="black")

Entry15 = tk.Entry(top)
Entry15.place(relx=0.351, rely=0.359,height=20, relwidth=0.026)
Entry15.configure(background="#1e1e1e")
Entry15.configure(disabledforeground="#a3a3a3")
Entry15.configure(font="TkFixedFont")
Entry15.configure(foreground="#30baff")
Entry15.configure(highlightbackground="#d9d9d9")
Entry15.configure(highlightcolor="black")
Entry15.configure(insertbackground="#33b4ff")
Entry15.configure(selectbackground="#c4c4c4")
Entry15.configure(selectforeground="black")

Entry16 = tk.Entry(top)
Entry16.place(relx=0.187, rely=0.406,height=20, relwidth=0.026)
Entry16.configure(background="#1e1e1e")
Entry16.configure(disabledforeground="#a3a3a3")
Entry16.configure(font="TkFixedFont")
Entry16.configure(foreground="#30baff")
Entry16.configure(highlightbackground="#d9d9d9")
Entry16.configure(highlightcolor="black")
Entry16.configure(insertbackground="#33b4ff")
Entry16.configure(selectbackground="#c4c4c4")
Entry16.configure(selectforeground="black")

Entry17 = tk.Entry(top)
Entry17.place(relx=0.231, rely=0.406,height=20, relwidth=0.026)
Entry17.configure(background="#1e1e1e")
Entry17.configure(disabledforeground="#a3a3a3")
Entry17.configure(font="TkFixedFont")
Entry17.configure(foreground="#30baff")
Entry17.configure(highlightbackground="#d9d9d9")
Entry17.configure(highlightcolor="black")
Entry17.configure(insertbackground="#33b4ff")
Entry17.configure(selectbackground="#c4c4c4")
Entry17.configure(selectforeground="black")

Entry18 = tk.Entry(top)
Entry18.place(relx=0.269, rely=0.406,height=20, relwidth=0.026)
Entry18.configure(background="#1e1e1e")
Entry18.configure(disabledforeground="#a3a3a3")
Entry18.configure(font="TkFixedFont")
Entry18.configure(foreground="#30baff")
Entry18.configure(highlightbackground="#d9d9d9")
Entry18.configure(highlightcolor="black")
Entry18.configure(insertbackground="#33b4ff")
Entry18.configure(selectbackground="#c4c4c4")
Entry18.configure(selectforeground="black")

Entry19 = tk.Entry(top)
Entry19.place(relx=0.313, rely=0.406,height=20, relwidth=0.026)
Entry19.configure(background="#1e1e1e")
Entry19.configure(disabledforeground="#a3a3a3")
Entry19.configure(font="TkFixedFont")
Entry19.configure(foreground="#30baff")
Entry19.configure(highlightbackground="#d9d9d9")
Entry19.configure(highlightcolor="black")
Entry19.configure(insertbackground="#33b4ff")
Entry19.configure(selectbackground="#c4c4c4")
Entry19.configure(selectforeground="black")

Entry20 = tk.Entry(top)
Entry20.place(relx=0.351, rely=0.406,height=20, relwidth=0.026)
Entry20.configure(background="#1e1e1e")
Entry20.configure(disabledforeground="#a3a3a3")
Entry20.configure(font="TkFixedFont")
Entry20.configure(foreground="#30baff")
Entry20.configure(highlightbackground="#d9d9d9")
Entry20.configure(highlightcolor="black")
Entry20.configure(insertbackground="#33b4ff")
Entry20.configure(selectbackground="#c4c4c4")
Entry20.configure(selectforeground="black")

Entry21 = tk.Entry(top)
Entry21.place(relx=0.187, rely=0.445,height=20, relwidth=0.026)
Entry21.configure(background="#1e1e1e")
Entry21.configure(disabledforeground="#a3a3a3")
Entry21.configure(font="TkFixedFont")
Entry21.configure(foreground="#30baff")
Entry21.configure(highlightbackground="#d9d9d9")
Entry21.configure(highlightcolor="black")
Entry21.configure(insertbackground="#33b4ff")
Entry21.configure(selectbackground="#c4c4c4")
Entry21.configure(selectforeground="black")

Entry22 = tk.Entry(top)
Entry22.place(relx=0.231, rely=0.445,height=20, relwidth=0.026)
Entry22.configure(background="#1e1e1e")
Entry22.configure(disabledforeground="#a3a3a3")
Entry22.configure(font="TkFixedFont")
Entry22.configure(foreground="#30baff")
Entry22.configure(highlightbackground="#d9d9d9")
Entry22.configure(highlightcolor="black")
Entry22.configure(insertbackground="#33b4ff")
Entry22.configure(selectbackground="#c4c4c4")
Entry22.configure(selectforeground="black")

Entry23 = tk.Entry(top)
Entry23.place(relx=0.269, rely=0.445,height=20, relwidth=0.026)
Entry23.configure(background="#1e1e1e")
Entry23.configure(disabledforeground="#a3a3a3")
Entry23.configure(font="TkFixedFont")
Entry23.configure(foreground="#30baff")
Entry23.configure(highlightbackground="#d9d9d9")
Entry23.configure(highlightcolor="black")
Entry23.configure(insertbackground="#33b4ff")
Entry23.configure(selectbackground="#c4c4c4")
Entry23.configure(selectforeground="black")

Entry24 = tk.Entry(top)
Entry24.place(relx=0.313, rely=0.445,height=20, relwidth=0.026)
Entry24.configure(background="#1e1e1e")
Entry24.configure(disabledforeground="#a3a3a3")
Entry24.configure(font="TkFixedFont")
Entry24.configure(foreground="#30baff")
Entry24.configure(highlightbackground="#d9d9d9")
Entry24.configure(highlightcolor="black")
Entry24.configure(insertbackground="#33b4ff")
Entry24.configure(selectbackground="#c4c4c4")
Entry24.configure(selectforeground="black")

Entry25 = tk.Entry(top)
Entry25.place(relx=0.351, rely=0.445,height=20, relwidth=0.026)
Entry25.configure(background="#1e1e1e")
Entry25.configure(disabledforeground="#a3a3a3")
Entry25.configure(font="TkFixedFont")
Entry25.configure(foreground="#30baff")
Entry25.configure(highlightbackground="#d9d9d9")
Entry25.configure(highlightcolor="black")
Entry25.configure(insertbackground="#33b4ff")
Entry25.configure(selectbackground="#c4c4c4")
Entry25.configure(selectforeground="black")

Label_plain_text = tk.Label(top)
Label_plain_text.place(relx=0.033, rely=0.499, height=21, width=214)

Label_plain_text.configure(activebackground="#303030")
Label_plain_text.configure(activeforeground="white")
Label_plain_text.configure(activeforeground="black")
Label_plain_text.configure(background="#303030")
Label_plain_text.configure(disabledforeground="#a3a3a3")
Label_plain_text.configure(font=font12)
Label_plain_text.configure(foreground="#1caafc")
Label_plain_text.configure(highlightbackground="#d9d9d9")
Label_plain_text.configure(highlightcolor="black")
Label_plain_text.configure(text='''Plain Text ( Orignal Message ) :''')

text_plain = ScrolledText(top)
text_plain.place(relx=0.05, rely=0.562, relheight=0.345
        , relwidth=0.407)
text_plain.configure(background="white")
text_plain.configure(font=font9)
text_plain.configure(foreground="black")
text_plain.configure(highlightbackground="#d9d9d9")
text_plain.configure(highlightcolor="black")
text_plain.configure(insertbackground="black")
text_plain.configure(insertborderwidth="3")
text_plain.configure(selectbackground="#c4c4c4")
text_plain.configure(selectforeground="black")
text_plain.configure(width=10)
text_plain.configure(wrap="none")

decrypt_label = tk.Label(top)
decrypt_label.place(relx=0.681, rely=0.094, height=21, width=154)
decrypt_label.configure(activebackground="#303030")
decrypt_label.configure(activeforeground="white")
decrypt_label.configure(activeforeground="black")
decrypt_label.configure(background="#303030")
decrypt_label.configure(disabledforeground="#a3a3a3")
decrypt_label.configure(font=font12)
decrypt_label.configure(foreground="#1caafc")
decrypt_label.configure(highlightbackground="#d9d9d9")
decrypt_label.configure(highlightcolor="black")
decrypt_label.configure(text='''Decryption Input :''')



sv2 = tk.StringVar()
sv2.trace("w", lambda name, index, mode, sv=sv: keyArrange2())

EntryKeyD = tk.Entry(top,textvariable=sv2)
EntryKeyD.place(relx=0.648, rely=0.14,height=20, relwidth=0.301)
EntryKeyD.configure(background="#1e1e1e")
EntryKeyD.configure(disabledforeground="#a3a3a3")
EntryKeyD.configure(font="TkFixedFont")
EntryKeyD.configure(foreground="#30baff")
EntryKeyD.configure(highlightbackground="#d9d9d9")
EntryKeyD.configure(highlightcolor="black")
EntryKeyD.configure(insertbackground="#33b4ff")
EntryKeyD.configure(selectbackground="#c4c4c4")
EntryKeyD.configure(selectforeground="black")
#EntryKeyD.configure(textvariable=Playfair_cipher_code_support.keyD)

Label_key_D = tk.Label(top)
Label_key_D.place(relx=0.538, rely=0.14, height=21, width=44)
Label_key_D.configure(activebackground="#303030")
Label_key_D.configure(activeforeground="white")
Label_key_D.configure(activeforeground="black")
Label_key_D.configure(background="#303030")
Label_key_D.configure(disabledforeground="#a3a3a3")
Label_key_D.configure(font=font12)
Label_key_D.configure(foreground="#1caafc")
Label_key_D.configure(highlightbackground="#d9d9d9")
Label_key_D.configure(highlightcolor="black")
Label_key_D.configure(text='''Key :''')

Label_Matrix_D = tk.Label(top)
Label_Matrix_D.place(relx=0.527, rely=0.257, height=21, width=104)
Label_Matrix_D.configure(activebackground="#303030")
Label_Matrix_D.configure(activeforeground="white")
Label_Matrix_D.configure(activeforeground="black")
Label_Matrix_D.configure(background="#303030")
Label_Matrix_D.configure(disabledforeground="#a3a3a3")
Label_Matrix_D.configure(font=font12)
Label_Matrix_D.configure(foreground="#1caafc")
Label_Matrix_D.configure(highlightbackground="#d9d9d9")
Label_Matrix_D.configure(highlightcolor="black")
Label_Matrix_D.configure(text='''Key Martix :''')

d1 = tk.Entry(top)
d1.place(relx=0.703, rely=0.257,height=20, relwidth=0.026)
d1.configure(background="#1e1e1e")
d1.configure(disabledforeground="#a3a3a3")
d1.configure(font="TkFixedFont")
d1.configure(foreground="#30baff")
d1.configure(highlightbackground="#d9d9d9")
d1.configure(highlightcolor="black")
d1.configure(insertbackground="#33b4ff")
d1.configure(selectbackground="#c4c4c4")
d1.configure(selectforeground="black")
#d1.configure(textvariable=Playfair_cipher_code_support.d1)

d2 = tk.Entry(top)
d2.place(relx=0.746, rely=0.257,height=20, relwidth=0.026)
d2.configure(background="#1e1e1e")
d2.configure(disabledforeground="#a3a3a3")
d2.configure(font="TkFixedFont")
d2.configure(foreground="#30baff")
d2.configure(highlightbackground="#d9d9d9")
d2.configure(highlightcolor="black")
d2.configure(insertbackground="#33b4ff")
d2.configure(selectbackground="#c4c4c4")
d2.configure(selectforeground="black")
#d2.configure(textvariable=Playfair_cipher_code_support.d2)

d3 = tk.Entry(top)
d3.place(relx=0.79, rely=0.257,height=20, relwidth=0.026)
d3.configure(background="#1e1e1e")
d3.configure(disabledforeground="#a3a3a3")
d3.configure(font="TkFixedFont")
d3.configure(foreground="#30baff")
d3.configure(highlightbackground="#d9d9d9")
d3.configure(highlightcolor="black")
d3.configure(insertbackground="#33b4ff")
d3.configure(selectbackground="#c4c4c4")
d3.configure(selectforeground="black")
#d3.configure(textvariable=Playfair_cipher_code_support.d3)

d4 = tk.Entry(top)
d4.place(relx=0.829, rely=0.257,height=20, relwidth=0.026)
d4.configure(background="#1e1e1e")
d4.configure(disabledforeground="#a3a3a3")
d4.configure(font="TkFixedFont")
d4.configure(foreground="#30baff")
d4.configure(highlightbackground="#d9d9d9")
d4.configure(highlightcolor="black")
d4.configure(insertbackground="#33b4ff")
d4.configure(selectbackground="#c4c4c4")
d4.configure(selectforeground="black")
#d4.configure(textvariable=Playfair_cipher_code_support.d4)

d5 = tk.Entry(top)
d5.place(relx=0.867, rely=0.257,height=20, relwidth=0.026)
d5.configure(background="#1e1e1e")
d5.configure(disabledforeground="#a3a3a3")
d5.configure(font="TkFixedFont")
d5.configure(foreground="#30baff")
d5.configure(highlightbackground="#d9d9d9")
d5.configure(highlightcolor="black")
d5.configure(insertbackground="#33b4ff")
d5.configure(selectbackground="#c4c4c4")
d5.configure(selectforeground="black")
#d5.configure(textvariable=Playfair_cipher_code_support.d5)

d6 = tk.Entry(top)
d6.place(relx=0.703, rely=0.304,height=20, relwidth=0.026)
d6.configure(background="#1e1e1e")
d6.configure(disabledforeground="#a3a3a3")
d6.configure(font="TkFixedFont")
d6.configure(foreground="#30baff")
d6.configure(highlightbackground="#d9d9d9")
d6.configure(highlightcolor="black")
d6.configure(insertbackground="#33b4ff")
d6.configure(selectbackground="#c4c4c4")
d6.configure(selectforeground="black")
#d6.configure(textvariable=Playfair_cipher_code_support.d6)

d7 = tk.Entry(top)
d7.place(relx=0.746, rely=0.304,height=20, relwidth=0.026)
d7.configure(background="#1e1e1e")
d7.configure(disabledforeground="#a3a3a3")
d7.configure(font="TkFixedFont")
d7.configure(foreground="#30baff")
d7.configure(highlightbackground="#d9d9d9")
d7.configure(highlightcolor="black")
d7.configure(insertbackground="#33b4ff")
d7.configure(selectbackground="#c4c4c4")
d7.configure(selectforeground="black")
#d7.configure(textvariable=Playfair_cipher_code_support.d7)

d8 = tk.Entry(top)
d8.place(relx=0.79, rely=0.304,height=20, relwidth=0.026)
d8.configure(background="#1e1e1e")
d8.configure(disabledforeground="#a3a3a3")
d8.configure(font="TkFixedFont")
d8.configure(foreground="#30baff")
d8.configure(highlightbackground="#d9d9d9")
d8.configure(highlightcolor="black")
d8.configure(insertbackground="#33b4ff")
d8.configure(selectbackground="#c4c4c4")
d8.configure(selectforeground="black")
#d8.configure(textvariable=Playfair_cipher_code_support.d8)

d9 = tk.Entry(top)
d9.place(relx=0.829, rely=0.304,height=20, relwidth=0.026)
d9.configure(background="#1e1e1e")
d9.configure(disabledforeground="#a3a3a3")
d9.configure(font="TkFixedFont")
d9.configure(foreground="#30baff")
d9.configure(highlightbackground="#d9d9d9")
d9.configure(highlightcolor="black")
d9.configure(insertbackground="#33b4ff")
d9.configure(selectbackground="#c4c4c4")
d9.configure(selectforeground="black")
#d9.configure(textvariable=Playfair_cipher_code_support.d9)

d10 = tk.Entry(top)
d10.place(relx=0.867, rely=0.304,height=20, relwidth=0.026)
d10.configure(background="#1e1e1e")
d10.configure(disabledforeground="#a3a3a3")
d10.configure(font="TkFixedFont")
d10.configure(foreground="#30baff")
d10.configure(highlightbackground="#d9d9d9")
d10.configure(highlightcolor="black")
d10.configure(insertbackground="#33b4ff")
d10.configure(selectbackground="#c4c4c4")
d10.configure(selectforeground="black")
#d10.configure(textvariable=Playfair_cipher_code_support.d10)

d11 = tk.Entry(top)
d11.place(relx=0.703, rely=0.351,height=20, relwidth=0.026)
d11.configure(background="#1e1e1e")
d11.configure(disabledforeground="#a3a3a3")
d11.configure(font="TkFixedFont")
d11.configure(foreground="#30baff")
d11.configure(highlightbackground="#d9d9d9")
d11.configure(highlightcolor="black")
d11.configure(insertbackground="#33b4ff")
d11.configure(selectbackground="#c4c4c4")
d11.configure(selectforeground="black")
#d11.configure(textvariable=Playfair_cipher_code_support.d11)

d12 = tk.Entry(top)
d12.place(relx=0.746, rely=0.351,height=20, relwidth=0.026)
d12.configure(background="#1e1e1e")
d12.configure(disabledforeground="#a3a3a3")
d12.configure(font="TkFixedFont")
d12.configure(foreground="#30baff")
d12.configure(highlightbackground="#d9d9d9")
d12.configure(highlightcolor="black")
d12.configure(insertbackground="#33b4ff")
d12.configure(selectbackground="#c4c4c4")
d12.configure(selectforeground="black")
#d12.configure(textvariable=Playfair_cipher_code_support.d12)

d13 = tk.Entry(top)
d13.place(relx=0.79, rely=0.351,height=20, relwidth=0.026)
d13.configure(background="#1e1e1e")
d13.configure(disabledforeground="#a3a3a3")
d13.configure(font="TkFixedFont")
d13.configure(foreground="#30baff")
d13.configure(highlightbackground="#d9d9d9")
d13.configure(highlightcolor="black")
d13.configure(insertbackground="#33b4ff")
d13.configure(selectbackground="#c4c4c4")
d13.configure(selectforeground="black")
#d13.configure(textvariable=Playfair_cipher_code_support.d13)
#
d14 = tk.Entry(top)
d14.place(relx=0.829, rely=0.351,height=20, relwidth=0.026)
d14.configure(background="#1e1e1e")
d14.configure(disabledforeground="#a3a3a3")
d14.configure(font="TkFixedFont")
d14.configure(foreground="#30baff")
d14.configure(highlightbackground="#d9d9d9")
d14.configure(highlightcolor="black")
d14.configure(insertbackground="#33b4ff")
d14.configure(selectbackground="#c4c4c4")
d14.configure(selectforeground="black")
#d14.configure(textvariable=Playfair_cipher_code_support.d14)

d15 = tk.Entry(top)
d15.place(relx=0.873, rely=0.351,height=20, relwidth=0.026)
d15.configure(background="#1e1e1e")
d15.configure(disabledforeground="#a3a3a3")
d15.configure(font="TkFixedFont")
d15.configure(foreground="#30baff")
d15.configure(highlightbackground="#d9d9d9")
d15.configure(highlightcolor="black")
d15.configure(insertbackground="#33b4ff")
d15.configure(selectbackground="#c4c4c4")
d15.configure(selectforeground="black")
#d15.configure(textvariable=Playfair_cipher_code_support.d15)

d16 = tk.Entry(top)
d16.place(relx=0.703, rely=0.398,height=20, relwidth=0.026)
d16.configure(background="#1e1e1e")
d16.configure(disabledforeground="#a3a3a3")
d16.configure(font="TkFixedFont")
d16.configure(foreground="#30baff")
d16.configure(highlightbackground="#d9d9d9")
d16.configure(highlightcolor="black")
d16.configure(insertbackground="#33b4ff")
d16.configure(selectbackground="#c4c4c4")
d16.configure(selectforeground="black")
#d16.configure(textvariable=Playfair_cipher_code_support.d16)

d17 = tk.Entry(top)
d17.place(relx=0.746, rely=0.398,height=20, relwidth=0.026)
d17.configure(background="#1e1e1e")
d17.configure(disabledforeground="#a3a3a3")
d17.configure(font="TkFixedFont")
d17.configure(foreground="#30baff")
d17.configure(highlightbackground="#d9d9d9")
d17.configure(highlightcolor="black")
d17.configure(insertbackground="#33b4ff")
d17.configure(selectbackground="#c4c4c4")
d17.configure(selectforeground="black")
#d17.configure(textvariable=Playfair_cipher_code_support.d17)

d18 = tk.Entry(top)
d18.place(relx=0.79, rely=0.398,height=20, relwidth=0.026)
d18.configure(background="#1e1e1e")
d18.configure(disabledforeground="#a3a3a3")
d18.configure(font="TkFixedFont")
d18.configure(foreground="#30baff")
d18.configure(highlightbackground="#d9d9d9")
d18.configure(highlightcolor="black")
d18.configure(insertbackground="#33b4ff")
d18.configure(selectbackground="#c4c4c4")
d18.configure(selectforeground="black")
#d18.configure(textvariable=Playfair_cipher_code_support.d18)

d19 = tk.Entry(top)
d19.place(relx=0.834, rely=0.398,height=20, relwidth=0.026)
d19.configure(background="#1e1e1e")
d19.configure(disabledforeground="#a3a3a3")
d19.configure(font="TkFixedFont")
d19.configure(foreground="#30baff")
d19.configure(highlightbackground="#d9d9d9")
d19.configure(highlightcolor="black")
d19.configure(insertbackground="#33b4ff")
d19.configure(selectbackground="#c4c4c4")
d19.configure(selectforeground="black")
#d19.configure(textvariable=Playfair_cipher_code_support.d19)

d20 = tk.Entry(top)
d20.place(relx=0.873, rely=0.398,height=20, relwidth=0.026)
d20.configure(background="#1e1e1e")
d20.configure(disabledforeground="#a3a3a3")
d20.configure(font="TkFixedFont")
d20.configure(foreground="#30baff")
d20.configure(highlightbackground="#d9d9d9")
d20.configure(highlightcolor="black")
d20.configure(insertbackground="#33b4ff")
d20.configure(selectbackground="#c4c4c4")
d20.configure(selectforeground="black")
#d20.configure(textvariable=Playfair_cipher_code_support.d20)

d21 = tk.Entry(top)
d21.place(relx=0.708, rely=0.452,height=20, relwidth=0.026)
d21.configure(background="#1e1e1e")
d21.configure(disabledforeground="#a3a3a3")
d21.configure(font="TkFixedFont")
d21.configure(foreground="#30baff")
d21.configure(highlightbackground="#d9d9d9")
d21.configure(highlightcolor="black")
d21.configure(insertbackground="#33b4ff")
d21.configure(selectbackground="#c4c4c4")
d21.configure(selectforeground="black")
#d21.configure(textvariable=Playfair_cipher_code_support.d21)

d22 = tk.Entry(top)
d22.place(relx=0.746, rely=0.452,height=20, relwidth=0.026)
d22.configure(background="#1e1e1e")
d22.configure(disabledforeground="#a3a3a3")
d22.configure(font="TkFixedFont")
d22.configure(foreground="#30baff")
d22.configure(highlightbackground="#d9d9d9")
d22.configure(highlightcolor="black")
d22.configure(insertbackground="#33b4ff")
d22.configure(selectbackground="#c4c4c4")
d22.configure(selectforeground="black")
#d22.configure(textvariable=Playfair_cipher_code_support.d22)

d23 = tk.Entry(top)
d23.place(relx=0.79, rely=0.452,height=20, relwidth=0.026)
d23.configure(background="#1e1e1e")
d23.configure(disabledforeground="#a3a3a3")
d23.configure(font="TkFixedFont")
d23.configure(foreground="#30baff")
d23.configure(highlightbackground="#d9d9d9")
d23.configure(highlightcolor="black")
d23.configure(insertbackground="#33b4ff")
d23.configure(selectbackground="#c4c4c4")
d23.configure(selectforeground="black")
#d23.configure(textvariable=Playfair_cipher_code_support.d23)

d24 = tk.Entry(top)
d24.place(relx=0.829, rely=0.452,height=20, relwidth=0.026)
d24.configure(background="#1e1e1e")
d24.configure(disabledforeground="#a3a3a3")
d24.configure(font="TkFixedFont")
d24.configure(foreground="#30baff")
d24.configure(highlightbackground="#d9d9d9")
d24.configure(highlightcolor="black")
d24.configure(insertbackground="#33b4ff")
d24.configure(selectbackground="#c4c4c4")
d24.configure(selectforeground="black")
#d24.configure(textvariable=Playfair_cipher_code_support.d24)

d25 = tk.Entry(top)
d25.place(relx=0.873, rely=0.445,height=20, relwidth=0.026)
d25.configure(background="#1e1e1e")
d25.configure(disabledforeground="#a3a3a3")
d25.configure(font="TkFixedFont")
d25.configure(foreground="#30baff")
d25.configure(highlightbackground="#d9d9d9")
d25.configure(highlightcolor="black")
d25.configure(insertbackground="#33b4ff")
d25.configure(selectbackground="#c4c4c4")
d25.configure(selectforeground="black")
#d25.configure(textvariable=Playfair_cipher_code_support.d25)

Label_cipher_text = tk.Label(top)
Label_cipher_text.place(relx=0.527, rely=0.507, height=21
        , width=234)
Label_cipher_text.configure(activebackground="#303030")
Label_cipher_text.configure(activeforeground="white")
Label_cipher_text.configure(activeforeground="black")
Label_cipher_text.configure(background="#303030")
Label_cipher_text.configure(disabledforeground="#a3a3a3")
Label_cipher_text.configure(font=font12)
Label_cipher_text.configure(foreground="#1caafc")
Label_cipher_text.configure(highlightbackground="#d9d9d9")
Label_cipher_text.configure(highlightcolor="black")
Label_cipher_text.configure(text='''Cipher Text ( Encrypted Text ) :''')

TextCipherText = ScrolledText(top)
TextCipherText.place(relx=0.543, rely=0.562, relheight=0.345
        , relwidth=0.429)
TextCipherText.configure(background="white")
TextCipherText.configure(font=font9)
TextCipherText.configure(foreground="black")
TextCipherText.configure(highlightbackground="#d9d9d9")
TextCipherText.configure(highlightcolor="black")
TextCipherText.configure(insertbackground="black")
TextCipherText.configure(insertborderwidth="3")
TextCipherText.configure(selectbackground="#c4c4c4")
TextCipherText.configure(selectforeground="black")
TextCipherText.configure(width=10)
TextCipherText.configure(wrap="none")

Label_key_from = tk.Label(top)
Label_key_from.place(relx=-0.06, rely=0.211, height=21, width=224)
Label_key_from.configure(activebackground="#303030")
Label_key_from.configure(activeforeground="white")
Label_key_from.configure(activeforeground="black")
Label_key_from.configure(background="#303030")
Label_key_from.configure(disabledforeground="#a3a3a3")
Label_key_from.configure(font=font12)
Label_key_from.configure(foreground="#1caafc")
Label_key_from.configure(highlightbackground="#d9d9d9")
Label_key_from.configure(highlightcolor="black")
Label_key_from.configure(text='''Convert :''')

EntryKeyFrom = tk.Entry(top)
EntryKeyFrom.place(relx=0.137, rely=0.203, height=20
        , relwidth=0.092)
EntryKeyFrom.configure(background="#1e1e1e")
EntryKeyFrom.configure(disabledforeground="#30baff")
EntryKeyFrom.configure(disabledbackground="#1e1e1e")
EntryKeyFrom.configure(font="TkFixedFont")
EntryKeyFrom.configure(foreground="#30baff")
EntryKeyFrom.configure(highlightbackground="#d9d9d9")
EntryKeyFrom.configure(highlightcolor="black")
EntryKeyFrom.configure(insertbackground="#33b4ff")
EntryKeyFrom.configure(selectbackground="#c4c4c4")
EntryKeyFrom.configure(selectforeground="black")
EntryKeyFrom.insert(1,"J")
EntryKeyFrom.configure(state='disabled')

#EntryKeyFrom.configure(textvariable=Playfair_cipher_code_support.cfe)

EntryKeyTo = tk.Entry(top)
EntryKeyTo.place(relx=0.351, rely=0.211,height=20, relwidth=0.092)
EntryKeyTo.configure(background="#1e1e1e")
EntryKeyTo.configure(disabledforeground="#30baff")
EntryKeyTo.configure(disabledbackground="#1e1e1e")

EntryKeyTo.configure(font="TkFixedFont")
EntryKeyTo.configure(foreground="#30baff")
EntryKeyTo.configure(highlightbackground="#d9d9d9")
EntryKeyTo.configure(highlightcolor="black")
EntryKeyTo.configure(insertbackground="#33b4ff")
EntryKeyTo.configure(selectbackground="#c4c4c4")
EntryKeyTo.configure(selectforeground="black")
EntryKeyTo.insert(1,"I")
EntryKeyTo.configure(state='disabled')

#EntryKeyTo.configure(textvariable=Playfair_cipher_code_support.cte)

label_Key_to = tk.Label(top)
label_Key_to.place(relx=0.258, rely=0.203, height=21, width=54)
label_Key_to.configure(activebackground="#303030")
label_Key_to.configure(activeforeground="white")
label_Key_to.configure(activeforeground="black")
label_Key_to.configure(background="#303030")
label_Key_to.configure(disabledforeground="#a3a3a3")
label_Key_to.configure(font=font12)
label_Key_to.configure(foreground="#1caafc")
label_Key_to.configure(highlightbackground="#d9d9d9")
label_Key_to.configure(highlightcolor="black")
label_Key_to.configure(text='''To :''')

Label_key_from_2 = tk.Label(top)
Label_key_from_2.place(relx=0.538, rely=0.203, height=21, width=64)
Label_key_from_2.configure(activebackground="#303030")
Label_key_from_2.configure(activeforeground="white")
Label_key_from_2.configure(activeforeground="black")
Label_key_from_2.configure(background="#303030")
Label_key_from_2.configure(disabledforeground="#a3a3a3")
Label_key_from_2.configure(font=font12)
Label_key_from_2.configure(foreground="#1caafc")
Label_key_from_2.configure(highlightbackground="#d9d9d9")
Label_key_from_2.configure(highlightcolor="black")
Label_key_from_2.configure(text='''Convert :''')

Label_key_to_2 = tk.Label(top)
Label_key_to_2.place(relx=0.774, rely=0.195, height=21, width=54)
Label_key_to_2.configure(activebackground="#303030")
Label_key_to_2.configure(activeforeground="white")
Label_key_to_2.configure(activeforeground="black")
Label_key_to_2.configure(background="#303030")
Label_key_to_2.configure(disabledforeground="#a3a3a3")
Label_key_to_2.configure(font=font12)
Label_key_to_2.configure(foreground="#1caafc")
Label_key_to_2.configure(highlightbackground="#d9d9d9")
Label_key_to_2.configure(highlightcolor="black")
Label_key_to_2.configure(text='''To :''')

EntryKeyFrom2 = tk.Entry(top)
EntryKeyFrom2.place(relx=0.648, rely=0.195, height=20
        , relwidth=0.092)
EntryKeyFrom2.configure(background="#1e1e1e")
EntryKeyFrom2.configure(disabledforeground="#30baff")
EntryKeyFrom2.configure(disabledbackground="#1e1e1e")
EntryKeyFrom2.configure(font="TkFixedFont")
EntryKeyFrom2.configure(foreground="#30baff")
EntryKeyFrom2.configure(highlightbackground="#d9d9d9")
EntryKeyFrom2.configure(highlightcolor="black")
EntryKeyFrom2.configure(insertbackground="#33b4ff")
EntryKeyFrom2.configure(selectbackground="#c4c4c4")
EntryKeyFrom2.configure(selectforeground="black")
EntryKeyFrom2.insert(1,"J")
EntryKeyFrom2.configure(state='disabled')

#EntryKeyFrom2.configure(textvariable=Playfair_cipher_code_support.cfd)

EntryKeyTo2 = tk.Entry(top)
EntryKeyTo2.place(relx=0.856, rely=0.195, height=20, relwidth=0.092)

EntryKeyTo2.configure(background="#1e1e1e")
EntryKeyTo2.configure(disabledforeground="#30baff")
EntryKeyTo2.configure(disabledbackground="#1e1e1e")
EntryKeyTo2.configure(font="TkFixedFont")
EntryKeyTo2.configure(foreground="#30baff")
EntryKeyTo2.configure(highlightbackground="#d9d9d9")
EntryKeyTo2.configure(highlightcolor="black")
EntryKeyTo2.configure(insertbackground="#33b4ff")
EntryKeyTo2.configure(selectbackground="#c4c4c4")
EntryKeyTo2.configure(selectforeground="black")
EntryKeyTo2.insert(1,"I")
EntryKeyTo2.configure(state='disabled')

#EntryKeyTo2.configure(textvariable=Playfair_cipher_code_support.ctd)

top.mainloop()