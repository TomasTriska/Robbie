import os
from pydub import AudioSegment
from pydub.playback import play


class SoundSystem(object):
	"Systém pro pouštění zvuků a přehrávání textu."

	def __init__(self):
		self.samples = {
			'Beep': AudioSegment.from_wav("robbie/sounds/Beep.wav"),
			'Action': AudioSegment.from_wav("robbie/sounds/Action.wav"),
			'Failure': AudioSegment.from_wav("robbie/sounds/Failure.wav")
		}

	def send(self, what):
		if isinstance(what, Phrase):
			self._play_phrase(what.content)
		elif isinstance(what, Sample):
			self._play_sample(what.name)
		else:
			print(what)

	def _play_phrase(self, content):
		if os.name == 'mac':
			os.system("say '" + what.content.replace("'","´") + "'")
		else:
			pass # mute @TODO Implementation own solving for other platform.

	def _play_sample(self, name):
		play(self.samples[name])


class Sample(object):
	"Reprezentuje nějakou existující pojmenovanou nahrávku."

	def __init__(self, name):
		self.name = name



class Phrase(object):
	"Reprezentuje frázi, kterou se pokoušíme přečíst."

	def __init__(self, content):
		self.content = content
