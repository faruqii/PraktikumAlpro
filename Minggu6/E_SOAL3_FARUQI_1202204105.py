data = ["Faruqi","Suka","Makan","Nasi","Padang"]
def getIndex():
    indexing = int(input("Masukkan index: "))
    try:
        print("Data index ke -", indexing, "adalah", data[indexing])
    except IndexError:
        print("Index tidak ada")

getIndex()
