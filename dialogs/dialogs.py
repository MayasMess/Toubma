from dialogbox.dialogbox import Dialogbox


class Dialogs(Dialogbox):
    def __init__(self, screen):
        super().__init__(screen)
        self.dialog_init_up = False
        self.dialog_init_down = False
        self._dialog_count = 0
        self.is_first_call = True
        self.start_dialog = False
        self.is_first_step = False

    @property
    def dialog_count(self):
        return self._dialog_count

    @dialog_count.setter
    def dialog_count(self, dialog_count):
        if self.start_dialog is True:
            self._dialog_count = dialog_count

    def step(self, step, text, position):
        if self.dialog_count == step and self.is_first_step is True:
            self.is_first_step = False
            self.update_dialogue(text=text, position=position)

    def init_step(self, step, text, position, identity_path):
        if position == 'up':
            if self.dialog_count == step or self.dialog_init_up is True:
                self.appear(identity_path=identity_path, position=position)
                if self.dialog_init_up is False:
                    self.update_dialogue(text=text, position=position)
                self.dialog_init_up = True
        else:
            if self.dialog_count == step or self.dialog_init_down is True:
                self.appear(identity_path=identity_path, position=position)
                if self.dialog_init_down is False:
                    self.update_dialogue(text=text, position=position)
                self.dialog_init_down = True

    def final_step(self, step, list_identity_path, number_of_boxes=1):
        if self.dialog_count == step:
            self.dialog_init_up = False
            self.appear(identity_path=list_identity_path[0], position='up', disappear=True)
            self.is_first_call = True
            self.start_dialog = False
            if number_of_boxes == 2:
                self.dialog_init_down = False
                self.appear(identity_path=list_identity_path[1], position='down', disappear=True)

    def go_to_next_step(self):
        self.dialog_count += 1
        self.is_first_step = True

    def init_dialog(self):
        if self.is_first_call is True:
            self.is_first_call = False
            self.dialog_count += 1

    def finish_dialog(self, step):
        if self.dialog_count >= step:
            self.dialog_count = 0

    def test_dialog(self):
        # Init the first call
        self.init_dialog()
        # All steps of the dialog
        self.init_step(step=1, text='Saha les hommes', position='up', identity_path='dialogs/assets/test.jpg')
        self.init_step(step=2, text='Amek ayachrik', position='down', identity_path='dialogs/assets/test2.jpg')
        self.step(step=3, text='Dayen foukagh el code ni !', position='up')
        self.step(step=4, text='Ahh kifkif ! Bon courage fréére', position='down')
        self.step(step=5, text='thanks bro', position='up')
        self.final_step(step=6, list_identity_path=['dialogs/assets/test.jpg', 'dialogs/assets/test2.jpg'],
                        number_of_boxes=2)
        # Finish dialog and go back to zero
        self.finish_dialog(step=7)
