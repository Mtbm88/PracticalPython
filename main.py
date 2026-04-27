from gtts import gTTS 
import os

#texto = "Me gusta comer palmeritas"
texto = input("que te gustaria decir?")

output = gTTS(texto,lang="es", slow=False) #no te olvides que los booleanos van con mayusculas y poner los =
output.save("output.mp3") #aca se guarda

os.system("open output.mp3") #en linux es open en windows start, esto reproduce el audio


#en este proyecto probamos como funciona la libreria gtts, y como os manipula el sistema para abrir el programa de repŕoduccion de audio 
#pregunta para indagar despues os sirve para crear payloads??
#me dicen por cucaracha que os es equivalente a escribir en la terminal pero usando python lo que indica que si se puede usar para crear payloads
