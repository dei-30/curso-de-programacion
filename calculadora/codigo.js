document.addEventListener('DOMContentLoaded', () => {
    const resultado = document.getElementById('resultado');
    const teclas = document.querySelector('.teclas');
    let expresion = '';
    teclas.addEventListener('click', e => {
        const tecla = e.target;
        if (tecla.tagName !== 'BUTTON') return;

        const valor = tecla.textContent;
        if (tecla.classList.contains('numero') || tecla.classList.contains('operador') || tecla.classList.contains('decimal')) {
            if (valor === '=' && expresion !== '') {
                try {
                    let resultadoCalculado = eval(expresion.replace('x', '*'));
                    if (!isFinite(resultadoCalculado)) {
                        resultado.value = 'Error';
                        expresion = '';
                    } else {
                        resultado.value = resultadoCalculado;
                        expresion = resultadoCalculado.toString();
                    }
                } catch (error) {
                    resultado.value = 'Error';
                    expresion = '';
                }
            } else if (valor !== '=') {
                expresion += (valor === 'x') ? '*' : valor;
                resultado.value = expresion;
            }
        } 
        
        else if (tecla.classList.contains('utilitario')) {
            if (valor === 'C') {
                expresion = '';
                resultado.value = '';
            } else if (valor === 'DEL') {
                expresion = expresion.slice(0, -1);
                resultado.value = expresion;
            }
        } 
        
        else if (tecla.classList.contains('cientifico')) {
            const numero = parseFloat(expresion);
            if (!isNaN(numero)) {
                let resultadoCientifico;
                if (valor === '√') {
                    resultadoCientifico = Math.sqrt(numero);
                } else if (valor === 'x³') {
                    resultadoCientifico = Math.pow(numero, 3);
                } else if (valor === 'xʸ') {
                    expresion += '**'; 
                    resultado.value = expresion;
                    return;
                } else if (valor === 'tan') {
                    const anguloEnRadianes = numero * (Math.PI / 180);
                    resultadoCientifico = Math.tan(anguloEnRadianes);
                }
                
                if (resultadoCientifico !== undefined) {
                    resultado.value = resultadoCientifico;
                    expresion = resultadoCientifico.toString();
                }
            } else {
                resultado.value = 'Error';
                expresion = '';
            }
        }

    });
});