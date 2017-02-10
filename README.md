# Robbie

> Robbie is Artificial Inteligence [IoT] framework for all purposes. Is written in [Python] and uses [Alicebot AIML 2.0]. Robbie needs no screens. Just type or say commands like to normal people. Robbie do command, tell you something or do another action depending on his installed modules for sensors and devices. Developers can write own modules and enhance Robbie. Possibilities are endless. From home assistant (primary use), car assistants, airplanes assistants, interactive robots to clever space ships like in Star Trek in future :)

## Features
  - Open Source
  - Based on [Alicebot AIML 2.0]
  - Robbie understand your sentences and reacts (Just tell him "Prepare some coffee for me", or "How many people live on Earth"...)
  - Text to speech
  - Running on all [UNIX] devices include [MacOS]
  - Primary used for [Intel Edison], but can run on another home server
  - Prepared for [IoT] manufacturers (just connect your sensors and devices using Robbie's methods)
  
## To-do
- Support for [Answers.com], [Wolfram Alpha], [Wikipedia] and other services
- Using of another bots in network (your home Robbie instance can ask for closing of doors in your company for example)
- Voice recognization
- Support for sensors and devices using [Intel Edison]
- Support for sensors and devices using protocols
- Web console support
- Libraries for main programming languages (one can use communicate with Robbie using mobile phone microphone and text input for example + Robbie can show informations on display and use mobile phone speaker)
- [Python] GUI for desktop platforms using libraries
- User profiles with users swithching ("Hello, here is Thomas. Can you do some notes for me?", "Hi Thomas, what do you want to note?")

## Dependencies
- [Python 3]
- [pyyaml]
- [python-dateutil]
- [requests]

## Installation
### MacOS
- Install [Python 3] first
and then:
```sh
$ pip3 install pyaml
$ pip3 install python-dateutil
$ pip3 install requests
```

## Running
- CD to Robbie folder in terminal 
and then:
```sh
$ sh start.sh
```

>You can set automatic lauching of this script on restart as well.

## Stopping
- Hit CTRL+C in terminal

>Do not close Robbie. He can not respond on you and can not learn when is closed. Let him live on old PC or own [Intel Edison] board for example.

## Help us
Want to help us with this amazing project? [Contact us](mailto:tomas.triska@icloud.com). We like investors as well.

## License
Robbie is build upon [program-y] AIML project and [GNU LGPL v3.0] license is used.

   [Internet of Things]: <https://en.wikipedia.org/wiki/Internet_of_things>
   [IoT]: <https://en.wikipedia.org/wiki/Internet_of_things>
   [Python]: <https://www.python.org>
   [Python 3]: <https://www.python.org/download/releases/3.0/>
   [Unix]: <https://en.wikipedia.org/wiki/Unix>
   [MacOS]: <https://cs.wikipedia.org/wiki/Mac_OS>
   [Intel Edison]: <https://software.intel.com/en-us/iot/hardware/edison>
   [Wolfram Alpha]: <https://www.wolframalpha.com>
   [Wikipedia]: <https://www.wikipedia.org>
   [pyyaml]: <http://pyyaml.org>
   [python-dateutil]: <https://dateutil.readthedocs.io/en/stable/>
   [requests]: <http://docs.python-requests.org/en/master/>
   [program-y]: <https://github.com/keiffster/program-y>
   [GNU LGPL v3.0]: <https://www.gnu.org/licenses/lgpl-3.0.en.html>
   [Alicebot AIML 2.0]: <https://docs.google.com/document/d/1wNT25hJRyupcG51aO89UcQEiG-HkXRXusukADpFnDs4/pub>
   [Answers.com]: <http://www.answers.com>
