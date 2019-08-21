import goslate
try:
      f=open("file.txt","r")
      text=f.read()
      gs = goslate.Goslate()
      translatedText = gs.translate(text,'ta')
      print(translatedText)
except IOError:
      print("Connect the Internet \n Check the File")
