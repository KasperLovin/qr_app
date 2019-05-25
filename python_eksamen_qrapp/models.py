class SaveFile():

    def __init__(self):
        pass

    @classmethod
    def savenewfile(cls, url):
        handle1 = open('file.txt', 'r+') #x ny fil, r+ overskriv gammel
        handle1.write(url)
        handle1.close()

