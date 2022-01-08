# PythonTraining
 Aprendendo Python

<!-- 

Configurações para otimizar o Python em seus projetos no Vscode, Sistema Linux Mint.
Segundo Otávio Miranda, ótimo professor.


1° Baixando extensões
    - code runner
    - python (da microsoft)
    
2° Criar sempre o ambiente virtual no novo projeto (virtualenv)
    - Abrir terminal no Vscode
    
    - digitar: python3 -m venv venv
        Isso criará uma pasta chamada venv, em seu projeto.
    
    - Após criar um arquivo com extensão .py
        Provavelmente ao fazer isso, fechar e abrir um novo terminal, ele pedirá para
        instalar algumas extensões no projeto e aparecerá no começo da linha do
        terminal um: (venv). Se não aparecer, digitar e executar: . venv/bin/activate
    
    - Pode ocorrer de ele não criar uma outra pasta chamada: .vscode
        Com um arquivo dentro chamado "settings.json"
        Serve para configurar algumas coisas no projeto específico
        E neste case não aparecer a pasta e o arquivo, pode criar manualmente.
    
    - Configurações no "settings,json":

        "python.pythonPath": "venv/bin/python",
        "code-runner.executorMap": {
        "python": "venv/bin/python",
    },

3° Settings.json - global

    settings > settings.json e digitar:

        "code-runner.ignoreSelection": true,
        "code-runner.runInTerminal": true,
        "python.linting.mypyEnabled": true,
        "python.linting.flake8Enabled": true,
        "python.testing.unittestEnabled": true,
        "[python]": {
            "editor.formatOnSave": true,
        },
        "window.zoomLevel": 1,
        "bracket-pair-colorizer-2.depreciation-notice": false,


    Agora pode seguir com o aprendizado e executar de forma mais tranquila o python no Vscode. Sistema Linux.

-->