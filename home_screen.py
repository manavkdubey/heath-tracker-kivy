from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from database import HabitDatabase

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a main layout for the home screen
        main_layout = BoxLayout(orientation='vertical')

        # Add a title label
        title_label = Label(text="Habit Tracker App", size_hint=(1, 0.1))
        main_layout.add_widget(title_label)

        # Display habits
        habits_label = Label(text="Your Habits:", size_hint=(1, 0.1))
        main_layout.add_widget(habits_label)

        # Get habits from the database and display them
        habits = db.get_habits()

          # Add a button to clear all habits
        clear_button = Button(text="Clear All Habits", size_hint=(1, 0.1))
        clear_button.bind(on_release=self.clear_all_habits)
        main_layout.add_widget(clear_button)

    

        # Add a button to go to the habit entry screen
        habit_entry_button = Button(text="Add New Habit", size_hint=(1, 0.1))
        habit_entry_button.bind(on_release=self.go_to_habit_entry)
        main_layout.add_widget(habit_entry_button)

        self.add_widget(main_layout)

        # Store a reference to the habits label for updating
        self.habits_label = habits_label

    def update_habits(self):
        # Clear the existing habits displayed
        self.habits_label.text = "Your Habits:\n"

        # Get habits from the database and display them
        habits = db.get_habits()

        for habit in habits:
            self.habits_label.text += habit[1] + "\n"

    def go_to_habit_entry(self, instance):
        self.manager.current = 'habit_entry'

    
    def clear_all_habits(self, instance):
        # Clear all habits from the database
        db.clear_all_habits()

        # Update the displayed habits
        self.update_habits()

db = HabitDatabase()  # Instantiate the HabitDatabase class
