def pertambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b

def main():
    print("Program Kalkulator Sederhana")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    pilihan = int(input("Pilih operasi (1/2/3/4): "))

    if pilihan == 1:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print(f"Hasil pertambahan: {pertambahan(a, b)}")
    elif pilihan == 2:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print(f"Hasil pengurangan: {pengurangan(a, b)}")
    elif pilihan == 3:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print(f"Hasil perkalian: {perkalian(a, b)}")
    elif pilihan == 4:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print(f"Hasil pembagian: {pembagian(a, b)}")
    elif pilihan == 5:
        print("Terima kasih telah menggunakan program ini!")
        return
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
