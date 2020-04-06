# bbbot
## Instalações necessárias
### Instale o Python

Para instalar o Python 3, digite em um terminal:

$ sudo apt-get install python3

### Instale o pip

Para instalar o gerenciador de pacotes pip, digite em um terminal:

$ sudo apt-get install python3-pip

### Instale o Selenium

Digite em um terminal

$ python -m pip install -U selenium

### Edições

Com o bbbot.py e o chromedriver.exe na mesma pasta, faça o seguinte:
  
1º Clique com o botão direito do mouse no chromedriver e em propriedades para checar sua localização (ou seja, a pasta onde você salvou)

2º Clique para editar o arquivo bbbot.py, pode ser em qualquer bloco de notas ou editor de scripts que você preferir

3º Vá em "chrome_path" e no meio das aspas, apague o endereço caminho\até\chromedriver.exe e cole o endereço que copiou no 1º passo, ele irá ficar assim:
Exemplo: chrome_path = r"C:\Users\usuario\Desktop\pasta\chromedriver.exe"

4º Vá em "login_globo" e "senha_globo" e troque seu_email.com pelo seu email e sua_senha pela senha para efetuar o login no site

### Executando

5º Após isso, é só salvar a edição e executar o bbbot.py na sua linha de comando com 

$ python bbbot.py 

;)

### Edição extra para futuros paredões

O link do site de votação muda, então é só mudar o site dentro de driver.get("https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-babu-flayslane-ou-marcela-5ed83d00-014e-401d-80c8-20314769ce2f.ghtml") com o paredão da vez entre aspas

O bot está configurado para votar automaticamente na Marcela nesse paredão, mas se quiser mudar é só encontrar os caminhos XPath de cada participante. 
Ou você pode usar o atalho com a dica: Marcela é a terceira participante, seu driver.find_element_by_xpath("""/html/body/div[2]/div[4]/div/div[1]/div[4]/div[3]/div/div[1]""").click() contém esse div[3], assim como as outras 2 variáveis do captcha dessa sessão (, se mudar para 1 e 2 serão os respectivos participantes.
Exemplo, o driver.find_elemet_by_xpath do segundo participante é: """/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div/div[1]"""

## Solução de problemas
### Chromedriver

Caso o chromedriver dê erro, pode ser por conta da permissão da pasta onde ele está, uma solução possível é colocar o chromedriver.exe no PATH ou em alguma pasta onde o PATH já abra normalmente e apagar a variável chrome_path
Outra opção pode ser com a versão do chromedriver que não é compatível com sua versão do Chrome ou do PC, para isso baixe outra versão no site: https://chromedriver.chromium.org/downloads

### Selenium

Instalar o Selenium pode ser treta às vezes, então vou incluir a documentação original, caso o método que citei acima não funcione: https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/

### Sistema operacional

É pra funcionar em todos os OS, Windows e MAC podem dar alguns problemas de instalação, como na hora de instalar o pip pra instalar o Selenium, mas daí é só pesquisar "como instalar pip no Windows".

### Problemas a resolver

Se demora muito pra ter resposta do site, o bot fica bravo e fecha

### Agradecimentos

Bot inspirado no bot de @he4rt e @r3br34k
