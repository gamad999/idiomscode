import tkinter as tk
from playsound import playsound
import random
from tkinter import messagebox
import sqlite3

raiz = tk.Tk()
raiz.title("IDIOMS CODE")
#raiz.geometry("1000x550")


marcoPresnt = tk.Frame(raiz)

marcoPresnt.pack()


Moon = tk.PhotoImage(file="OnceInABlueMoon.png")
acth = tk.PhotoImage(file="ASLTW.png")
Presentacion = tk.Label(marcoPresnt, image=Moon)
Presentacion.pack()
hear = tk.PhotoImage(file="hear.png")
iniRiddle = "inicioRiddle.mp3"
crtPlayersonido = "createPlayer.mp3"
crtedPlayerExito = "playerActivated.mp3"
playerHasNoGems = "noGemsPlayer.mp3"
premGem = "premioGem.mp3"
explanCoin = "explnCoins.mp3"
explanGem = "explnGems.mp3"
gemsGanadas = 0

nickname = tk.StringVar()
#record = [(0,"",0,0,0,0)]
score = 0
scoreAcumulado = 0
lifes = -1
lifesAc = 0
goldCoins = 0

nicknameText = tk.Label(marcoPresnt, text = "Nickname", font = ("Comic Sans MS", 12))
nicknameText.config(fg = "white", bg = "blue")
nicknameText.place(x=100, y=440)

nicknameCuad = tk.Entry(marcoPresnt, textvariable=nickname, font = ("Comic Sans MS", 14), justify = "center")
nicknameCuad.config(bg="black", fg="green")
nicknameCuad.place(x=10, y=480)

actBoton = tk.Button(marcoPresnt, text="Activate player", font = ("Comic Sans MS", 11), command=lambda:crearJugador())
actBoton.config(fg="blue")
actBoton.place(x=270, y=480)

quitBoton = tk.Button(marcoPresnt, text="Quit game", font = ("Comic Sans MS", 11), command=lambda:quitjuego())
quitBoton.config(fg="blue")
quitBoton.place(x=420, y=480)

def quitjuego():

	if nickname.get() != "" and lifes >= 0:

		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()

		raiz.destroy()

	elif lifes < 0:
		raiz.destroy()



def crearJugador():

	global record
	global score
	global scoreAcumulado
	global lifes
	global lifesAc
	global goldCoins
	global gemsGanadas

	conexion1 = sqlite3.connect("players")
	cursor1 = conexion1.cursor()

	sql = "insert into playeridiom(nickname, gems, goldcoins, score, gemsgand) values(?, ?, ?, ?, ?)"
	datos = (nickname.get(), 4, 0, 100, 0)
	sql2 = "select * from playeridiom where nickname = (?)"
	dato = (nickname.get(),)

	cursor1.execute(sql2, dato)
	dt = cursor1.fetchall()

	if len(dt) == 0:

		cursor1.execute(sql, datos)
		cursor1.execute(sql2, dato)
		record = cursor1.fetchall()
		score = record[0][4]
		scoreAcumulado = record[0][4]
		lifes = record[0][2] - 1
		lifesAc = record[0][2]
		goldCoins = record[0][3]
		gemsGanadas = record[0][5]
		playsound(crtPlayersonido)
		playsound(crtedPlayerExito)



	elif dt[0][2] > 0:

		score = dt[0][4]
		scoreAcumulado = dt[0][4]
		lifes = dt[0][2] - 1
		lifesAc = dt[0][2]
		goldCoins = dt[0][3]
		gemsGanadas = dt[0][5]
		playsound(crtPlayersonido)
		playsound(crtedPlayerExito)

	elif dt[0][2] <= 0:

		playsound(playerHasNoGems)


	conexion1.commit()
	conexion1.close()

	


