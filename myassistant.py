import pyttsx3
import os

pyttsx3.speak("Hi user")

while True:
	pyttsx3.speak("Which App do you want to use")
	print("Write your requirements :", end=' ')
	s = input()
	
	if (("run" in s) or ("open" in s) or ("execute" in s)) and (("notepad" in s) or ("note" in s) or ("text editor" in s)):
	  pyttsx3.speak("Opening notepad")
	  os.system("notepad")

	
	elif (("run" in s) or ("open" in s) or ("execute" in s)) and (("chrome" in s) or ("browser" in s) or ("google" in s)):
	  pyttsx3.speak("Opening google chrome")
	  os.system("chrome")

	elif (("run" in s) or ("open" in s) or ("execute" in s)) and (("skype business" in s) or ("skype for business" in s) or ("skype meeting" in s)):
	  pyttsx3.speak("Opening skype for business")
	  os.system("lync")

	elif (("run" in s) or ("open" in s) or ("execute" in s)) and (("vlc" in s) or ("vlc media player" in s)):
	  pyttsx3.speak("Opening vlc ")
	  os.system("vlc")

	elif (("run" in s) or ("open" in s) or ("execute" in s)) and ("zoom" in s):
	  pyttsx3.speak("Opening zoom")
	  os.system("zoom")

	elif (("run" in s) or ("open" in s)) and (("oracle" in s) or ("virtual box" in s)):
	  pyttsx3.speak("Opening Oracle Virtual box")
	  os.system("virtualbox")

	
	elif ("exit" in s) or ("close" in s) or ("stop" in s) or ("bye" in s):
	  pyttsx3.speak("Bye, catch you later")
	  break

	else :
	  pyttsx3.speak("Please check your command")
	  print("Doesn't support")  