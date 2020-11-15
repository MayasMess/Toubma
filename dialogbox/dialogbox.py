import time

import pygame


class Dialogbox:
    box_up = pygame.image.load('dialogbox/assets/dialogbox.jpg').convert()
    box_down = pygame.transform.flip(pygame.image.load('dialogbox/assets/dialogbox.jpg').convert(), True, False)

    def __init__(self, screen):
        self.screen = screen
        self.dialbox_pos_x_up = 84
        self.dialbox_pos_y_up = 50
        self.dialbox_pos_x_down = 84
        self.dialbox_pos_y_down = 300
        self.box_heigth_up = 0
        self.box_heigth_down = 0
        self.base_box_height = self.box_up.get_height()
        self.identity_image_up = None
        self.identity_image_down = None
        self.identity_pos_up = (20, 20)
        self.identity_pos_down = (self.box_down.get_width()-20-57, self.box_down.get_height()-20-60)
        self.is_image_loaded_up = False
        self.is_image_loaded_down = False
        self.font = pygame.font.SysFont('courier new', 18)
        self.text_up = ''
        self.text_down = ''
        self._display_text_up = ''
        self._display_text_down = ''
        self.clear_text_up = False
        self.clear_text_down = False
        self.text_position_up = (175, 90)
        self.text_position_down = (175, 340)

    def update_dialogue(self, text, append=False, position='up'):
        if not append:
            if position == 'up':
                self._display_text_up = ''
                self.clear_text_up = True
            else:
                self._display_text_down = ''
                self.clear_text_down = False
        if position == 'up':
            self.text_up = text
        else:
            self.text_down = text

    def _display_text(self, text_pos, position):
        if position == 'up':
            if self.text_up != '':
                self._display_text_up = self._display_text_up + self.text_up[0]
                self.text_up = self.text_up[1:]
            render_text = self.font.render(self._display_text_up, True, (0, 0, 0))
            self.screen.blit(render_text, text_pos)
        else:
            if self.text_down != '':
                self._display_text_down = self._display_text_down + self.text_down[0]
                self.text_down = self.text_down[1:]
            render_text = self.font.render(self._display_text_down, True, (0, 0, 0))
            self.screen.blit(render_text, text_pos)

    def set_loaded_true(self, position, identity_image):
        if position == 'up':
            self.is_image_loaded_up = True
            self.identity_image_up = identity_image
        else:
            self.is_image_loaded_down = True
            self.identity_image_down = identity_image

    def blit_img(self, box, position):
        if position == 'up':
            box.blit(self.identity_image_up, self.identity_pos_up)
        else:
            box.blit(self.identity_image_down, self.identity_pos_down)

    def update_clear_text(self, position):
        if position == 'up':
            self.clear_text_up = False
        else:
            self.clear_text_down = False

    def appear(self, identity_path=None, disappear=False, position='up'):
        if position == 'up':
            box = self.box_up
            pos_x = self.dialbox_pos_x_up
            pos_y = self.dialbox_pos_y_up
            text_pos = self.text_position_up
            is_loaded = self.is_image_loaded_up
            idt_img = self.identity_image_up
            idt_img_pos = self.identity_pos_up
            box_h = self.box_heigth_up
            clear_text = self.clear_text_up
        else:
            box = self.box_down
            pos_x = self.dialbox_pos_x_down
            pos_y = self.dialbox_pos_y_down
            text_pos = self.text_position_down
            is_loaded = self.is_image_loaded_down
            idt_img = self.identity_image_down
            idt_img_pos = self.identity_pos_down
            box_h = self.box_heigth_down
            clear_text = self.clear_text_down

        if clear_text:
            box.blit(idt_img, idt_img_pos)
            self.screen.blit(box, (pos_x, pos_y))
            self.update_clear_text(position=position)
        else:
            new_box = pygame.transform.scale(box, (box.get_width(), box_h))
            if disappear:
                box_h -= 5
                if box_h < 0:
                    box_h = 0
                    if position == 'up':
                        self._display_text_up = ''
                    else:
                        self._display_text_down = ''
            else:
                box_h += 5
            self.screen.blit(new_box, (pos_x, pos_y))
            if box_h > self.base_box_height:
                box_h = self.base_box_height
                self._display_text(text_pos=text_pos, position=position)
            if identity_path:
                if not is_loaded:
                    identity_image = pygame.image.load(identity_path).convert()
                    self.set_loaded_true(position=position, identity_image=identity_image)
                self.blit_img(box=box, position=position)
            if position == 'up':
                self.box_heigth_up = box_h
            else:
                self.box_heigth_down = box_h
