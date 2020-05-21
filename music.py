from pygame import mixer
from timeit import default_timer as timer
mixer.init()
k=["Butta.mp3","Break.mp3","DDD.mp3","Tula.mp3","Sanam.mp3","Inkem.mp3","Makhna.mp3","Naina.mp3","New Rules.mp3","On.mp3"]
k1=["Buttabomo","Break","DDD","Tula Pahate Re","Sanam Re","Inkem Inkem","Makhna-Drive","Naina Lade","New Rules","On My Way"]
def rewind_1():
    mixer.music.rewind()
def load_1(text):
    mixer.music.load(text)
    mixer.music.set_volume(1)
def play_1():
    mixer.music.play()
def next_1(text_1,text_2):
    mixer.music.load(text_1)
    mixer.music.play(1)
    mixer.music.queue(text_2)
i=0   
text=k[i]
text_2=k[i+1]
load_1(text)
play_1()
mixer.music.queue(text_2) 
print("Press\n'p' to pause\n'r' to Resume\n'e' to Exit\n're'to Rewind the song \n'n' to Next Song\n'pre' to Previous Song\n's' to select the Song") 
while True:
    
    q=input(">>>>")
    if q=='p':
        mixer.music.pause()
        continue
    elif q=='r':
        mixer.music.unpause()
        continue
    elif q=='e':
        mixer.music.stop()
        break
    elif q=='re':
        rewind_1()
        continue
    elif q=='n':
        try:
            text_1=k[i+1]
            text_2=k[i+2]
            next_1(text_1,text_2)
            i=i+1
        except:
            text_1=k[i+1]
            text_2=k[-1]
            next_1(text_1,text_2)
            i=-1

    elif q=='pre':
        if i==0:
            text_1=k[-1]
            text_2=k[-2]
            next_1(text_1,text_2)
        else:
            text_1=k[i-1]
            text_2=k[i]
            next_1(text_1,text_2)
            i=i-1
    elif q=='s':
        input_1=input("Song number:")
        if input_1=='1':
            text_1=k[0]
            text_2=k[1]
            next_1(text_1,text_2)
            i=0
        elif input_1=='2':
            text_1=k[1]
            text_2=k[2]
            next_1(text_1,text_2)
            i=1
        elif input_1=='3': 
            text_1=k[2]
            text_2=k[3]
            next_1(text_1,text_2) 
            i=2
        elif input_1=='4':
            text_1=k[3]
            text_2=k[4]
            next_1(text_1,text_2)
            i=3
        elif input_1=='5':
            text_1=k[4]
            text_2=k[5]
            next_1(text_1,text_2)
            i=4
        elif input_1=='6':
            text_1=k[5]
            text_2=k[6]
            next_1(text_1,text_2)
            i=5
        elif input_1=='7':
            text_1=k[6]
            text_2=k[7]
            next_1(text_1,text_2)
            i=6
        elif input_1=='8':
            text_1=k[7]
            text_2=k[8]
            next_1(text_1,text_2)
            i=7
        elif input_1=='9':
            text_1=k[8]
            text_2=k[9]
            next_1(text_1,text_2)
            i=8
        elif input_1=='10':
            text_1=k[9]
            text_2=k[0]
            next_1(text_1,text_2)
            i=-1
    print("Playing:{}".format(k1[i]))


