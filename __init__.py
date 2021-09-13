import subprocess
from mycroft import MycroftSkill, intent_handler


class MpdCommand(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('play.mpd.intent')
    def handle_play_mpd(self, message):
        self.speak_dialog('play.mpd')
        text = subprocess.Popen(('mpc', 'play'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = text.communicate()

    @intent_handler('stop.mpd.intent')
    def handle_play_mpd(self, message):
        self.speak_dialog('stop.mpd')
        text = subprocess.Popen(('mpc', 'stop'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = text.communicate()

    @intent_handler('info.mpd.intent')
    def handle_info_mpd(self, message):
        self.speak_dialog('info.mpd')

        text = subprocess.Popen(('mpc', 'current'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = text.communicate()
        self.speak(output)



def create_skill():
    return MpdCommand()

