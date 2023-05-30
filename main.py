from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle


Builder.load_string("""
<CoffeeShop>:
    orientation: 'vertical'
    spacing: dp(20)
    padding: dp(20)
    BoxLayout:
        size_hint: 1, 0.5
        Image:
            source: "C:/Users/Acer/Documents/Louie_BSIT_2nd_year/kivy_env/1.png"
            size_hint: 0.5, 1
            pos_hint: {'center_x': 0.5}
        Image:
            source: "C:/Users/Acer/Documents/Louie_BSIT_2nd_year/kivy_env/5.png"
            size_hint: 0.7, 1
            pos_hint: {'center_x': 0.5}
    BoxLayout:
        size_hint: 1, 0.5
        orientation: 'vertical'
        spacing: dp(20)
        BoxLayout:
            size_hint: 1, 0.33
            orientation: 'horizontal'
            Image:
                source: 'C:/Users/Acer/Documents/Louie_BSIT_2nd_year/kivy_env/2.png'
                size_hint: 0.45, 1
            Label:
                text: 'Americano'
                font_size: sp(24)
                bold: True
                halign: 'left'
                valign: 'middle'
                size_hint: 0.33, 1
            TextInput:
                id: americano_qty
                text: '0'
                input_type: 'number'
                size_hint: 0.33, 1
            Spinner:
                id: americano_spinner
                text: 'Size'
                values: ['Small', 'Large']
                size_hint: 0.33, 1
        BoxLayout:
            size_hint: 1, 0.33
            orientation: 'horizontal'
            Image:
                source: 'C:/Users/Acer/Documents/Louie_BSIT_2nd_year/kivy_env/3.png'
                size_hint: 0.45, 1
            Label:
                text: 'Cappuccino'
                font_size: sp(24)
                bold: True
                halign: 'left'
                valign: 'middle'
                size_hint: 0.33, 1
            TextInput:
                id: cappuccino_qty
                text: '0'
                input_type: 'number'
                size_hint: 0.33, 1
            Spinner:
                id: cappuccino_spinner
                text: 'Size'
                values: ['Small', 'Large']
                size_hint: 0.33, 1
        BoxLayout:
            size_hint: 1, 0.33
            orientation: 'horizontal'
            Image:
                source: 'C:/Users/Acer/Documents/Louie_BSIT_2nd_year/kivy_env/4.png'
                size_hint: 0.45, 1
            Label:
                text: 'Latte'
                font_size: sp(24)
                bold: True
                halign: 'left'
                valign: 'middle'
                size_hint: 0.33, 1
            TextInput:
                id: latte_qty
                text: '0'
                input_type: 'number'
                size_hint: 0.33, 1
            Spinner:
                id: latte_spinner
                text: 'Size'
                values: ['Small', 'Large']
                size_hint: 0.33, 1
        Button:
            text: 'Compute Total'
            font_size: sp(24)
            bold: True
            size_hint: 1, 0.33
            on_press: root.compute_total()
        
       
        BoxLayout:
            size_hint: 1, 0.33
            orientation: 'horizontal'
            
            Label:
                id: total_label
                text: 'Total: P0.00'
                font_size: sp(36)
                bold: True
                halign: 'center'
                valign: 'middle' """)

class CoffeeShop(BoxLayout):
    def compute_total(self):
        americano_price = 80.00 if self.ids.americano_spinner.text == 'Small' else 120.00
        americano_qty = int(self.ids.americano_qty.text) if self.ids.americano_qty.text else 0
        americano_cost = americano_qty * americano_price

        cappuccino_price = 90.00 if self.ids.cappuccino_spinner.text == 'Small' else 140.00
        cappuccino_qty = int(self.ids.cappuccino_qty.text) if self.ids.cappuccino_qty.text else 0
        cappuccino_cost = cappuccino_qty * cappuccino_price

        latte_price = 100.00 if self.ids.latte_spinner.text == 'Small' else 160.00
        latte_qty = int(self.ids.latte_qty.text) if self.ids.latte_qty.text else 0
        latte_cost = latte_qty * latte_price

        total = americano_cost + cappuccino_cost + latte_cost
        self.ids.total_label.text = f'Total: P{total:.2f}'
    def __init__(self, **kwargs):
        super(CoffeeShop, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.55, 0.27, 0.07, 1.0) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class CoffeeShopApp(App):
    def build(self):
        return CoffeeShop()

if __name__ == '__main__':
    CoffeeShopApp().run()