words = ["be a bit much","a bit of skirt", "a bit on the side", "not a bit of it", "a bit of rough", "get the bit between your teeth",
"be in bits", "be living in a dream world", "a mug's game", "in a dream", "never in your wildest dreams", "wouldn't dream of doing something",
"in your mind's eye", "think outside the box", "a reach of the imagination", "work like a dream", "come back down to earth",
"as it comes", "something to shout about", "the boy next door", "clean up your act", "as and when", "under the wire", "about-face",
"a new broom sweeps clean", "a mistery to me", "a narrow squeak", "a feather in your cap", "put something to bed", "actions speak louder than words",
"a bird in the hand is worth two in the bush", "all things being equal", "be in someone's shoes", "it's a funny old world",
"have the wind at your back", "around robin hood's barn", "what's cooking?", "blessing in disguise", "while the cat's away, the mice will play",
"a chip off the old block", "add fuel to the fire", "talk smack", "be a dime a dozen", "a friend in need is a friend indeed",
"a leopard doesn't change its spots", "a stitch in time saves nine", "enough is enough", "once in a blue moon", "be barking up the wrong tree",
"let the cat out of the bag", "all that glitters is not gold", "a penny saved is a penny earned", "a piece of cake", "lipstick on a pig",
"a rolling stone gathers no moss", "at the drop of a hat", "know on which side one's bread is buttered", "a million and one thoughts",
"a two cents plane", "act one's age", "afraid of one's own shadow", "after one's own heart", "ahead of the game", "ahead of time",
"alive with", "all at sea", "all in", "all the same", "all there", "all wet", "and as if that weren't enough", "apple-pie order", "around the clock",
"as quick as a wink", "as the crow flies", "ask for the moon", "at one's beck and call", "at one's wit's end", "at sixes and sevens",
"back to the salt mines", "bag and baggage", "ball of fire", "ball up", "barge in", "be becoming", "be bound for", "be carried away",
"be cut out for", "be fond of", "be had", "be hard put", "be in a rush", "be into", "be looking up", "be of no account", "be off like a shot",
"be out of the question", "be up for grabs", "be up to something", "be well off", "bear in mind", "bear up", "bear with", "bear about the bush",
"beat it", "beat one's brains out", "bed of roses", "before one's time", "beforehand", "behind one's back", "behind the eight ball",
"beside the point", "best man", "better half", "better off", "between the devil and the deep sea", "big deal", "big hand", "big stink",
"big time", "bind oneself", "break in", "bring about", "bug someone", "build up", "butt in", "buy it", "by heart", "by which to abide",
"call a spade a spade", "call down", "call it a day", "call someone names", "call the shots", "cancel out", "can of worms", "can't help",
"can't see the forest for the trees", "carrot and stick", "carry the ball", "cart before the horse", "catch a few rays", "catch up with somebody",
"charley horse", "check up on somebody", "chew the fat", "chickenfeed", "chicken-hearted", "child's play", "chip off the old block",
"take someone aback", "know what you are about", "above yourself", "not be above", "the acceptable face of something", "hold all the aces"]

idiomMeans = ["idiom1.mp3", "idiom2.mp3", "idiom3.mp3", "idiom4.mp3", "idiom5.mp3", "idiom6.mp3", "idiom7.mp3", "idiom8.mp3",
"idiom9.mp3", "idiom10.mp3", "idiom11.mp3", "idiom12.mp3", "idiom13.mp3", "idiom14.mp3", "idiom15.mp3", "idiom16.mp3", "idiom17.mp3",
"idiom18.mp3", "idiom19.mp3", "idiom20.mp3", "idiom21.mp3", "idiom22.mp3", "idiom23.mp3", "idiom24.mp3", "idiom25.mp3", "idiom26.mp3", "idiom27.mp3",
"idiom28.mp3", "idiom29.mp3", "idiom30.mp3", "idiom31.mp3", "idiom32.mp3", "idiom33.mp3", "idiom34.mp3", "idiom35.mp3", "idiom36.mp3", "idiom37.mp3",
"idiom38.mp3", "idiom39.mp3", "idiom40.mp3", "idiom41.mp3", "idiom42.mp3", "idiom43.mp3", "idiom44.mp3", "idiom45.mp3", "idiom46.mp3",
"idiom47.mp3", "idiom48.mp3", "idiom49.mp3", "idiom50.mp3", "idiom51.mp3", "idiom52.mp3", "idiom53.mp3", "idiom54.mp3", "idiom55.mp3",
"idiom56.mp3", "idiom57.mp3", "idiom58.mp3", "idiom59.mp3", "idiom60.mp3", "idiom61.mp3", "idiom62.mp3", "idiom63.mp3", "idiom64.mp3",
"idiom65.mp3", "idiom66.mp3", "idiom67.mp3", "idiom68.mp3", "idiom69.mp3", "idiom70.mp3", "idiom71.mp3", "idiom72.mp3", "idiom73.mp3",
"idiom74.mp3", "idiom75.mp3", "idiom76.mp3", "idiom77.mp3", "idiom78.mp3", "idiom79.mp3", "idiom80.mp3", "idiom81.mp3", "idiom82.mp3",
"idiom83.mp3", "idiom84.mp3", "idiom85.mp3", "idiom86.mp3", "idiom87.mp3", "idiom88.mp3", "idiom89.mp3", "idiom90.mp3", "idiom91.mp3",
"idiom92.mp3", "idiom93.mp3", "idiom94.mp3", "idiom95.mp3", "idiom96.mp3", "idiom97.mp3", "idiom98.mp3", "idiom99.mp3", "idiom100.mp3",
"idiom101.mp3", "idiom102.mp3", "idiom103.mp3", "idiom104.mp3", "idiom105.mp3", "idiom106.mp3", "idiom107.mp3", "idiom108.mp3",
"idiom109.mp3", "idiom110.mp3", "idiom111.mp3", "idiom112.mp3", "idiom113.mp3", "idiom114.mp3", "idiom115.mp3", "idiom116.mp3",
"idiom117.mp3", "idiom118.mp3", "idiom119.mp3", "idiom120.mp3", "idiom121.mp3", "idiom122.mp3", "idiom123.mp3", "idiom124.mp3",
"idiom125.mp3", "idiom126.mp3", "idiom127.mp3", "idiom128.mp3", "idiom129.mp3", "idiom130.mp3", "idiom131.mp3", "idiom132.mp3",
"idiom133.mp3", "idiom134.mp3", "idiom135.mp3", "idiom136.mp3", "idiom137.mp3", "idiom138.mp3", "idiom139.mp3", "idiom140.mp3",
"idiom141.mp3", "idiom142.mp3", "idiom143.mp3", "idiom144.mp3", "idiom145.mp3", "idiom146.mp3", "idiom147.mp3", "idiom148.mp3",
"idiom149.mp3", "idiom150.mp3", "idiom151.mp3", "idiom152.mp3", "idiom153.mp3", "idiom154.mp3", "idiom155.mp3", "idiom156.mp3"]

