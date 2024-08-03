from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class ToDoApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.tasks = None
        self.task_input = None

    def build(self):
        self.tasks = []

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input area
        input_layout = BoxLayout(size_hint_y=None, height=40)
        self.task_input = TextInput(multiline=False)
        add_button = Button(text="Add Task", on_press=self.add_task, size_hint_x=None, width=100)
        input_layout.add_widget(self.task_input)
        input_layout.add_widget(add_button)

        # Task list area
        self.task_list = BoxLayout(orientation='vertical', spacing=5)
        scroll_view = ScrollView()
        scroll_view.add_widget(self.task_list)

        # Add widgets to main layout
        layout.add_widget(input_layout)
        layout.add_widget(scroll_view)

        return layout

    def add_task(self, instance):
        task = self.task_input.text.strip()
        if task:
            task_layout = BoxLayout(size_hint_y=None, height=40)
            task_label = Label(text=task, size_hint_x=0.7)
            complete_button = Button(text="Complete", size_hint_x=0.15, on_press=self.complete_task)
            remove_button = Button(text="Remove", size_hint_x=0.15, on_press=self.remove_task)

            task_layout.add_widget(task_label)
            task_layout.add_widget(complete_button)
            task_layout.add_widget(remove_button)

            self.task_list.add_widget(task_layout)
            self.tasks.append(task_layout)
            self.task_input.text = ""

    def complete_task(self, instance):
        task_layout = instance.parent
        task_label = task_layout.children[2]  # The label is the third child (index 2)
        if task_label.color == [1, 1, 1, 1]:  # If not completed
            task_label.color = [0, 1, 0, 1]  # Green color for completed tasks
        else:
            task_label.color = [1, 1, 1, 1]  # White color for uncompleted tasks

    def remove_task(self, instance):
        task_layout = instance.parent
        self.task_list.remove_widget(task_layout)
        self.tasks.remove(task_layout)


if __name__ == '__main__':
    ToDoApp().run()