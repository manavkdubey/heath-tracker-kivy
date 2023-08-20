from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from home_screen import HomeScreen  # Import the HomeScreen class
from habit_entry_screen import HabitEntryScreen  # Import the HabitEntryScreen class

class MyApp(App):
    def build(self):
        # Create a ScreenManager to manage different screens
        screen_manager = ScreenManager()

        # Add screens to the ScreenManager
        home_screen = HomeScreen(name='home')
        habit_entry_screen = HabitEntryScreen(name='habit_entry')

        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(habit_entry_screen)

        return screen_manager

if __name__ == '__main__':
    MyApp().run()
