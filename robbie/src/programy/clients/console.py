import logging
import time

from programy.clients.clients import BotClient
from programy.clients.sounds import SoundSystem, Sample, Phrase

class ConsoleBotClient(BotClient):

    def __init__(self):
        BotClient.__init__(self)
        self.clientid = "Console"
        self.sound = SoundSystem()

    def set_environment(self):
        self.bot.brain.predicates.pairs.append(["env", "Console"])

    def run(self):
        if self.arguments.noloop is False:
            logging.info("Entering conversation loop...")
            running = True
            self.__play(Sample('Beep'))
            self.display_response(self.bot.get_version_string)
            self.__play(Sample('Beep'))
            self.display_response(self.bot.brain.post_process_response(self.bot, self.clientid, self.bot.initial_question))
            while running is True:
                try:
                    question = self.get_question()
                    self.__play(Sample('Beep'))
                    response = self.bot.ask_question(self.clientid, question)
                    if response is None:
                        self.__play(Sample('Failure'))
                        self.display_response(self.bot.default_response)
                        self.log_unknown_response(question)
                    else:
                        self.__play(Sample('Action'))
                        self.display_response(response)
                        self.log_response(question, response)
                except KeyboardInterrupt:
                    running = False
                    self.__play(Sample('Failure'))
                    self.display_response(self.bot.exit_response)
                except Exception as excep:
                    logging.exception(excep)
                    logging.error("Oops something bad happened !")

    def get_question(self):
        ask="%s "%"You ➜"
        return input(ask)

    def display_response(self, response):
        print("R🤖bbie ➜ "+response)
        self.__play(Phrase(response))

    def __play(self, what):
        if not self.arguments.mute:
            self.sound.send(what)



if __name__ == '__main__':

    def run():
        print("Loading, please wait...")
        console_app = ConsoleBotClient()
        console_app.run()

    run()
