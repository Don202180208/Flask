import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CoffeeKiosk(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        # Create labels for each product
        label1 = Label(text='Americano Barrako - Small: $2.50, Large: $3.50')
        label2 = Label(text='Cappuccino Great Taste - Small: $3.00, Large: $4.00')
        label3 = Label(text='Latte 3 in 1 - Small: $3.50, Large: $4.50')

        # Create text inputs for ordering
        input1 = TextInput(multiline=False, hint_text='Enter quantity for Americano Barrako')
        input2 = TextInput(multiline=False, hint_text='Enter quantity for Cappuccino Great Taste')
        input3 = TextInput(multiline=False, hint_text='Enter quantity for Latte 3 in 1')

        # Create buttons to compute the total
        button = Button(text='Compute Total')
        button.bind(on_press=self.calculate_total)

        # Create label to display the total
        self.total_label = Label(text='Total: $0.00')

        # Add widgets to the layout
        layout.add_widget(label1)
        layout.add_widget(input1)
        layout.add_widget(label2)
        layout.add_widget(input2)
        layout.add_widget(label3)
        layout.add_widget(input3)
        layout.add_widget(button)
        layout.add_widget(self.total_label)

        return layout

    def calculate_total(self, instance):
        # Get the quantity and size for each product
        quantity1 = int(self.root.children[0].text)
        quantity2 = int(self.root.children[2].text)
        quantity3 = int(self.root.children[4].text)

        size1 = 'Small' if self.root.children[1].text.lower() == 'small' else 'Large'
        size2 = 'Small' if self.root.children[3].text.lower() == 'small' else 'Large'
        size3 = 'Small' if self.root.children[5].text.lower() == 'small' else 'Large'

        # Compute the total cost
        total_cost = (quantity1 * (2.50 if size1 == 'Small' else 3.50)) + \
                     (quantity2 * (3.00 if size2 == 'Small' else 4.00)) + \
                     (quantity3 * (3.50 if size3 == 'Small' else 4.50))

        # Update the total label
        self.total_label.text = f'Total: ${total_cost:.2f}'

if __name__ == '__main__':
    CoffeeKiosk().run()
