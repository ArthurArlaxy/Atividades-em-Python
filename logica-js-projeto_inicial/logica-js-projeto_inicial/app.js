alert('Boas Vindas ao jogo do número secreto');
let chooseNumber = 100;
let secretNumber = parseInt(Math.random() * chooseNumber + 1 );
let number;
let tentativa = 0;

while (number != secretNumber){

    let number = prompt(`Escolha um número entre 1 e ${chooseNumber}`);
    tentativa += 1;

    if (secretNumber == number){
        alert(`Isso você acertou!! O número secreto era ${secretNumber}`);
        break;
    }else {
        if (secretNumber > number){
            alert(`O número secreto é maior do que ${number}`);
        }else {
            alert(`O número secreto é menor do que ${number}`);
        };
    };
};

let palavraTentativa  = tentativa > 1 ? 'tentativas' : 'tentativa';
alert(`Você precisou de ${tentativa} ${palavraTentativa}`);