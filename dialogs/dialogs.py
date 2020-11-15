from dialogbox.dialogbox import Dialogbox


class Dialogs(Dialogbox):
    def __init__(self, screen):
        super().__init__(screen)
        self.dialog_init_up = False
        self.dialog_init_down = False
        self._dialog_count = 0
        self.is_first_call = True
        self.start_dialog = False

    @property
    def dialog_count(self):
        return self._dialog_count

    @dialog_count.setter
    def dialog_count(self, dialog_count):
        if self.start_dialog is True:
            self._dialog_count = dialog_count

    def test_dialog(self):
        if self.is_first_call is True:
            self.is_first_call = False
            self.dialog_count += 1
        if self.dialog_count == 1 or self.dialog_init_up is True:
            self.appear(identity_path='dialogs/assets/test.jpg', position='up')
            if self.dialog_init_up is False:
                self.update_dialogue(text='Saha les hommes', position='up')
            self.dialog_init_up = True
        if self.dialog_count == 2 or self.dialog_init_down is True:
            self.appear(identity_path='dialogs/assets/test2.jpg', position='down')
            if self.dialog_init_down is False:
                self.update_dialogue(text='Amek ayachrik', position='down')
            self.dialog_init_down = True
        if self.dialog_count == 3:
            self.update_dialogue(text='Dayen a3yigh yel code', position='up')
        if self.dialog_count == 4:
            self.update_dialogue(text='Ahh kifki ! Bon courage fréére', position='down')
        if self.dialog_count == 5:
            self.update_dialogue(text='thanks bro', position='up')
        if self.dialog_count == 6:
            self.dialog_init_up = False
            self.dialog_init_down = False
            self.appear(identity_path='dialogs/assets/test.jpg', position='up', disappear=True)
            self.appear(identity_path='dialogs/assets/test2.jpg', position='down', disappear=True)
            self.is_first_call = True
            self.dialog_count = 0
            self.start_dialog = False
