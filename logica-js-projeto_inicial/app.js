alert('Boas Vindas ao jogo do número secreto');
let secretNumber = 10;
let number;
let tentativa = 0;

while (number != secretNumber){

    let number = prompt('Escolha um número entre 1 e 30');
    tentativa += 1;

    if (secretNumber == number){
        alert(`Isso você acertou!! O número secreto era ${secretNumber}`);
        alert(`Você precisou de ${tentativa} tentativas`);
        break
    }else {
        if (secretNumber > number){
            alert(`O número secreto é maior do que ${number}`);
        }else {
            alert(`O número secreto é menor do que ${number}`);
        };
    }
};


