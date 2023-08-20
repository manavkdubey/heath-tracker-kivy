from kivy.uix.button import Button

class CustomActionButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Customize the appearance of the button
        self.background_color = (0.2, 0.6, 0.2, 1)  # Green background color
        self.color = (1, 1, 1, 1)  # White text color
        self.size_hint = (None, None)
        self.size = (150, 50)
