import tkinter as tk
from tkinter import messagebox
import random

class Kelime4:
    def __init__(self):
        self.tutulan_kelime = self.kelime()  # Oyun başında bir kelime seç
        self.deneme_sayisi = 0  # Deneme sayısını sıfırla
        self.kullanici_tahmini = "****"
        self.root = tk.Tk()
        self.root.title("Kelime4")
        self.panel_genislik = 80
        self.panel_yukseklik = 80
        self.panel_arasi = 10
        self.panel_saydam_yukseklik = self.panel_yukseklik + (self.panel_arasi * 2)
        self.panel_x = self.panel_arasi
        self.panel_y = self.panel_arasi
        self.frame_genislik = (7000 * self.panel_genislik) + (10000 * self.panel_arasi)
        self.frame_yukseklik = (6 * self.panel_saydam_yukseklik) + (7 * self.panel_arasi) 
        self.framesaydam = tk.Frame(self.root, bg="lightblue", width=self.frame_genislik, height=self.frame_yukseklik)
        self.framesaydam.pack()
        self.olustur()
        self.root.mainloop()
    
    @staticmethod
    def kelime():
        kelimeler = ["kasa", "masa", "lale", "ayva", "elma", "park", "para", "kafa", "ödev", "ödül","kalp","priz","örtü","duru","küpe","erik","hata","dize","uzun","kısa"]
        r = random.randint(0, 19)
        return kelimeler[r].upper()

    def dort_harfli_panel(self, panel_no, tahmin):
        panel = tk.Frame(self.framesaydam, bg="lightgray", width=self.panel_genislik, height=self.panel_saydam_yukseklik)
        panel.grid(row=panel_no, column=0, padx=self.panel_arasi, pady=self.panel_arasi)
        
        harfler = [harf for harf in tahmin]
        tutulan_harfler = [harf for harf in self.tutulan_kelime]

        for i in range(4):
            harf = harfler[i]
            harf_renk = self.harf_renk_ayarla(harf, tutulan_harfler[i])
            label = tk.Label(panel, text=harf, font=("Ubuntu", 40, "bold"), bg=harf_renk, padx=5, pady=5)
            label.grid(row=0, column=i, padx=self.panel_arasi, pady=self.panel_arasi)

    def tahmin_paneli(self, tahmin_no):
        tahmin_frame = tk.Frame(self.framesaydam, bg="lightblue", width=self.panel_genislik, height=self.panel_yukseklik)
        tahmin_frame.grid(row=tahmin_no, column=1, padx=self.panel_arasi, pady=self.panel_arasi)


        label_tahmin = tk.Label(tahmin_frame, text=f"{tahmin_no}/5. Tahmin", font=("Ubuntu", 10, "bold"), bg="lightblue")
        label_tahmin.grid(row=0, column=0, padx=5, pady=5)

        entry = tk.Entry(tahmin_frame, width=8)
        entry.grid(row=1, column=0, padx=5, pady=5)

        button = tk.Button(tahmin_frame, text="Göster", command=lambda: self.tahmin_yap(entry.get(), tahmin_no))
        button.grid(row=2, column=0, padx=5, pady=5)

    def tahmin_yap(self, tahmin, tahmin_no):
        self.kullanici_tahmini = tahmin.upper()

        if self.kullanici_tahmini == self.tutulan_kelime:
            messagebox.showinfo("Tebrikler!", f"Doğru kelimeyi buldunuz: {self.tutulan_kelime}")
            self.dort_harfli_panel(0, self.kullanici_tahmini)
            self.dort_harfli_panel(tahmin_no, self.kullanici_tahmini)
        else:
            self.dort_harfli_panel(tahmin_no, self.kullanici_tahmini)

        if tahmin_no == 5:  # Son tahmin yapıldığında
            messagebox.showinfo("Üzgünüm", f"Doğru kelimeyi bulamadınız. Doğru kelime: {self.tutulan_kelime}")
            self.dort_harfli_panel(0, self.tutulan_kelime)
        
        self.deneme_sayisi += 1  # Her tahmin sonrası deneme sayısını artır

        if self.deneme_sayisi == 5:  # 5 deneme hakkı bittiğinde
            messagebox.showinfo("5 deneme hakkınız bitti", f"Doğru Kelime:{self.tutulan_kelime}")
            print("5 deneme hakkınız bitti. Doğru kelime:", self.tutulan_kelime)

    def olustur(self):
        for i in range(6):
            self.dort_harfli_panel(i, self.kullanici_tahmini)
        
        for i in range(1, 6):
            self.tahmin_paneli(i)

    @staticmethod
    def harf_renk_ayarla(harf, tutulan_kelime):
        if harf == "*":
         return "lightblue"
        elif harf in tutulan_kelime:
            if tutulan_kelime.index(harf) == tutulan_kelime.index(tutulan_kelime):
             return "lightgreen"
            else:
             return "lightyellow"
        else:
          return "lightcoral"
if __name__ == "__main__":
    Kelime4()


 