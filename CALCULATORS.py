import flet as ft

def main(page: ft.Page):
    
    def basic_calc(e):
        try:
            a, b = int(num1.value), int(num2.value)
            op = e.control.text
            if op == "+": r = a + b
            elif op == "-": r = a - b
            elif op == "*": r = a * b
            elif op == "/" and b != 0: r = a // b
            else: raise ValueError
            result.value = f"Result: {r}"
        except:
            result.value = "Invalid input"
        page.update()

    num1 = ft.TextField(label="Number 1")
    num2 = ft.TextField(label="Number 2")
    result = ft.Text()
    basic_tab = ft.Column([
        num1, num2,
        ft.Row([ft.ElevatedButton("+", on_click=basic_calc),
                ft.ElevatedButton("-", on_click=basic_calc),
                ft.ElevatedButton("*", on_click=basic_calc),
                ft.ElevatedButton("/", on_click=basic_calc)]),
        result
    ])

    def bmi_calc(e):
        try:
            h = int(height.value) / 100
            w = int(weight.value)
            bmi.value = f"BMI: {int(w / (h * h))}"
        except:
            bmi.value = "Invalid input"
        page.update()

    height = ft.TextField(label="Height (cm)")
    weight = ft.TextField(label="Weight (kg)")
    bmi = ft.Text()
    bmi_tab = ft.Column([height, weight, ft.ElevatedButton("Calculate", on_click=bmi_calc), bmi])

    def convert(e):
        try:
            v = int(val.value)
            f, t = from_u.value, to_u.value
            if f == t: r = v
            elif f == "cm" and t == "inch": r = v // 3
            elif f == "inch" and t == "cm": r = v * 3
            elif f == "kg" and t == "pound": r = v * 2
            elif f == "pound" and t == "kg": r = v // 2
            else: r = "?"
            converted.value = f"Converted: {r if isinstance(r, int) else '?'}"
        except:
            converted.value = "Error"
        page.update()

    val = ft.TextField(label="Value")
    from_u = ft.Dropdown(options=[
        ft.dropdown.Option("cm"),
        ft.dropdown.Option("inch"),
        ft.dropdown.Option("kg"),
        ft.dropdown.Option("pound")
    ], value="cm")
    to_u = ft.Dropdown(options=[
        ft.dropdown.Option("cm"),
        ft.dropdown.Option("inch"),
        ft.dropdown.Option("kg"),
        ft.dropdown.Option("pound")
    ], value="inch")
    converted = ft.Text()
    convert_tab = ft.Column([val, from_u, to_u, ft.ElevatedButton("Convert", on_click=convert), converted])

    page.add(ft.Tabs(tabs=[
        ft.Tab(text="Basic", content=basic_tab),
        ft.Tab(text="BMI", content=bmi_tab),
        ft.Tab(text="Converter", content=convert_tab)
    ]))

ft.app(target=main)
