import math #dengan menambahkan awalan "math.", misalnya "math.sqrt(4)" untuk menghitung akar kuadrat dari 4.
import tkinter as tk #mengimpor modul Python "tkinter", yang menyediakan toolkit antarmuka pengguna grafis (GUI) untuk membangun aplikasi desktop

# Font Style
SMALL_FONT = ("Arial",16) #sin cos tan log
LARGE_FONT = ("Arial",25)
DIGIT_FONT = ("Arial",20) #angka
DEFAULT_FONT = ("Arial",15) #operasi matematika



class Kalkulator: #mendefinisikan kelas Python Kalkulator

     def __init__(self): #dijalankan ketika kelas Kalkulator dibuat untuk pertama kalinya
          self.root = tk.Tk() #menginisialisasi objek Tkinter "root" sebagai atribut "self.root" di dalam kelas

          icon = tk.PhotoImage(file="icon.png") # Mengubah Icon
          self.root.wm_iconphoto(True,icon)

          self.root.geometry("375x667") # Mengatur Tinggi dan lebar Form
          self.root.title("kalkulator-evi") # Mengatur Title Form
          self.root.resizable(0,0) # Berfungsi agar Ukuran Form tidak dapat diubah
          self.root.configure(bg='gray11') #mengganti warna

          self.total_expression = "" # Total
          self.current_expression = "" # Input angka / operator
     
          self.display_frame = self.create_dispaly_frame()
          self.total_label,self.label = self.create_display_label()

          # Digit
          self.digits = {
               7:(1,1), 8:(1,2), 9:(1,3),
               4:(2,1), 5:(2,2), 6:(2,3),
               1:(3,1), 2:(3,2), 3:(3,3),
               0:(4,2),'.':(4,1)
          }

          # Operator
          self.operations = {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"} #Simbol "\u00F7" dan "\u00D7" adalah karakter Unicode yang merepresentasikan simbol pembagian dan perkalian
                                                                        #memastikan bahwa simbol matematika ditampilkan dengan benar pada layar kalkulator di semua perangkat, menggunakan karakter Unicode adalah cara yang tepat untuk memastikan kompatibilitas lintas-platform
          self.buttons_frame = self.create_buttons_frame()

          for x in range(1,5):
               self.buttons_frame.rowconfigure(x,weight=1)
               self.buttons_frame.columnconfigure(x,weight=1)

          self.create_digits_button()
          self.create_operator_buttons()
          self.create_special_buttons()
     

     def create_special_buttons(self):
          self.clear_button()
          self.equals_button()
          self.create_square_buttons()
          self.create_sqrt_buttons()
          self.delete_button()
          self.cos_btn()
          self.sin_btn()
          self.tan_btn()
          self.log_btn()


     def create_display_label(self):
          total_label = tk.Label(self.display_frame,text=self.total_expression,
               anchor=tk.E,
               bg='gray11',
               fg="White",
               padx=24,
               font=SMALL_FONT
          )
          total_label.pack(expand=True,fill='both')

          label = tk.Label(
               self.display_frame,
               text=self.current_expression,
               anchor=tk.E,
               bg='gray11',
               fg='White',
               padx=24,
               font=LARGE_FONT
          )
          label.pack(expand=True,fill='both')

          return total_label,label
     
     def create_dispaly_frame(self):
          frame = tk.Frame(self.root, height=200, bg="blue")
          frame.pack(expand=True, fill="both")
          return frame

     # Membuat button digits
     def create_digits_button(self):
          # Untuk menampilkan angka dengan cara melukan perulangan dari dictionary self.digits
          for angka,grid in self.digits.items():
               button = tk.Button(
                    self.buttons_frame,
                    text=str(angka),
                    bg="gray11",
                    fg="DarkOrange1",
                    font=DIGIT_FONT,
                    borderwidth=0,
                    command=lambda x=angka: self.add_to_expression(x)
               )
               button.grid(row=grid[0],column=grid[1],sticky=tk.NSEW)
          

     # Function penghitungan
     def total(self):
          self.total_expression += self.current_expression
          self.update_total_label()
          try:
               self.current_expression = str(eval(self.total_expression)) # Melukan perhitungan
               self.total_expression = ""
          
          except ZeroDivisionError:
               self.current_expression = "Error"
          
          finally:
               self.update_label()
     
     # Fungsi button clear
     def clear(self):
          self.current_expression = ""
          self.total_expression = ""
          self.update_label()
          self.update_total_label()
     

     def create_operator_buttons(self):
          # Melakukan perulangan dictionary self.operations
          i = 0
          for operator,symbol in self.operations.items():
               button = tk.Button(self.buttons_frame,text=symbol,bg='gray11',fg='white',font=DEFAULT_FONT,borderwidth=0,command=lambda x=operator: self.append_operator(x))
               button.grid(row=i,column=4,sticky=tk.NSEW)
               i += 1
     
     # Meambahkan angka
     def add_to_expression(self,value):
          self.current_expression += str(value)
          self.update_label()
     
     # Menambahkan operator
     def append_operator(self,operator):
          if len(self.total_expression) > 0:
               if self.total_expression[-1] != operator :
                    self.current_expression += operator
                    self.total_expression = self.total_expression[0:len(self.total_expression)-1] + self.current_expression
          else:
               self.current_expression += operator
               self.total_expression += self.current_expression
          
          
          self.current_expression = ""
          self.update_total_label()
          self.update_label()


     # Button backspace
     def backspace(self):
          length = len(self.current_expression) # Menghitung panjang self.current_expression
          angka = ''
          for i in range(0,int(length)-1): # Looping
               angka = angka + self.current_expression[i] # Mengurangi i dan hasilnya di masukkan ke variabel angka

          self.current_expression = angka
          self.update_label()
               

     # Membuat Button clear
     def clear_button(self):
          button = tk.Button(self.buttons_frame,text="C",bg='gray11',fg='white',font=DEFAULT_FONT,borderwidth=0,command=self.clear)
          button.grid(row=0,column=1,sticky=tk.NSEW)
     
     # Membuat Button backspace
     def delete_button(self):
          button = tk.Button(self.buttons_frame,width=4,height=2,text="\u232B",bg='gray11',fg='white',font=DEFAULT_FONT,borderwidth=0,command=self.backspace)
          button.grid(row=0,column=0,pady=0,sticky=tk.NSEW)
     

     # Button Log
     def find_log(self):
          nilai = self.current_expression
          hasil = math.log(int(nilai))
          self.current_expression = str(hasil)
          self.update_label()
     
     def log_btn(self):
          button = tk.Button(self.buttons_frame,width=4,height=2,text="𝘭𝘰𝘨",bg='gray11',fg='white',font=SMALL_FONT,borderwidth=0,command=self.find_log)
          button.grid(row=4,column=0,pady=0,sticky=tk.NSEW)
     

     # Button Tan
     def find_tan(self):
          nilai = self.current_expression
          hasil = math.tan(int(nilai))
          self.current_expression = str(hasil)
          self.update_label()
     
     def tan_btn(self):
          button = tk.Button(self.buttons_frame,width=4,height=2,text="𝘵𝘢𝘯",bg='gray11',fg='white',font=SMALL_FONT,borderwidth=0,command=self.find_tan)
          button.grid(row=3,column=0,pady=0,sticky=tk.NSEW)
     
     # Button Sin
     def find_sin(self):
          nilai = self.current_expression
          hasil = math.sin(int(nilai))
          self.current_expression = str(hasil)
          self.update_label()
     
     def sin_btn(self):
          button = tk.Button(self.buttons_frame,width=4,height=2,text="𝘴𝘪𝘯",bg='gray11',fg='white',font=SMALL_FONT,borderwidth=0,command=self.find_cos)
          button.grid(row=2,column=0,pady=0,sticky=tk.NSEW)
     

     # Button Cos
     def find_cos(self):
          nilai = self.current_expression
          hasil = math.cos(int(nilai))
          self.current_expression = str(hasil)
          self.update_label()
     
     def cos_btn(self):
          button = tk.Button(self.buttons_frame,width=4,height=2,text="𝘤𝘰𝘴",bg='gray11',fg='white',font=SMALL_FONT,borderwidth=0,command=self.find_cos)
          button.grid(row=1,column=0,pady=0,sticky=tk.NSEW)
     
     # Membuat button =
     def equals_button(self):
          button = tk.Button(self.buttons_frame,text="＝",bg='orange',fg='white',borderwidth=0,command=self.total,font=("Arial",17))
          button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
     
     # Function Perpangkatan
     def squere(self):
          if self.current_expression == "": # Mengcheck nilai self.current_expression
               self.current_expression = ""
          
          # Jika bernilai maka code di bawah ini akan di eksekusi
          else:
               self.current_expression = str(eval(f"{self.current_expression}**2"))

          self.update_label()
     
     def create_square_buttons(self):
          button = tk.Button(self.buttons_frame,text="x\u00b2",bg='gray11',fg='white',font=DEFAULT_FONT,borderwidth=0,command=self.squere)
          button.grid(row=0,column=2,sticky=tk.NSEW)
     
     # Function perpangkatan
     def sqrt(self):
          if self.current_expression == "":
               self.current_expression = ""
          else:
               self.current_expression = str(eval(f"{self.current_expression}**0.5"))

          self.update_label()
     
     def create_sqrt_buttons(self):
          button = tk.Button(self.buttons_frame,text="\u221ax",bg='gray11',fg='white',font=DEFAULT_FONT,borderwidth=0,command=self.sqrt)
          button.grid(row=0,column=3,sticky=tk.NSEW)
     
     # Mengupdate variabel self.total_label
     def update_total_label(self):
          ex = self.total_expression
          for op,symbol in self.operations.items():
               ex = ex.replace(op,f' {symbol} ')
          self.total_label.config(text=ex)
     
     # Mengupdate variabel self.label
     def update_label(self):
          self.label.config(text=self.current_expression[:11])
     
     def create_buttons_frame(self):
          frame = tk.Frame(self.root)
          frame.pack(expand=True,fill="both")
          return frame
     

     def start(self):
          self.root.mainloop() # loop tak terbatas yang digunakan untuk menjalankan aplikasi, loop akan berhenti jika user menutup aplikasi


if __name__ == "__main__":
     try:
          (Kalkulator().start()) # Deklarasi Class Kalkulator dan Memanggil Method star yang ada di dalam Class Kalkulator
     
     except Exception as E:
          print(E)