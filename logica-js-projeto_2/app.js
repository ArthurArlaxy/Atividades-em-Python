let chooseNumber = 100;

let titulo = document.querySelector('h1');
titulo.innerHTML = 'Jogo do número secreto';

let paragrafo = document.querySelector('p');
paragrafo.innerHTML = `Escolha um número de 0 a ${chooseNumber}`;

function verificarChute(){
    console.log('Me apertaram');
}