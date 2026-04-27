from gtts import gTTS
import os

with open('demo.txt', 'r', encoding="utf-8") as file: 
        texto = file.read()

#print (texto)

output = gTTS(texto, lang='es', slow=False)
output.save("output_2.mp3")

os.system('open output_2.mp3')