idiomExamples = ["idiom1EX.mp3", "idiom2EX.mp3", "idiom3EX.mp3", "idiom4EX.mp3", "idiom5EX.mp3", "idiom6EX.mp3", "idiom7EX.mp3", "idiom8EX.mp3",
"idiom9EX.mp3", "idiom10EX.mp3", "idiom11EX.mp3", "idiom12EX.mp3", "idiom13EX.mp3", "idiom14EX.mp3", "idiom15EX.mp3", "idiom16EX.mp3", "idiom17EX.mp3",
"idiom18EX.mp3", "idiom19EX.mp3", "idiom20EX.mp3", "idiom21EX.mp3", "idiom22EX.mp3", "idiom23EX.mp3", "idiom24EX.mp3", "idiom25EX.mp3", "idiom26EX.mp3", "idiom27EX.mp3",
"idiom28EX.mp3", "idiom29EX.mp3", "idiom30EX.mp3", "idiom31EX.mp3", "idiom32EX.mp3", "idiom33EX.mp3", "idiom34EX.mp3", "idiom35EX.mp3", "idiom36EX.mp3", "idiom37EX.mp3",
"idiom38EX.mp3", "idiom39EX.mp3", "idiom40EX.mp3", "idiom41EX.mp3", "idiom42EX.mp3", "idiom43EX.mp3", "idiom44EX.mp3", "idiom45EX.mp3",
"idiom46EX.mp3", "idiom47EX.mp3", "idiom48EX.mp3", "idiom49EX.mp3", "idiom50EX.mp3", "idiom51EX.mp3", "idiom52EX.mp3", "idiom53EX.mp3", "idiom54EX.mp3", "idiom55EX.mp3",
"idiom56EX.mp3", "idiom57EX.mp3", "idiom58EX.mp3", "idiom59EX.mp3", "idiom60EX.mp3", "idiom61EX.mp3", "idiom62EX.mp3", "idiom63EX.mp3", "idiom64EX.mp3", "idiom65EX.mp3",
"idiom66EX.mp3", "idiom67EX.mp3", "idiom68EX.mp3", "idiom69EX.mp3", "idiom70EX.mp3", "idiom71EX.mp3", "idiom72EX.mp3", "idiom73EX.mp3", "idiom74EX.mp3", "idiom75EX.mp3",
"idiom76EX.mp3", "idiom77EX.mp3", "idiom78EX.mp3", "idiom79EX.mp3", "idiom80EX.mp3", "idiom81EX.mp3", "idiom82EX.mp3", "idiom83EX.mp3", "idiom84EX.mp3", "idiom85EX.mp3",
"idiom86EX.mp3", "idiom87EX.mp3", "idiom88EX.mp3", "idiom89EX.mp3", "idiom90EX.mp3", "idiom91EX.mp3", "idiom92EX.mp3", "idiom93EX.mp3", "idiom94EX.mp3", "idiom95EX.mp3",
"idiom96EX.mp3", "idiom97EX.mp3", "idiom98EX.mp3", "idiom99EX.mp3", "idiom100EX.mp3", "idiom101EX.mp3", "idiom102EX.mp3", "idiom103EX.mp3",
"idiom104EX.mp3", "idiom105EX.mp3", "idiom106EX.mp3", "idiom107EX.mp3", "idiom108EX.mp3", "idiom109EX.mp3", "idiom110EX.mp3", "idiom111EX.mp3",
"idiom112EX.mp3", "idiom113EX.mp3", "idiom114EX.mp3", "idiom115EX.mp3", "idiom116EX.mp3", "idiom117EX.mp3", "idiom118EX.mp3", "idiom119EX.mp3",
"idiom120EX.mp3", "idiom121EX.mp3", "idiom122EX.mp3", "idiom123EX.mp3", "idiom124EX.mp3", "idiom125EX.mp3", "idiom126EX.mp3", "idiom127EX.mp3",
"idiom128EX.mp3", "idiom129EX.mp3", "idiom130EX.mp3", "idiom131EX.mp3", "idiom132EX.mp3", "idiom133EX.mp3", "idiom134EX.mp3", "idiom135EX.mp3",
"idiom136EX.mp3", "idiom137EX.mp3", "idiom138EX.mp3", "idiom139EX.mp3", "idiom140EX.mp3", "idiom141EX.mp3", "idiom142EX.mp3", "idiom143EX.mp3",
"idiom144EX.mp3", "idiom145EX.mp3", "idiom146EX.mp3", "idiom147EX.mp3", "idiom148EX.mp3", "idiom149EX.mp3", "idiom150EX.mp3", "idiom151EX.mp3",
"idiom152EX.mp3", "idiom153EX.mp3", "idiom154EX.mp3", "idiom155EX.mp3", "idiom156EX.mp3"]


