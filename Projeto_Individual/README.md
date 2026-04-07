# Anotobolso Versão 1

O Anotobolso é um sistema para facilitar a criação anotações sobre livros de compartilhá-las:<br>
Funcionalidades<br>
* Criação, modificação e deleção de livros por parte do usuário
* Criação, modificação e deleção de anotações em livros criados pelo usuário
* Visualizar livros e anotações de outros usuários
* Configuração de privacidade para livros e anotações
* Seguir outros usuários

### Transparência acerca do uso de IA
* GitHub copilot foi gerado para um rascunho inicial da tela de rascunho, cujo html gerado foi adaptado para criar a classe _card_, utilizada amplamente no site.
* Gemini foi utilizado como ferramenta de debug/pesquisa. Um exemplo de debugging é na linha abaixo:
```
    query = select(Annotation).where(Annotation.book_id == book.id and Annotation.public == True).order_by(Annotation.date.desc())
```
a query ignora a segunda condição `Annotation.public == True`, a ferramenta de IA foi capaz de apontar que a sintaxe correta era (trocando "and" por ","):
```
    query = select(Annotation).where(Annotation.book_id == book.id, Annotation.public == True).order_by(Annotation.date.desc())
```