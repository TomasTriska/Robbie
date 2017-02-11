import logging
import os
from pydub import AudioSegment
from pydub.playback import play
import time

from programy.clients.clients import BotClient

class ConsoleBotClient(BotClient):

    def __init__(self):
        BotClient.__init__(self)
        self.clientid = "Console"
        self.soundBeep = AudioSegment.from_wav("robbie/sounds/Beep.wav")
        self.soundAction = AudioSegment.from_wav("robbie/sounds/Action.wav")
        self.soundFailure = AudioSegment.from_wav("robbie/sounds/Failure.wav")

    def set_environment(self):
        self.bot.brain.predicates.pairs.append(["env", "Console"])

    def run(self):
        if self.arguments.noloop is False:
            logging.info("Entering conversation loop...")
            running = True
            play(self.soundBeep)
            self.display_response(self.bot.get_version_string)
            play(self.soundBeep)
            self.display_response(self.bot.brain.post_process_response(self.bot, self.clientid, self.bot.initial_question))
            while running is True:
                try:
                    question = self.get_question()
                    play(self.soundBeep)
                    response = self.bot.ask_question(self.clientid, question)
                    if response is None:
                        play(self.soundFailure)
                        self.display_response(self.bot.default_response)
                        self.log_unknown_response(question)
                    else:
                        play(self.soundAction)
                        self.display_response(response)
                        self.log_response(question, response)
                except KeyboardInterrupt:
                    running = False
                    play(self.soundFailure)
                    self.display_response(self.bot.exit_response)
                except Exception as excep:
                    logging.exception(excep)
                    logging.error("Oops something bad happened !")

    def get_question(self):
        ask="%s "%"You ➜"
        return input(ask)

    def display_response(self, response):
        print("R🤖bbie ➜ "+response)
        os.system("say '"+response.replace("'","´")+"'")

if __name__ == '__main__':

    def run():
        print("Loading, please wait...")
        console_app = ConsoleBotClient()
        console_app.run()

    run()