mision = -1
listMision = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15", "M16",
"M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33",
"M34", "M35", "M36", "M37", "M38", "M39", "M40", "M41", "M42", "M43", "M44", "M45", "M46", "M47", "M48", "M49", "M50",
"M51", "M52", "M53", "M54", "M55", "M56", "M57", "M58", "M59", "M60", "M61", "M62", "M63", "M64", "M65", "M66", "M67",
"M68", "M69", "M70", "M71", "M72", "M73", "M74", "M75", "M76", "M77", "M78", "M79", "M80", "M81", "M82", "M83", "M84",
"M85", "M86", "M87", "M88", "M89", "M90", "M91", "M92", "M93", "M94", "M95", "M96", "M97", "M98", "M99", "M100", "M101",
"M102", "M103", "M104", "M105", "M106", "M107", "M108", "M109", "M110", "M111", "M112", "M113", "M114", "M115", "M116",
"M117", "M118", "M119", "M120", "M121", "M122", "M123", "M124", "M125", "M126", "M127", "M128", "M129", "M130", "M131",
"M132", "M133", "M134", "M135", "M136", "M137", "M138", "M139", "M140", "M141", "M142", "M143", "M144", "M145", "M146",
"M147", "M148", "M149", "M150", "M151", "M152", "M153", "M154", "M155", "M156"]

indice = ""
secretWord = ""
blanks = ""
correctLetters = 0
correctLettersDsp = ""
missedLetters = ""
alreadyLetters = ""
#score = record[4]
#scoreAcumulado = record[4]
wrongs = 0
#lifes = record[2] - 1
#lifesAc = record[2]
gameOver = False
guessSecWord = False
passedMissions = -1
avisoGuess = 0
runOut = False
avisoRunOut = 0
#goldCoins = record[3]
ganancia = "donkey.mp3"
perdida = "faily.mp3"
ganarPantalla = "monedas_1.mp3"
Verd = tk.PhotoImage(file="Verdugo200.png")
Verd2 = tk.PhotoImage(file="VerdugoPass1.png")
jimmy = "Jimmy.mp3"
imnUse = tk.PhotoImage(file="IdiomUse.png")
coinbatt = tk.PhotoImage(file="Coin.png")
gembatt = tk.PhotoImage(file="Gem.png")
exceUse = "exceptEx.mp3"
risaJim = "risaJimmy.mp3"
risaFin = "risaFinal.mp3"
gemLostt = "gemLost.mp3"
#if reset_CrLetters:
#	correctLetters = 0


def cambiarImagen():

	Presentacion.config(image=acth)



