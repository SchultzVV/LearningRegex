import re

txt = '''quero que monte um payload com o request do python usando método post com header para aplicação em json usando esse payload [{'datetime': '2023-06-01 13:19:11.374289',
    'n_frame': 6000,
    'label': 'aluno',
    'menssagem': 'Heinz_Roesel_Neto_5830b679-ef3c-11ed-a82a-0e40a07336d7_face_direita',
    'escola': 'ermelino_de_leao',
    'equipamento': 't41129164-109daa',
    'data_upload': '30-05-2023',
    'data_coleta': '30-05-2023',
    'hora_coleta': '17:45:18',
    'primeiro_nome': 'Heinz',
    'nome_completo': 'Heinz Roesel Neto  ',
    'student_id': '5830b679-ef3c-11ed-a82a-0e40a07336d7',
    'posicao_rosto': 'direita'},
    {'datetime': '2023-06-01 13:20:00.305692',
    'n_frame': 21000,
    'label': 'aluno',
    'menssagem': 'Renato_Ramos_b8f86d75-ef3a-11ed-a82a-0e40a07336d7_face_esquerda',
    'escola': 'ermelino_de_leao',
    'equipamento': 't41129164-109daa',
    'data_upload': '30-05-2023',
    'data_coleta': '30-05-2023',
    'hora_coleta': '17:45:18',
    'primeiro_nome': 'Renato',
    'nome_completo': 'Renato Ramos  ',
    'student_id': 'b8f86d75-ef3a-11ed-a82a-0e40a07336d7',
    'posicao_rosto': 'esquerda'}]'''

def get_n_frame(texto):
    match = re.search('n_frame',texto)
    texto = texto[match.end():]
    match = re.search('n_frame',texto)
    texto = texto[match.start():]
    match = re.search('\d\d\d\d\d',texto)
    texto = texto[:match.end()]
    return texto

n_frame = get_n_frame(txt).replace("':"," =")
n_frame = n_frame.replace("n_frame = ", "")
n_frame = int(n_frame)+555
print(n_frame)
print(type(n_frame))


def get_hora_coleta(texto):
    a=0
    return texto

def get_elements(texto,elemento):
    # exemplo de elemento = 'hora_coleta'
    a=0
    return texto