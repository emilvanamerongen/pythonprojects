__author__ = 'emilvanamerongen'
__version__ = '2.2'

print("welkom bij chromosomescan")
print("door Emil van Amerongen")
print("geoptimaliseerd voor grote bestanden")

# imports
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog as filedia

# global variables
regels = []
dna = ""
pernummer = 0

#tkinter
top = tkinter.Tk()

#plot een grafiek van het voorkomen van de codons uit de opgegeven sequentie
def per1000():
    bestandsnaam = f.get()
    bestand = open(bestandsnaam)
    lheide = l.get()
    lheid = int(lheide)
    rest = 0
    gc = 0
    teller = lheid
    teller2 = 0
    ticklist = []
    sequentie = ""
    totaal = 0
    totaallengte = 100
    ttot = 0
    restregel2 = ""
    for regel in bestand:
        if ">" in regel:
            regel = ""
        if len(regel) > 0:
            totaallengte = len(regel)
        if totaal < lheid-totaallengte:
            gp = regel.count("G")
            tp = regel.count("T")
            ap = regel.count("A")
            cp = regel.count("C")
            gc += gp + cp
            totaal += gp + cp + ap + tp
        else:
            regelletters = regel.count("G") + regel.count("T") + regel.count("A") + regel.count("C")
            restregel = regel[:(lheid-totaal)]
            restregel2 = regel[(lheid-totaal):]
            gp = restregel.count("G")
            tp = restregel.count("T")
            ap = restregel.count("A")
            cp = restregel.count("C")
            gc += gp + cp
            totaal += gp + cp + ap + tp
        if totaal >= lheid:
            ticklist.append(ttot)
            plt.bar(height=(gc-((totaal-lheid)/2))/(lheid-(totaal-lheid))*100, left=teller-lheid, width=lheid )
            ttot += totaal
            teller += lheid
            totaal=0
            gc =0
            gp = restregel2.count("G")
            tp = restregel2.count("T")
            ap = restregel2.count("A")
            cp = restregel2.count("C")
            gc += gp + cp
            totaal += gp + cp + ap + tp
            print(ttot)

    ticklist.append(teller-lheid)
    plt.bar(height=(gc-((totaal-teller)/2))/(totaal-(totaal-teller))*100, left=teller-lheid, width=lheid )
    ttot += totaal
    plt.ylabel("gc percentage (%)")
    plt.xlabel("aantal basen")
    plt.show()


def pieplot():
    bestandsnaam = f.get()
    bestand = open(bestandsnaam)
    gp=0
    tp=0
    ap=0
    cp=0
    for regel in bestand:
            gp += regel.count("G")
            tp += regel.count("T")
            ap += regel.count("A")
            cp += regel.count("C")
    rest = ap + tp
    tgc = cp + gp
    print(rest+tgc)
    labels = 'GC', 'rest(AT)'
    sizes = [tgc, rest]
    colors = ['lightskyblue', 'gold']
    explode = (0, 0.1) # only "explode" the 2nd slice (i.e. 'Hogs')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
#tkinter commando's

#sluit alle vensters
def afsluiten():
    top.destroy()
    plt.close()

def openbestand():
    bestandsnaam = filedia.askopenfilename()
    f.insert(0, bestandsnaam)

#tkinter UI onderdelen
top.wm_title("chromo-scan2.2")
onder = tkinter.Grid()
f = tkinter.Entry()
g = tkinter.Label(top, text="bestandsnaam:")
s = tkinter.Button(top, text="afsluiten", command = afsluiten)
d=tkinter.Button(top, text="open", command = openbestand)

g.pack()
d.pack()
f.pack()
a=tkinter.Label(top, text="--------------------------------------------------")
u=tkinter.Label(top, text="maak een histogram per:")
l=tkinter.Entry()
c=tkinter.Button(top, text="maak histogram", command = per1000)
k=tkinter.Button(top, text="maak GC% pie", command = pieplot)
c.pack()
a.pack()
u.pack()
l.pack()
c.pack()
f.delete(0, )
a.pack()
k.pack()
s.pack()
top.mainloop()