def createNewWindow():

	global words
	global idiomMeans
	global listMision
	global mision
	global secretWord
	global indice
	global blanks
	global correctLettersDsp
	global missedLetters
	global score
	global scoreAcumulado
	global guessSecWord
	global passedMissions
	global idiomMeans
	global Verd
	global hear
	global jimmy
	global imnUse
	global coinbatt
	global gembatt
	global goldCoins
	global lifes
	global lifesAc
	global iniRiddle
	global Verd2
	global marcoAhorc
	

	if passedMissions == mision and nickname.get() != "" and lifes >= 0:

		mision = mision + 1
		
		
		#if mision <= 7:
		#	indice = random.randint(0, 7-mision)

		#elif 7 < mision <= 15:
		#	indice = random.randint(0, 15-mision)

		#elif 15 < mision <= 20:
		#	indice = random.randint(0, 20-mision)

		playsound(iniRiddle)
		indice = random.randint(0, len(words)-1)
		secretWord = words[indice]
		blanks = tk.StringVar(value="*" * len(secretWord))
		correctLettersDsp = tk.StringVar(value="")
		missedLetters = tk.StringVar(value="")
		score = tk.IntVar(value=(0 + scoreAcumulado))
		lifesAc = tk.IntVar(value=lifes + 1)


		listMision[mision] = tk.Toplevel(raiz)
		listMision[mision].geometry("995x550")
		listMision[mision].title("IDIOMS CODE")
		listMision[mision].config(bg="#0FCDCA")
		
		#marcoBienv = tk.Frame(listMision[mision])
		#marcoBienv.place(x=10, y=10)
		

		#munecoAhorc = tk.PhotoImage(file83ahorcado2.png")
		marcoAhorc = tk.Button(listMision[mision], image=Verd, command=lambda:jim())
		marcoAhorc.config(bg="#0FCDCA")
		marcoAhorc.place(x=88, y=350)

		

		Bienvenida = tk.Label(listMision[mision], text="IDIOMS CODE", font=("Comic Sans MS", 32))
		Bienvenida.config(fg="#243032", bg="#0FCDCA", padx=10)
		Bienvenida.place(x=15, y=20)

		miFrame = tk.Frame(listMision[mision])
		miFrame.place(x=60, y=100)
		#miFrame.config(padx=10, pady=20)

		#------------------------fila 1-------------------------------------

		botonQ = tk.Button(miFrame, text="A", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("a"), guessSecretWord(), runOutGuess()])
		botonQ.grid(row=0, column=1)
		botonQ.config(fg="#2D0F85")
		botonW = tk.Button(miFrame, text="B", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("b"), guessSecretWord(), runOutGuess()])
		botonW.grid(row=0, column=2)
		botonW.config(fg="#2D0F85")
		botonE = tk.Button(miFrame, text="C", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("c"), guessSecretWord(), runOutGuess()])
		botonE.grid(row=0, column=3)
		botonE.config(fg="#2D0F85")
		botonR = tk.Button(miFrame, text="D", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("d"), guessSecretWord(), runOutGuess()])
		botonR.grid(row=0, column=4)
		botonR.config(fg="#2D0F85")
		botonT = tk.Button(miFrame, text="E", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("e"), guessSecretWord(), runOutGuess()])
		botonT.grid(row=0, column=5)
		botonT.config(fg="#2D0F85")

		#------------------------fila 2-------------------------------------

		botonY = tk.Button(miFrame, text="F", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("f"), guessSecretWord(), runOutGuess()])
		botonY.grid(row=1, column=1)
		botonY.config(fg="#2D0F85")
		botonU = tk.Button(miFrame, text="G", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("g"), guessSecretWord(), runOutGuess()])
		botonU.grid(row=1, column=2)
		botonU.config(fg="#2D0F85")
		botonI = tk.Button(miFrame, text="H", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("h"), guessSecretWord(), runOutGuess()])
		botonI.grid(row=1, column=3)
		botonI.config(fg="#2D0F85")
		botonO = tk.Button(miFrame, text="I", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("i"), guessSecretWord(), runOutGuess()])
		botonO.grid(row=1, column=4)
		botonO.config(fg="#2D0F85")
		botonP = tk.Button(miFrame, text="J", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("j"), guessSecretWord(), runOutGuess()])
		botonP.grid(row=1, column=5)
		botonP.config(fg="#2D0F85")

		#------------------------fila 3-------------------------------------

		botonA = tk.Button(miFrame, text="K", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("k"), guessSecretWord(), runOutGuess()])
		botonA.grid(row=2, column=1)
		botonA.config(fg="#2D0F85")
		botonS = tk.Button(miFrame, text="L", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("l"), guessSecretWord(), runOutGuess()])
		botonS.grid(row=2, column=2)
		botonS.config(fg="#2D0F85")
		botonD = tk.Button(miFrame, text="M", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("m"), guessSecretWord(), runOutGuess()])
		botonD.grid(row=2, column=3)
		botonD.config(fg="#2D0F85")
		botonF = tk.Button(miFrame, text="N", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("n"), guessSecretWord(), runOutGuess()])
		botonF.grid(row=2, column=4)
		botonF.config(fg="#2D0F85")
		botonG = tk.Button(miFrame, text="O", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("o"), guessSecretWord(), runOutGuess()])
		botonG.grid(row=2, column=5)
		botonG.config(fg="#2D0F85")

		#------------------------fila 4-------------------------------------

		botonH = tk.Button(miFrame, text="P", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("p"), guessSecretWord(), runOutGuess()])
		botonH.grid(row=3, column=1)
		botonH.config(fg="#2D0F85")
		botonJ = tk.Button(miFrame, text="Q", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("q"), guessSecretWord(), runOutGuess()])
		botonJ.grid(row=3, column=2)
		botonJ.config(fg="#2D0F85")
		botonK = tk.Button(miFrame, text="R", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("r"), guessSecretWord(), runOutGuess()])
		botonK.grid(row=3, column=3)
		botonK.config(fg="#2D0F85")
		botonL = tk.Button(miFrame, text="S", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("s"), guessSecretWord(), runOutGuess()])
		botonL.grid(row=3, column=4)
		botonL.config(fg="#2D0F85")
		botonZ = tk.Button(miFrame, text="T", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("t"), guessSecretWord(), runOutGuess()])
		botonZ.grid(row=3, column=5)
		botonZ.config(fg="#2D0F85")


		#------------------------fila 5-------------------------------------

		botonX = tk.Button(miFrame, text="U", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("u"), guessSecretWord(), runOutGuess()])
		botonX.grid(row=4, column=1)
		botonX.config(fg="#2D0F85")
		botonC = tk.Button(miFrame, text="V", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("v"), guessSecretWord(), runOutGuess()])
		botonC.grid(row=4, column=2)
		botonC.config(fg="#2D0F85")
		botonV = tk.Button(miFrame, text="W", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("w"), guessSecretWord(), runOutGuess()])
		botonV.grid(row=4, column=3)
		botonV.config(fg="#2D0F85")
		botonB = tk.Button(miFrame, text="X", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("x"), guessSecretWord(), runOutGuess()])
		botonB.grid(row=4, column=4)
		botonB.config(fg="#2D0F85")
		botonN = tk.Button(miFrame, text="Y", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("y"), guessSecretWord(), runOutGuess()])
		botonN.grid(row=4, column=5)
		botonN.config(fg="#2D0F85")

		#-------------------------fila 6----------------------------------------------

		botonM = tk.Button(miFrame, text="Z", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("z"), guessSecretWord(), runOutGuess()])
		botonM.grid(row=5, column=1)
		botonM.config(fg="#2D0F85")
		botonApost = tk.Button(miFrame, text="'", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("'"), guessSecretWord(), runOutGuess()])
		botonApost.grid(row=5, column=2)
		botonApost.config(fg="#2D0F85")
		botonRaya = tk.Button(miFrame, text="-", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("-"), guessSecretWord(), runOutGuess()])
		botonRaya.grid(row=5, column=3)
		botonRaya.config(fg="#2D0F85")
		botonComa = tk.Button(miFrame, text=",", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada(","), guessSecretWord(), runOutGuess()])
		botonComa.grid(row=5, column=4)
		botonComa.config(fg="#2D0F85")
		botonPreg = tk.Button(miFrame, text="?", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("?"), guessSecretWord(), runOutGuess()])
		botonPreg.grid(row=5, column=5)
		botonPreg.config(fg="#2D0F85")
		botonEspacio = tk.Button(miFrame, text="                                                  ", font=("Comic Sans MS", 10), command=lambda:[letraPulsada(" "), guessSecretWord(), runOutGuess()])
		botonEspacio.grid(row=6, column=1, columnspan=5)


		#Rid = tk.Frame(listMision[mision])
		#Rid.grid(row=0, column=1, padx=100)
		#Rid.config(background="#F9D8F8")
		#secretWord = Label(board, text=words[index])
		#secretWord.grid(row=0, column=0)

		#board = tk.Frame(listMision[mision])
		#board.place(x=280, y=10)

		#etiqRiddle = tk.Label(listMision[mision], text="Riddle", font=("Lucida Calligraphy", 13,))
		#etiqRiddle.place(x=440, y=15)
		#etiqRiddle.config(fg="#3A0338", bg="#944DBD")

		#riddle = tk.Label(listMision[mision], text=riddles[indice], font=("Lucida Calligraphy", 12))
		#riddle.place(x=350, y=50)
		#riddle.config(fg="#3A0338", bg="#944DBD")

		etiqSecretWord = tk.Label(listMision[mision], text="Idiom's Secret Words", font=("Comic Sans MS", 20))
		etiqSecretWord.place(x=520, y=30)
		etiqSecretWord.config(bg="#0FCDCA")

		guessDisplay = tk.Entry(listMision[mision], textvariable=blanks, font=("Lucida Calligraphy", 18))
		guessDisplay.place(x=410, y=70)
		guessDisplay.config(width=35, background="black", fg="#07CEF2", justify="center")

		#etiqCorrcLetters = tk.Label(listMision[mision], text="Correct Letters", font=("Lucida Calligraphy", 13))
		#etiqCorrcLetters.place(x=420, y=280)
		#etiqCorrcLetters.config(bg="#944DBD")

		#displCorrcLetters = tk.Entry(listMision[mision], textvariable=correctLettersDsp, font=("Arial", 13))
		#displCorrcLetters.place(x=350, y=310)
		#displCorrcLetters.config(width=35, background="black", fg="yellow", justify="center")

		etiqMissLetters = tk.Label(listMision[mision], text="Missed Letters", font=("Comic Sans MS", 13) )
		etiqMissLetters.place(x=630, y=140)
		etiqMissLetters.config(bg="#0FCDCA")

		displMissLetters = tk.Entry(listMision[mision], textvariable=missedLetters, font=("Arial", 13))
		displMissLetters.place(x=540, y=170)
		displMissLetters.config(width=35, background="black", fg="red", justify="center")

		etiqScore = tk.Label(listMision[mision], text="Score", font=("Lucida Calligraphy", 14))
		etiqScore.place(x=350, y=450)
		etiqScore.config(bg="#0FCDCA")

		displScore = tk.Label(listMision[mision], textvariable=score, font=("Arial", 34))
		displScore.place(x=420, y=450)
		displScore.config(background="black", fg="#07CEF2", justify="center", width=6)

		btMeans = tk.Button(listMision[mision], image=hear, command=lambda:meaningSound())
		btMeans.config(fg="green")
		btMeans.place(x=610, y=230)

		btUse = tk.Button(listMision[mision], image=imnUse, command=lambda:exampleUse())
		btUse.place(x=725, y=230)

		btCoin = tk.Button(listMision[mision], image=coinbatt, command=lambda:explicCoins())
		btCoin.place(x=610, y=330)

		leyendCoin = tk.Label(listMision[mision], bg="white", fg="#FFD700", font=("Comic Sans MS", 10, "bold"))
		leyendCoin.place(x=613, y=387)
		leyendCoin.config(text=goldCoins)

		btGem = tk.Button(listMision[mision], image=gembatt, command=lambda:expplicGems())
		btGem.place(x=725, y=330)

		displGems = tk.Label(listMision[mision], textvariable=lifesAc, font=("Comic Sans MS", 12))
		displGems.place(x=728, y=372)
		displGems.config(bg="white", fg="blue")

		btFinish = tk.Button(listMision[mision], text="Finish riddle", font=("Comic Sans MS", 12), command=lambda:finishMision())
		btFinish.config(fg="blue")
		btFinish.place(x=620, y=510)

		btquitP = tk.Button(listMision[mision], text="Quit game", font=("Comic Sans MS", 12), command=lambda:quitMision())
		btquitP.config(fg="blue")
		btquitP.place(x=780, y=510)

