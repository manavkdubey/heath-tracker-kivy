from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from database import db

class HabitEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a main layout for the habit entry screen
        main_layout = BoxLayout(orientation='vertical')

        # Add a title label
        title_label = Label(text="Add New Habit", size_hint=(1, 0.1))
        main_layout.add_widget(title_label)

        # Add text input for habit name
        self.habit_name_input = TextInput(hint_text="Enter Habit Name", size_hint=(1, 0.1))
        main_layout.add_widget(self.habit_name_input)

        # Add text input for habit description
        self.habit_description_input = TextInput(hint_text="Enter Habit Description", size_hint=(1, 0.1))
        main_layout.add_widget(self.habit_description_input)

        # Add a button to save the new habit
        save_button = Button(text="Save Habit", size_hint=(1, 0.1))
        save_button.bind(on_release=self.save_habit)
        main_layout.add_widget(save_button)

        self.add_widget(main_layout)

    def save_habit(self, instance):
        # Retrieve habit name and description from text inputs
        habit_name = self.habit_name_input.text
        habit_description = self.habit_description_input.text

        # Add the habit to the database
        db.add_habit(name=habit_name, description=habit_description)

        # Clear text inputs after saving
        self.habit_name_input.text = ""
        self.habit_description_input.text = ""
         # Update the home screen to display the new habit
        home_screen = self.manager.get_screen('home')
        home_screen.update_habits()

        # Optionally, navigate back to the home screen
        self.manager.current = 'home'

  