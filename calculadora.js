const opcion = prompt("Elige una opcion \n 1 suma\n 2 resta\n 3 multiplicacion\n 4 division\n 5 potencia \n 6 raiz cuadrada \n 7 modulo \n 8 cociente \n elige:");

switch (opcion) {
    case "1":
        let numero_1 = prompt("pon un numero:");
        let numero_2 = Number(numero_1);
        let numero_11 = prompt("pon otro numero:");
        let numero_22 = Number(numero_11);
        let suma = numero_2 + numero_22;
        console.log(`suma: ${suma}`);
        break;

    case "2":
        let num_1 = prompt("pon un numero");
        let num_2 = Number(num_1);
        let num_11 = prompt("pon otro numero");
        let num_22 = Number(num_11);
        let resta = num_2 - num_22;
        console.log(`resta: ${resta}`);
        break;

    case "3":
        let numero1 = prompt("pon un numero");
        let numero2 = Number(numero1);
        let numero1_1 = prompt("pon otro numero");
        let numero2_2 = Number(numero1_1);
        let multiplicacion = numero2 * numero2_2;
        console.log(`multiplicacion: ${multiplicacion}`);
        break;

    case "4":
        let numero3 = prompt("pon un numero:");
        let numero4 = Number(numero3);
        let numero3_3 = prompt("pon otro numero:");
        let numero4_4 = Number(numero3_3);
        let division = numero4 / numero4_4;
        console.log(`division: ${division}`);
        break;
    
    case "5":
        let base= prompt("pon la base:");
        let exponente = prompt("pon el exponente:");
        let baseNumero = Number(base);
        let exponenteNumero = Number(exponente);
        let potencia = baseNumero ^ exponenteNumero;
        console.log(`potencia: ${potencia}`);
        break;
    
    case "6":
        let numeroRaiz = prompt("pon un numero:");
        let numeroRaizNumero = Number (numeroRaiz);
        let raizCuadrada = numeroRaizNumero ** 0.5;
        console.log(`raiz cuadrada: ${raizCuadrada}`);
        break;

    case "7":
        let numeroModulo = prompt("pon un numero:");
        let numeroModuloNumero = Number(numeroModulo);
        let numeroModulo2 = prompt("pon otro numero:");
        let numeroModuloNumero2 = Number(numeroModulo2);
        let modulo = numeroModuloNumero % numeroModuloNumero2;
        console.log(`modulo: ${modulo}`);
        break;
    
    case "8":
        let numeroCociente = prompt("pon un numero:");
        let numeroCocienteNumero = Number(numeroCociente);
        let numeroCociente2 = prompt("pon otro numero:");
        let numeroCocienteNumero2 = Number(numeroCociente2);
        let cociente = Math.floor(numeroCocienteNumero / numeroCocienteNumero2);
        console.log(`cociente: ${cociente}`);
        break;


} 
 