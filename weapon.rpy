init python:
    class Weapon(renpy.Displayable):
        def __init__(self, static_displayable, shooting_displayables, reloading_displayables, shooting_state=False, reloading_state=False, shooting_sfx=None, reloading_sfx=None):
            super(Weapon, self).__init__()
            
            self.static_displayable = static_displayable
            self.shooting_displayables = shooting_displayables
            self.reloading_displayables = reloading_displayables

            self.mousex_coordinate = None
            
            self.shooting = shooting_state
            self.reloading = reloading_state

            self.shooting_sfx = shooting_sfx
            self.reloading_sfx = reloading_sfx

            self.shooting_frame = 0
            self.reloading_frame = 0
            self.time_between_frames = 0.2

            self.shooting_start = None
            self.reloading_start = None
        
        def render(self, width, height, st, at):
            render_viewport = renpy.Render(width, height)

            if self.mousex_coordinate is not None:
                current_displayable_sprite = self.static_displayable
                if self.shooting:
                    self.shooting_frame = int((st - self.shooting_start) / self.time_between_frames)
                    if self.shooting_frame >= len(self.shooting_displayables):
                        self.shooting_frame = 0
                        self.shooting = False
                    else:
                        current_displayable_sprite = self.shooting_displayables[self.shooting_frame]
                elif self.reloading:
                    self.reloading_frame = int((st - self.reloading_start) / self.time_between_frames)
                    if self.reloading_frame >= len(self.reloading_displayables):
                        self.reloading_frame = 0
                        self.reloading = False
                    else:
                        current_displayable_sprite = self.reloading_displayables[self.reloading_frame]

                transform = Transform(current_displayable_sprite, zoom=0.75)

                child_render = renpy.render(transform, width, height, st, at)
                
                child_width, child_height = child_render.get_size()

                x_position = self.mousex_coordinate - child_width / 2
                y_position = renpy.config.screen_height - child_height
                padding = 400

                is_mouse_in_screen = x_position + child_width >= renpy.config.screen_width + padding

                if is_mouse_in_screen:
                    x_position = renpy.config.screen_width - child_width + padding
                
                render_viewport.blit(child_render, (x_position, y_position))
                renpy.redraw(self, self.time_between_frames)

            return render_viewport
        
        def event(self, event, x, y, st):
            if x != self.mousex_coordinate:
                self.mousex_coordinate = x
                renpy.redraw(self, 0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.reloading:
                self.shooting = True
                self.shooting_start = st
                renpy.sound.play([self.shooting_sfx], relative_volume=0.15, channel="audio")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not self.reloading:
                self.reloading = True
                self.reloading_start = st
                renpy.sound.play([self.reloading_sfx], relative_volume=0.15, channel="audio")

