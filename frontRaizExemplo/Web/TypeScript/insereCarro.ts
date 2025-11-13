onload = () => {
    (document.getElementById('insere') as HTMLButtonElement).addEventListener('click', evento=>{
        evento.preventDefault();

        //TODO: colocar mensagem "EM andamentp..." em azul

        const elements = (document.getElementById('Formulario') as HTMLFormElement).elements as HTMLFormControlsCollection;
        let data: Record<string, string> = {};
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i] as HTMLInputElement;
            data[element.name] = element.value;
        }
        fetch(backendAddress + "carros/umcarro/", {
            method: 'POST', body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => {
            if(response.ok) {
                //TODO: colocar mensagem "Carro inserido com sucesso!" em verde
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Carro inserido com sucesso!';
            } else {
                //TODO: colocar mensagem "Erro ao inserir carro." em vermelho
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Erro ao inserir carro.';}
        })
        .catch(error => { console.log(error) })
    });
}