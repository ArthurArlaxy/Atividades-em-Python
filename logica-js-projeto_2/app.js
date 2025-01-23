let chooseNumber = numeroSecreto();

let titulo = document.querySelector('h1');
titulo.innerHTML = 'Jogo do número secreto';

let paragrafo = document.querySelector('p');
paragrafo.innerHTML = `Escolha um número de 0 a 10`;

function numeroSecreto(){
    return parseInt(Math.random() * 10 + 1);
}

function verificarChute(){
    let chute = document.querySelector('input').value;
    console.log(chute == chooseNumber)
}