def quitMision():

	conexion2 = sqlite3.connect("players")
	cursor2 = conexion2.cursor()

	sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
	datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

	cursor2.execute(sql4, datsActs)
	conexion2.commit()
	conexion2.close()

	raiz.destroy()



def jim():

	playsound(jimmy)


def explicCoins():

	playsound(explanCoin)

def expplicGems():

	playsound(explanGem)



def finishMision():

	global words
	global idiomMeans
	global indice
	global listMision
	global mision 
	global idiomExamples

	if guessSecWord:

		del idiomMeans[indice]
		del idiomExamples[indice]
		del words[indice]

		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()

		listMision[mision].destroy()

	
		


def exampleUse():

	global exceUse
	global idiomExamples

	if guessSecWord == False:

		playsound(exceUse)

	else:

		playsound(idiomExamples[indice])


def meaningSound():

	global idiomMeans
	global indice

	playsound(idiomMeans[indice])

	

def letraPulsada(letra):
	global blanks
	global secretWord
	global correctLetters
	global correctLettersDsp
	global alreadyLetters
	global score
	global scoreAcumulado
	global wrongs
	global lifes
	global guessSecWord
	global passedMissions
	global runOut
	global ganancia
	global perdida
	global gameOver
	global avisoRunOut
	global goldCoins
	global leyendCoin
	global lifesAc
	global marcoAhorc

	for i in range(len(secretWord)):
		
		if letra in secretWord[i] and correctLetters < len(secretWord) and alreadyLetters.count(letra) < secretWord.count(letra) and wrongs <= 4:
			blanks.set(blanks.get()[:i] + secretWord[i] + blanks.get()[i+1:])
			correctLettersDsp.set(correctLettersDsp.get() + "   " + letra)
			correctLetters = correctLetters + 1
			alreadyLetters = alreadyLetters + letra
			score.set(score.get() + int((100/len(secretWord))))
			scoreAcumulado = scoreAcumulado + int((100/len(secretWord)))
			playsound(ganancia)
			

		
	if letra not in secretWord and correctLetters < len(secretWord) and wrongs <= 4:
		missedLetters.set(missedLetters.get() + "   " + letra)
		score.set(score.get() - 5)
		scoreAcumulado = scoreAcumulado - 5
		wrongs = wrongs + 1
		playsound(perdida)
		

	if correctLetters == len(secretWord):

		score.set(score.get() + 80)
		scoreAcumulado = scoreAcumulado + 80
		guessSecWord = True
		passedMissions = mision
		goldCoins = goldCoins + 1
		playsound(ganarPantalla)

		

		correctLetters = correctLetters + 1

	if wrongs >= 5 and lifes >= 1:

		runOut = True
		lifes = lifes - 1
		lifesAc.set(lifesAc.get() - 1)
		wrongs = 0

		if avisoRunOut == 1:

			avisoRunOut = 0

		#marcoAhorc.config(image=Verd2)

	elif wrongs >= 5 and lifes == 0:

		runOut = True		
		gameOver = True
		lifes = lifes - 1
		lifesAc.set(lifesAc.get() - 1)

		if avisoRunOut == 1:

			avisoRunOut = 0


	#leyendCoin.config(text=goldCoins)



