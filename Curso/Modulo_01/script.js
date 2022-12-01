function gritar() {
    alert("Ahhhhhhhhhhhhhhhhhhh!");
}

function perguntar() {
    var nome;
    nome = prompt('Qual é o seu nome?')
    alert("Olá, " + nome);
}

function mudar_texto() {
    var h1 = document.getElementsByTagName('h1');
    
    if (h1[0].innerText == "O grupo de cassino com maior assertividade do Brasil"){
        h1[0].innerText = 'Cresça a sua banca rápidamente'
    }
    else{
        h1[0].innerText = 'O grupo de cassino com maior assertividade do Brasil'
    }
   
}

function incrementa() {
    var p1 = document.getElementById('p1');

    p1.innerText = parseInt(p1.innerText) + 1;
    
}