import os
from pydub import AudioSegment
from pydub.playback import play
from .system import System


class SoundSystem(object):
	"Sound system for Robbie framework"

	def __init__(self):
            self.__samples = {
                'StartUp': AudioSegment.from_wav("robbie/sounds/StartUp.wav"),
                'Beep': AudioSegment.from_wav("robbie/sounds/Beep.wav"),
		'Action': AudioSegment.from_wav("robbie/sounds/Action.wav"),
		'Failure': AudioSegment.from_wav("robbie/sounds/Failure.wav"),
                'TurnOff': AudioSegment.from_wav("robbie/sounds/TurnOff.wav")
		}
            self.system=System()

	def send(self, what):
		if isinstance(what, Phrase):
			self.__play_phrase(what.content)
		elif isinstance(what, Sample):
			self.__play_sample(what.name)
		else:
			print(what)

	def __play_phrase(self, content):
		if self.system.get_os() == 'MacOS':
                    os.system("say '" + content.replace("'","´") + "'")
		else:
                    pass # mute @TODO Implementation own solving for other platform.

	def __play_sample(self, name):
		play(self.__samples[name])


class Sample(object):
	"Represents some existing and named record."

	def __init__(self, name):
		self.name = name



class Phrase(object):
	"Represents phrase for loading."

	def __init__(self, content):
		self.content = content
