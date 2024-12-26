import random
import pygame
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock

# SuperNES Emulator Logic
class SuperNES:
    def __init__(self):
        self.screen = None
        self.running = True
        self.glitch_intensity = 0.5  # Adjust for the "glitch" effect (0 to 1)

    def emulate_frame(self):
        # Render the frame (basic placeholder functionality)
        self.screen.fill((0, 0, 0))
        for _ in range(int(self.glitch_intensity * 50)):
            x = random.randint(0, 255)
            y = random.randint(0, 239)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.rect(self.screen, color, (x, y, 8, 8))

class SuperNESApp(App):
    def build(self):
        self.supernes = SuperNES()
        self.grid = GridLayout(cols=1)
        
        # Emulator UI components
        self.label = Label(text="SuperNES Emulator", font_size=32)
        self.grid.add_widget(self.label)

        self.start_button = Button(text="Start Emulator")
        self.start_button.bind(on_press=self.start_emulator)
        self.grid.add_widget(self.start_button)

        self.quit_button = Button(text="Quit")
        self.quit_button.bind(on_press=self.quit_emulator)
        self.grid.add_widget(self.quit_button)

        # Initialize pygame for the emulator frame
        pygame.init()
        self.supernes.screen = pygame.display.set_mode((256, 240))

        # Create a Clock object to emulate frame rate
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # 60 FPS

        return self.grid

    def start_emulator(self, instance):
        self.label.text = "Emulator Running..."

    def quit_emulator(self, instance):
        self.stop()

    def update(self, dt):
        if self.supernes.running:
            self.supernes.emulate_frame()
        pygame.display.flip()

if __name__ == "__main__":
    SuperNESApp().run()
