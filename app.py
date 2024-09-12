import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox('', key=f'check_0'), sg.Input('', key=f'input_0')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo list', layout=layout, finalize=True)

janela = criar_janela_inicial()
tarefas = 1  # Contador para gerar chaves únicas para cada nova tarefa

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        # Adiciona uma nova linha de tarefa
        janela.extend_layout(janela['container'], [[sg.Checkbox('', key=f'check_{tarefas}'), sg.Input('', key=f'input_{tarefas}')]])
        tarefas += 1
    elif event == 'Resetar':
        # Reseta todas as tarefas
        for i in range(tarefas):
            janela[f'check_{i}'].update(False)
            janela[f'input_{i}'].update('')

janela.close()