def resetCrLetters():
	global correctLetters
	global alreadyLetters
	global wrongs
	global guessSecWord
	global passedMissions
	global mision
	global avisoGuess
	global words
	global idiomMeans
	global indice

	if passedMissions == mision and nickname.get() != "" and lifes >= 0:

		correctLetters = 0
		alreadyLetters = ""
		wrongs = 0
		guessSecWord = False
		avisoGuess = 0
		

	elif passedMissions < mision and lifes >= 0:

		messagebox.showinfo(parent=raiz, message= "You must guess the current secret idiom first")

	elif nickname.get() == "":

		messagebox.showinfo(parent=raiz, message = "You must activate a player first")

	elif nickname.get() != "" and lifes < 0:

		playsound(playerHasNoGems)



def guessSecretWord():
	
	global guessSecWord
	global avisoGuess
	global gemsGanadas
	global goldCoins
	global lifes
	global lifesAc

	if guessSecWord and avisoGuess == 0:
		messagebox.showinfo(parent = listMision[mision], message = ("Well done!! you have guessed the secret idiom:  " + secretWord), title="Idioms Code")
		

		avisoGuess = 1

		if gemsGanadas < goldCoins//10:

			lifes = lifes + 1
			lifesAc.set((lifesAc.get()) + 1)
			gemsGanadas = gemsGanadas + 1
			playsound(premGem)


def runOutGuess():

	global runOut
	global avisoRunOut
	global marcoAhorc

	if runOut and avisoRunOut == 0 and gameOver == False:
		messagebox.showinfo(parent = listMision[mision], message = "You are run out of guesses. You have actually guessed: " + str(mision) + " idioms.\nTry again.", title="Idioms Code")
		avisoRunOut = 1
		runOut = False
		marcoAhorc.config(image=Verd2)
		playsound(risaJim)
		playsound(gemLostt)

	elif runOut and avisoRunOut == 0 and gameOver:
		
		messagebox.showinfo(parent = listMision[mision], message = "The game is over. You have guessed " + str(mision) + " idioms", title="Idioms Code")
		avisoRunOut = 2
		playsound(risaFin)
		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()
		listMision[mision].destroy()



buttonExample = tk.Button(raiz, 
			  text="Create Riddle", font=("Comic Sans MS", 12), fg="blue", command=lambda:[resetCrLetters(), createNewWindow()])
buttonExample.place(x=620, y=480)

playsound(iniRiddle)

#botonCambImg = tk.Button(raiz, text="cambiar", command=lambda:cambiarImagen())
#botonCambImg.place(x=520, y=480)

raiz.mainloop()