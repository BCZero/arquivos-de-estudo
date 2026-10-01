✅ Recomendação prática para o seu caso
Como você está usando só um repositório pessoal e ainda está aprendendo, eu sugeriria:

manter main como branch principal
trabalhar normalmente em duas máquinas
antes de qualquer coisa:

    git pull origin main

depois fazer alterações

    git add .
    git commit -m "..."
    git push origin main

Isso é simples e eficiente.

Agora, se você quiser começar a usar branches, faça assim:

    git checkout -b estudos-python

trabalha e
quando terminar:

    git checkout main
    git merge estudos-python
    git push origin main

Isso não é “muito burocrático”, mas é mais organizado.

Minha opinião direta
Para você, no momento:

não precisa criar branches por impulso
faça isso só quando a organização virar um problema real
Em repositório pessoal, o melhor é manter a simplicidade até ela começar a atrapalhar.

Fluxo ideal para evitar o problema: “rejected because the tip of your current branch is behind”.

Fluxo simples para duas máquinas
O melhor para o seu caso é manter uma regra bem clara:

main = branch principal
você trabalha sempre em main
antes de cada sessão, faz pull
depois faz alterações, commit e push
quando usar outra máquina, faz pull antes de continuar