# Belajar Default Argument Value

def say_hello(first_name="Bening", last_name="Saraswati"):
    print(f"Hello {first_name} {last_name}")

say_hello("Priyo", "Setio")
say_hello()
say_hello(last_name="setio", first_name="priyo")