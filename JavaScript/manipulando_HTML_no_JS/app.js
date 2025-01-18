let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function clickConsole(){
    console.log('Me clicaram!');
};

function clickAlert(){
    alert('Eu amo JavaScript');
};

function clickPrompt(){
    cidade = prompt('Digite uma cidade: ');
    alert(`Estive em ${cidade} e lembrei de você! :)`)
};

function clickSoma(){
    contador =  0;
    soma = 0;
    while (contador != 2 ){
        contador += 1;
        number = parseInt(prompt(`Digite o ${contador}° número: `));
        soma += number;
    };
    alert(`O resultado da soma foi ${soma}`);
};