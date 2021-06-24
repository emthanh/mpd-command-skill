from mycroft import MycroftSkill, intent_file_handler


class MpdCommand(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('command.mpd.intent')
    def handle_command_mpd(self, message):
        self.speak_dialog('command.mpd')


def create_skill():
    return MpdCommand()

