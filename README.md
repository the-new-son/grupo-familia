# Grupo da Família!!!  WhatsApp Web Automation

Este é um pequeno script em Python que utiliza a biblioteca Selenium para automatizar o envio de uma mensagem no WhatsApp Web. O código abre o WhatsApp Web no navegador Google Chrome e envia a mensagem "Booom dia famíliaaa!" para um grupo específico.

## Requisitos

Antes de executar o código, você precisará ter os seguintes requisitos instalados:

1. Python 3: Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixar a versão mais recente do Python em https://www.python.org.

2. Biblioteca Selenium: O script utiliza a biblioteca Selenium para automatizar a interação com o navegador. Para instalá-la, utilize o seguinte comando:

```bash
pip install selenium
```

3. Google Chrome e chromedriver: Certifique-se de ter o Google Chrome instalado em seu computador. Além disso, baixe o chromedriver compatível com a versão do seu Chrome em https://sites.google.com/a/chromium.org/chromedriver/downloads. Após o download, atualize o caminho do chromedriver na variável `service` no código.

## Configuração

Antes de executar o script, você precisará configurar o perfil de usuário do Chrome e definir o nome do grupo para o qual deseja enviar a mensagem. Siga os passos abaixo:

1. Configurando o perfil do Chrome:
   - Insira o caminho para o perfil de usuário do Chrome na variável `profile_path`. Isso permitirá que o script utilize a sessão do Chrome atual com suas credenciais e configurações.

2. Definindo o nome do grupo:
   - Localize a linha `grupo_familia_xpath = "//span[@title='NOME_DO_GRUPO']"`.
   - Substitua `'NOME_DO_GRUPO'` pelo título exato do grupo do WhatsApp para o qual deseja enviar a mensagem. Certifique-se de que o título esteja escrito exatamente como é mostrado no WhatsApp.

## Executando o Script

Após configurar corretamente o perfil do Chrome e definir o nome do grupo, você pode executar o script. Ele abrirá uma janela do Google Chrome com o WhatsApp Web e enviará a mensagem automaticamente.

Para executar o script, basta digitar o seguinte comando no terminal ou prompt de comando:

```bash
python nome_do_arquivo.py
```

Lembre-se de substituir `nome_do_arquivo.py` pelo nome real do arquivo que contém o código.

## Observações

- O script possui um pequeno trecho comentado no final (`#driver.quit()`). Se quiser que o navegador seja fechado automaticamente após o envio da mensagem, remova o símbolo de hashtag (#) antes dessa linha.

- É importante utilizar o script com responsabilidade e respeitar as políticas de uso do WhatsApp para evitar bloqueios de conta. Automações excessivas ou invasivas podem violar os termos de serviço do WhatsApp.

- Certifique-se de estar conectado ao WhatsApp Web antes de executar o script.

Com essas informações, você está pronto para usar o script de automação do WhatsApp Web! Lembre-se de que o código pode ser modificado e aprimorado de acordo com suas necessidades específicas.