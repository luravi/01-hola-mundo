def on_forever():
    # Mostrar texto en la pantalla LED
    basic.show_string("Hola Mundo!")

    # Mostrar un mensaje en la consola
    serial.write_line("Este texto aparece en la consola")

# Iniciar la ejecución continua de la función on_forever
basic.forever(on_forever)
