import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import pyjokes
import wikipedia  #need packages

def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	#  Microphone module
	with sr.Microphone() as source:
		print('Listening...')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing...")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("Shri your command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again shri")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is shri" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello shri I am your desktop assistant. how may I help you")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()

	while(True):

		query = takeCommand().lower()
		if "open google" in query:
			speak("Opening Google ")
			
			webbrowser.open("www.google.com")
			continue

		elif "hadoop" in query:
			speak("Opening hadoop.com")
			webbrowser.open("https://hadoop.apache.org/")
			continue

        
		elif "open notes" in query:
			speak("Opening detail notes on Google drive ")
			webbrowser.open("https://drive.google.com/drive/u/0/folders/1F6sx3liwPGYBuv5izg0bf28EPR8h6BTG")
			continue
        
                
		elif "open ppt" in query:
			speak("Opening ppt on Google drive ")
			webbrowser.open("https://drive.google.com/drive/u/0/folders/1MpoFrttEY4WQbSzilrngwE7pNO5ARjfx")
			continue

		elif "what is mean by big data" in query:
			speak("Here the trainers content ")
			webbrowser.open("https://docs.google.com/presentation/d/1OArA9bcYo9WHtd3A2Bz4Xjiuu9iD0cI8/edit#slide=id.p1")

			speak("did you need more content refer here ")
			webbrowser.open("https://www.ibm.com/analytics/big-data-analytics#:~:text=What%20is%20big%20data%20exactly,high%20velocity%20and%20high%20variety.")
			continue


  
		elif "play song" in query:
			song = query.replace('play','')
			speak('playing'+song)
			pywhatkit.playonyt(song)
			continue

		elif "play some tamil song" in query:
			song = query.replace('play','')
			speak('playing'+song)
			pywhatkit.playonyt(song)
			continue
        
		elif "joke" in query:
			speak(pyjokes.get_joke())
			continue
  

		elif "tell me the time" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye. Check Out me for more exciting things")
			exit()
		
		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
        
		
		elif "tell me your name" in query:
			speak("I am Shri. Your desktop Assistant")
   
        
            

if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()
