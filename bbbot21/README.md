# bbbot21
## Teste de bot por reconhecimento de imagem simulando cliques humanos (aleatórios)

### tl;dr: abre o site da Globo, entra na sua conta, abre a página do paredão, deixa o brother visível e liga o bot que ele se vira

Meio sem tempo irmão pro readme, mas você vai precisar de:

0 - um computador (que eu não posso te ajudar com isso) e python (que eu já te ajudei com isso, caso não tenha/não saiba cheque algum dos meus outros dois repositórios facebot ou bbbot que eu explico tudo)

1 - imagem do nome do brother, do botão do captcha (que tem que clicar em "sou humano" rs) e do votar novamente

Simples: tira print, corta esse pedaço, salva
de qualquer forma vou incluir as minhas e a foto do brother, que é pra quem o bot está pronto pra votar (se quiser votar em outra pessoa, você que lute)

2 - o bot funciona por reconhecimento de imagem, então precisamos do pyautogui e do PIL (que só usei pra otimizar a abertura de imagem, não é vitalmente necessário, caso não queira usar é só rancar de lá)

$ pip install pyautogui

$ pip install pillow

3 - ... infelizmente manter o browser aberto, já que qualquer tentativa de automação em segundo plano -> falhei

Ok, a treta toda é que não tem como abrir o site da Globo por algum browser automatizado tipo o selenium já que a header denuncia (você basicamente está com uma melância no pescoço escrito BOT) e qnd tenta votar o site prontamente chama o hCaptcha que começa a perguntar aquelas dezenas de "escolha imagem de um barco" que nem eu sei responder direito, quem dirá meu mero botzinho.

### A solução
usar reconhecimento de imagem pra achar onde clicar e apertar os botões como se fosse uma pessoa.

### A nova treta
como apontado pelo Pedrinho (https://github.com/nasaphreak), a galera lá monitora onde e em quanto tempo você clica, então caso demore sempre o mesmo tanto de tempo e clica sempre no mesmo lugar, eles vão descobrir e chamar as imagens do hCaptcha só pra ~testar se tu não é um bot mesmo e ~pasmem~ nós somos (#SomosTodosBots)

### A solução final
meti um monte de aleatoriedade tanto em onde ele vai clicar (tomando cuidado pra não ser fora da área clicável) tanto em COMO ele vai clicar (namoral, eu até coloquei pra ele escolher aleatoriamente na lista de funções disponíveis, cada vez), então o jeito e a duração do clique muda.  Também inclui ele apertar um f5 pra atualizar a página sempre que der ruim (caso ele não encontre a imagem, começa de novo) e descobri que algumas vezes quando o hCaptcha é acionado, alguns refreshs podem confundir o captcha e ele não chama kkk

### Otimização
Botei uns sleep aí no meio porque meu browser tava demorando pra abrir e dava problema, caso o seu seja mais rápido/lento é só ir tirando/diminuindo/aumentando o tempo dos sleep.

### Problemas
vish... pode ter uns problemas hein, do tipo: a tela do seu PC pode ser dimensionalmente diferente da minha, então você vai precisar mapear melhor o tamanho dos botões e seus limites usando pyautogui.position(), mas esperamos que não chegue a isso.
Sei lá, as imagens podem dar treta? Qualquer coisa tira print novo do seu PC aí e nomeia do mesmo jeito que tá os meus. Não força a barra em velocidade de clique que o site desconfia. Por fim, torce pro site não pedir captcha de imagem, se não já era, nesse caso espera um pouco/muda de browser, etc.
