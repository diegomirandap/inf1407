"use strict";
onload = () => {
    document.getElementById("adiciona-telefone").addEventListener("click", adicionaTelefone);
    document.getElementById("adiciona-email").addEventListener("click", adicionaEmail);
};
function adicionaTelefone() {
    // Cria um novo campo de texto para telefone
    var campo = document.createElement("input");
    campo.setAttribute("type", "text");
    // cria o botao de remover o campo
    var botao = document.createElement("button");
    botao.setAttribute("type", "button");
    botao.appendChild(document.createTextNode("-"));
    botao.addEventListener("click", function () {
        // remove o campo de texto e o botao
        this.parentNode.remove();
    });
    // cria o campo divv que vai envolver o campo de texto
    var div = document.createElement("div");
    div.setAttribute("class", "telefone");
    div.appendChild(campo);
    div.appendChild(botao);
    // adiciona o div na tela
    document.getElementById("telefones").appendChild(div);
}
function adicionaEmail() {
    //cria o campo de email
    var campo = "<input type='text' />";
    //cria o botao de remover o campo
    var botao = "<button type='button' onclick='this.parentNode.remove()'>-</button>";
    var div = "<div class='email'>" + campo + botao + "</div>";
    document.getElementById("emails").innerHTML += div;
}
