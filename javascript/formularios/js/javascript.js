onload = function() {
    let objName = document.getElementById("nome");
    objName.addEventListener("keyup", function() {
        console.log("mudou o valor do campo nome para: " + objName.value);
    });
    let objSenha = document.getElementById("senha")
    objSenha.addEventListener("blur", function() {
        console.log("saiu do campo senha com o valor: " + objSenha.value);
    });
    document.getElementById("btnSomar").addEventListener("click", function() {
        console.log("O tipo do campo num1 é: " + typeof document.getElementById("num1").value);
        let num1 = parseFloat(document.getElementById("num1").value) || 0;
        let num2 = parseFloat(document.getElementById("num2").value) || 0;
        let resultado = num1 + num2;
        document.getElementById("resultado").value = resultado;
    });
    this.document.getElementById("btnVerificar").addEventListener("click", function() {
        let check1 = document.getElementById("check1").checked;
        let check2 = document.getElementById("check2").checked;
        console.log("valor do campo check1: " + check1);
        console.log("valor do campo check2: " + check2);
    });
    this.document.getElementById("btnVerificarRadio").addEventListener("click", function() {
        let radios = document.getElementsByName("radio1");
        let valorRadio = null;
        for(let i = 0; i < radios.length; i++) {
            if(radios[i].checked) {
                valorRadio = radios[i].value;
                break;
            }
        }
        console.log("valor do radio selecionado: " + valorRadio);
    });
}   