import './App.css';

function App(){

  let nomeEvento="Jornada Acadêmica 2026/2";
  let dataEvento= "Do dia 27 a 29 de Outubro";
  let localEvento= "Faculdade Senac 913 Sul";
  let qtdVagas=30;
  let situacao="";
  let descricaoEvento="Trocas de Experiencias entre Profissionais";
  let eventoGratis= true;
  if(qtdVagas > 0){
    situacao= "Inscrições Disponíveis!"
  }
  else{
    situacao= "Evento Lotado!"
  }
return (
    <main className='container'>
        <h1>{nomeEvento}</h1>
        <p>{descricaoEvento}</p>
        <p>Entrada Franca: {eventoGratis? "Sim" : "Não"}</p>
        <p>Data: {dataEvento}</p>
        <p>Local: {localEvento}</p>
        <p>N° de Vagas: {qtdVagas}</p>
        <p className='situacao'>{situacao}</p>
      </main>
);
}

export default App; 