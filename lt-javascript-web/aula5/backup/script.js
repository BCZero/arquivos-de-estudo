let tecnologias = ["html", "css", "javascript", "b", "a"]
tecnologias[1] = "css3";
tecnologias.push("git");
alert("Removi o elemento: "+tecnologias.pop());
alert("Tamanho da estrutura de dados: " +tecnologias.length);
tecnologias.splice(3,4);
alert(tecnologias);