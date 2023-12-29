"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot, Backend

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import pandas as pd
import numpy as np




# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    # Caminho da aplicação
    app_path = r"https://web.whatsapp.com/"

    #importar a base de dados
    base = pd.read_excel(r"botyago\Contatos.xlsx")

    #Iniciando o whatzap web
    bot.browse(app_path)

    # Para cada linha da tabela
    for linha in base.index:

        contato = base.loc[linha,"Contato"]
        mensagem = base.loc[linha,"Msg"]
        arquivo = base.loc[linha,"Arquivo"]

        if not bot.find( "lupa", matching=0.97, waiting_time=60000):
            not_found("lupa")
        bot.click()
   
        bot.type_keys_with_interval(105,contato)
        bot.enter()

        if pd.isna(arquivo):
            bot.paste(mensagem)
            bot.enter()
        else:
            bot.paste(mensagem)
            bot.enter()
            if not bot.find( "cruz", matching=0.97, waiting_time=10000):
               not_found("cruz")
            bot.click()
            if not bot.find( "Documento", matching=0.97, waiting_time=10000):
                not_found("Documento")
            bot.click()
                
            if not bot.find( "nome", matching=0.97, waiting_time=10000):
                not_found("nome")

            bot.paste(arquivo)
            bot.enter()
                    
            if not bot.find( "Enviar", matching=0.97, waiting_time=10000):
                not_found("Enviar")
            bot.click()
                        
        if bot.find( "seta", matching=0.97, waiting_time=3000):   
            bot.click()
        
        bot.wait(2000)
        
        # Pressing Alt + f4, the keyboard shortcut.
    bot.alt_f4()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()






