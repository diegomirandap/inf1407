"use strict";
onload = () => {
    document.getElementById('insere').addEventListener('click', evento => {
        evento.preventDefault();
        //TODO: colocar mensagem "EM andamentp..." em azul
        const elements = document.getElementById('Formulario').elements;
        let data = {};
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            data[element.name] = element.value;
        }
        fetch(backendAddress + "carros/umcarro/", {
            method: 'POST', body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })
            .then(response => {
            if (response.ok) {
                //TODO: colocar mensagem "Carro inserido com sucesso!" em verde
                document.getElementById('mensagem').innerHTML = 'Carro inserido com sucesso!';
            }
            else {
                //TODO: colocar mensagem "Erro ao inserir carro." em vermelho
                document.getElementById('mensagem').innerHTML = 'Erro ao inserir carro.';
            }
        })
            .catch(error => { console.log(error); });
    });
};
