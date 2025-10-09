// novos tipos
type numberOrString = number | string;

//EXEMPLO DE CONSTANTES
//Exemplos do tipo string
const TEXTO: string = "Um texto";
const OUTRO_TEXTO: String = "Outro texto";

//TEXTO = 'mudou o valor da constante'; //vai dar erro pq é uma constante

let nome: string;
nome = "João";
nome = "Maria";

let aluno = {
    nome: "Pedro",
    idade: 20,
    matriculado: true
};

aluno.nome = "Ana";

let professor: {
    nome: string,
    idade: number,
    ministrando: boolean,
};
professor = {
    nome: "Carlos",
    idade: 40,
    ministrando: true
};