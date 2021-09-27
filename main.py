import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = ''
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu', '/start', 'start'):
            return f'''Olá bem vindo ao seu parceiro informativo de covid em BSB. Digite o número da ação que gostaria:{os.linesep}{os.linesep}1 - Pontos de vacinação para primeira dose{os.linesep}2 - Pontos de vacinação para segunda dose{os.linesep}3 - Pontos de vacinação para dose de reforço para 85+{os.linesep}4 - Máscaras Recomendadas{os.linesep}5 - Profilaxia{os.linesep}6 - Taixa de eficácia das vacinas{os.linesep}7 - Tempo de espera das doses de vacinas(Remind me){os.linesep}8 - Outras funcionalidades em desenvolvimento
            '''
        if mensagem == '1':
            return f'''Para quem tem entre 13-17 anos{os.linesep}Praça dos Cristais - 18 às 22hrs{os.linesep}{os.linesep}Para quem tem entre 18 anos ou mais{os.linesep}Parque da cidade - 9 às 17hrs{os.linesep}TaguaParque - 9 às 17hrs{os.linesep}UBS 3 Recanto das Emas - 9 às 17hrs{os.linesep}UBS 2 Taguatinga - 9 às 17hrs{os.linesep}{os.linesep}Para quem é gestante ou puerperas{os.linesep}Praça dos Cristais - 18 às 22hrs{os.linesep}UBS 12 Samambaia - 9 às 17hrs{os.linesep}UBS 3 Taguatinga - 9 às 17hrs{os.linesep}{os.linesep}Gostaria de voltar ao menu principal? Digite "menu"
            '''
        elif mensagem == '2':
            return f'''Em desenvolvimento 2{os.linesep}Em desenvolvimento 2'''
        elif mensagem == '3':
            return f'''Em desenvolvimento 3{os.linesep}Em desenvolvimento 3'''
        elif mensagem == '4':
            return f'''Máscaras contra a Covid-19: guia mostra os melhores tipos e as combinações mais eficientes{os.linesep}{os.linesep}Máscaras PFF2 (ou N95){os.linesep}Máscaras KN95{os.linesep}Máscaras elastoméricas{os.linesep}Máscaras com válvula{os.linesep}Máscaras cirúrgicas ou de procedimentos{os.linesep}Máscaras de pano com 3 camadas{os.linesep}{os.linesep}Gostaria de voltar ao menu principal? Digite "menu"
            '''
        elif mensagem == '5':
            return f'''Para evitar a propagação da COVID-19, siga estas orientações{os.linesep}{os.linesep}Mantenha uma distância segura de outras pessoas, mesmo que elas não pareçam estar doentes.{os.linesep}Use máscara em público, especialmente em locais fechados ou quando não for possível manter o distanciamento físico.{os.linesep}Prefira locais abertos e bem ventilados em vez de ambientes fechados. Abra uma janela se estiver em um local fechado.{os.linesep}Limpe as mãos com frequência. Use sabão e água ou álcool em gel.{os.linesep}Tome a vacina quando chegar a sua vez. Siga as orientações locais para isso.{os.linesep}Cubra o nariz e a boca com o braço dobrado ou um lenço ao tossir ou espirrar.{os.linesep}Fique em casa se você sentir indisposição.{os.linesep}{os.linesep}Gostaria de voltar ao menu principal? Digite "menu"
            '''
        elif mensagem == '6':
            return f'''Em desenvolvimento 6{os.linesep}Em desenvolvimento 6'''
        elif mensagem == '7':
            return f'''Em desenvolvimento 7{os.linesep}Em desenvolvimento 7'''
        elif mensagem == '8':
            return f'''Em desenvolvimento 8{os.linesep}Em desenvolvimento 8'''

        elif mensagem.lower() in ('s', 'sim'):
            return '''Confirmado! '''
        elif mensagem.lower() in ('n', 'não'):
            return '''Cancelado!'''
        else:
            return 'Gostaria de voltar ao menu principal? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
