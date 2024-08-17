// Iniciar la ejecución continua de la función on_forever
basic.forever(function () {
    // Mostrar texto en la pantalla LED
    basic.showString("Hola Mundo!")
    // Mostrar un mensaje en la consola
    serial.writeLine("Este texto aparece en la consola")
})
