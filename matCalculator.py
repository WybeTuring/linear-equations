# Importing the necessary dependies

import reduction
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.previousButton = None
        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(
            multiline = True, readonly = True, halign = "right", font_size = 30
            )
        main_layout.add_widget(self.solution)
        buttons = [
            ["Clear All", "Backspace"],
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [".", "0", "-"],
            ["Gaussian Reduced Matrix"],
            ["Echelon Form Reduced Matrix"],
            ["Reduced Echelon Form Reduced Matrix"],
            ["Gauss-Jordan Reduced Matrix"]
        ] 
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label,
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        enter_button = Button(
            text = "ENTER", pos_hint = {"center_x": 0.5, "center_y": 0.5}
        )

        main_layout.add_widget(enter_button)

        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "Clear All":
          # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            elif button_text in ["7", "8", "9", "4", "5", "6", "1", "2", "3"] and self.previousButton == "-":
                new_text = current + ("-" + button_text)
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        self.previousButton = instance.text
   
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()