"""Simple bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, replymarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)
import webbrowser
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
LOC, DOSE1, D1217, D18, DOSE2, DOSER85, PNOTURNO, TAXAEFICACIA, EFIASTRAZENECA, EFICORONA, EFIPFIZER, OPCOES2, NOVAVARIANTE, TERCEIRADOSE, COMOFUNCIONAVACINA, STATUS2DOSE, CARE, MASK, START, END, ASTRA2DOSE, CORONA2DOSE, PFIZER2DOSE, AGENDAMENTO, COMORBIDADE, CONSULTAR, IMPRIMIR, LINKREDIRECIONAMENTO = range(
    28)

# ---------------------------------------- INICIO ----------------------------------------


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(LOC)),
            InlineKeyboardButton("2", callback_data=str(MASK)),
            InlineKeyboardButton("3", callback_data=str(CARE)),
            InlineKeyboardButton("4", callback_data=str(TAXAEFICACIA)),
        ], [
            InlineKeyboardButton("5", callback_data=str(STATUS2DOSE)),
            InlineKeyboardButton("6", callback_data=str(LINKREDIRECIONAMENTO)),
            InlineKeyboardButton("...", callback_data=str(OPCOES2)),
            InlineKeyboardButton("🛑", callback_data=str(END)),

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(
        '''Olá bem vindo ao seu parceiro informativo de Covid-19 do DF. Selecione a ação desejada:

        1 - Locais Postos de vacinação
        2 - Máscaras Recomendadas
        3 - Cuidados e Profilaxia
        4 - Taxa de eficácia das vacinas
        5 - Tempo de intervalo das doses
        6 - Link de redirecionamento (agendamento,cadastro,consulta e imprimir)
        ... - Mais informações da vacina
        ''', reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

# ---------------------------------------- RESTART ----------------------------------------


def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(LOC)),
            InlineKeyboardButton("2", callback_data=str(MASK)),
            InlineKeyboardButton("3", callback_data=str(CARE)),
            InlineKeyboardButton("4", callback_data=str(TAXAEFICACIA)),
        ], [
            InlineKeyboardButton("5", callback_data=str(STATUS2DOSE)),
            InlineKeyboardButton("6", callback_data=str(LINKREDIRECIONAMENTO)),
            InlineKeyboardButton("...", callback_data=str(OPCOES2)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(
        text='''Olá bem vindo ao seu parceiro informativo de Covid-19 do DF. Selecione a ação desejada:

        1 - Locais Postos de vacinação
        2 - Máscaras Recomendadas
        3 - Cuidados e Profilaxia
        4 - Taxa de eficácia das vacinas
        5 - Tempo de intervalo das doses
        6 - Link de redirecionamento (agendamento,cadastro,consulta e imprimir)
        ... - Mais informações da vacina
        ''', reply_markup=reply_markup)
    return FIRST

# ---------------------------------------- LOCAIS ----------------------------------------


def locais(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Abaixo temos o link do site oficial da secretaria de saúde que disponibiliza os locais e os horários das vacinas para pessoas de todas as idades. \nO site contem primeiras doses, segundas doses, doses adicionais, doses de reforço e postos noturnos. A pagina é oficial e é atualizada regularmente.

        https://www.saude.df.gov.br/locaisdevacinacao/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- MASCARAS ----------------------------------------


def mascaras(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''2 - Máscaras Recomendadas contra a Covid-19: guia mostra os melhores tipos e as combinações mais eficientes
        
         - Máscaras PFF2 (ou N95)
        https://d24ji74u9qkhok.cloudfront.net/wp-content/uploads/2020/04/mascaras_page-0001-768x432.jpg
        - Máscaras KN95
        https://http2.mlstatic.com/D_NQ_NP_870886-MLB45514116642_042021-O.jpg
        - Máscaras elastoméricas
        https://a-static.mlcdn.com.br/1500x1500/mascara-semifacial-gvs-elipse-p3r-anti-odor-m-g/tuzaferramentaseepi/4da78a0c7ec811eab21e4201ac18501e/7494ae109efefffa302f7d2044302cfc.jpg
        - Máscaras com válvula
        https://a-static.mlcdn.com.br/618x463/mascara-p2-com-valvula-delta-plus/sanchesby/8810170620/fda07a0150d5bf6dafa1653cc141476c.jpg
        - Máscaras cirúrgicas ou de procedimentos
        https://cirurgicaeldorado.com.br/wp-content/uploads/2020/02/Mascara-Cirurgica.jpeg
        - Máscaras de pano com 3 camadas (Apenas em ultimo caso de falta/emergencia)
        ''', reply_markup=reply_markup
    )
    return SECOND

# ---------------------------------------- CUIDADOS ----------------------------------------


def cuidados(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Para evitar a propagação da COVID-19, siga estas orientações
        
        Mantenha uma distância segura de outras pessoas, mesmo que elas não pareçam estar doentes.
        Use máscara em público, especialmente em locais fechados ou quando não for possível manter o distanciamento físico.
        Prefira locais abertos e bem ventilados em vez de ambientes fechados. Abra uma janela se estiver em um local fechado.
        Limpe as mãos com frequência. Use sabão e água ou álcool em gel.
        Tome a vacina quando chegar a sua vez. Siga as orientações locais para isso.
        Cubra o nariz e a boca com o braço dobrado ou um lenço ao tossir ou espirrar.
        Fique em casa se você sentir indisposição.
        ''', reply_markup=reply_markup
    )
    return SECOND

# ---------------------------------------- REDIRECIONAMENTO ----------------------------------------


def linkredirecionamento(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(COMORBIDADE)),
            InlineKeyboardButton("2", callback_data=str(CONSULTAR)),
            InlineKeyboardButton("3", callback_data=str(IMPRIMIR)),
        ],[
            InlineKeyboardButton("◀️", callback_data=str(START)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
            Links de redirecionamento:

        1- Cadastro de Comorbidades e Grupos Prioritários
        2- Consultar agendamento
        3- Imprimir ficha de vacina
        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

# ---------------------------------------- COMORBIDADE ----------------------------------------


def comorbidade(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""

    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton(
                "◀️", callback_data=str(LINKREDIRECIONAMENTO)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Cadastro de Comorbidades e Grupos Prioritários
        
        https://vacina.saude.df.gov.br/Comorbidade

        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

# ---------------------------------------- AGENDAMENTO ----------------------------------------


def agendamento(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='''
        'https://vacina.saude.df.gov.br/'
        ''', reply_markup=replymarkup
    )
    return FIRST


# ---------------------------------------- CONSULTAR ----------------------------------------


def consultar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton(
                "◀️", callback_data=str(LINKREDIRECIONAMENTO)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Consultar agendamento da vacina

    https://vacina.saude.df.gov.br/Home/Consultar
        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

# ---------------------------------------- IMPRIMIR ----------------------------------------


def imprimir(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton(
                "◀️", callback_data=str(LINKREDIRECIONAMENTO)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Link para imprimir ficha de vacina
        
        https://vacina.saude.df.gov.br/Home/Ficha
        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

# ---------------------------------------- TAXA EFICIENCIA ----------------------------------------


def taxaeficacia(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(EFIASTRAZENECA)),
            InlineKeyboardButton("2", callback_data=str(EFICORONA)),
            InlineKeyboardButton("3", callback_data=str(EFIPFIZER)),
        ],[
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Escolha a opção da vacina que deseja saber a eficácia:

        1 - Astrazeneca
        2 - Coronavac
        3 - Pfizer
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- EFICACIA ASTRAZENECA ----------------------------------------


def efiastrazeneca(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(TAXAEFICACIA)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
        1 - Astrazeneca

        A vacina demonstrou eficácia de 70,4% contra a infecção e 100% contra casos graves da infecção.


        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- EFICACIA CORNAVAC ----------------------------------------


def eficorona(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(TAXAEFICACIA)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
        2 - Coronavac

        A vacina demonstrou uma taxa de eficácia de 78% para casos leves e de 100% para infecções moderadas e graves.


        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- EFICACIA PFIZER ----------------------------------------


def efipfizer(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(TAXAEFICACIA)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
        3 - Pfizer

        A vacina apresentou 95% de eficácia contra infecção e 100% contra casos graves da doença.


        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- OPCOES 2 ----------------------------------------


def opcoes2(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(COMOFUNCIONAVACINA)),
            InlineKeyboardButton("2", callback_data=str(TERCEIRADOSE)),
            InlineKeyboardButton("3", callback_data=str(NOVAVARIANTE)),
        ],[
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Mais informações sobre a vacina:

        1 - Como a vacina funciona
        2 - É preciso tomar terceira dose?
        3 - A vacina contra a nova variante
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- COMO FUNCIONA A VACINA ----------------------------------------


def comofunciona(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(OPCOES2)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''1 - Como a vacina funciona
        
        Tecnologia genética do RNA mensageiro (Pfizer e Moderna): é uma tecnologia mais utilizada na produção de vacinas para animais e que faz com que as células saudáveis do corpo produzam a mesma proteína que o coronavírus utiliza para entrar nas células. Ao fazer isso, o sistema imune é obrigado a produzir anticorpos que, durante uma infecção, podem neutralizar a proteína do verdadeiro coronavírus e impedir o desenvolvimento da infecção;

        Uso de adenovírus modificados (Astrazeneca, Sputnik V e J&J): consiste em utilizar adenovírus, que são inofensivos para o corpo humano, e modificá-los geneticamente para que atuem de forma parecida com o coronavírus, mas sem risco para a saúde. Isso faz com que o sistema imunológico treine e produza anticorpos capazes de eliminar o vírus caso aconteça a infecção;
        
        Uso do coronavírus inativado (Coronavac) : é utilizada uma forma inativada do novo coronavírus que não provoca a infecção, nem problemas para a saúde, mas que permite ao corpo produzir os anticorpos necessários para combater o vírus.

        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- TERCEIRA DOSE ----------------------------------------


def terceiradose(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(OPCOES2)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''2 - É preciso tomar terceira dose?

        O Ministério da Saúde no Brasil autorizou a terceira dose da vacina contra a COVID-19, com previsão de iniciar a aplicação em setembro, preferencialmente com uma dose de reforço da vacina da Pfizer, ou de forma alternativa, uma dose de uma das vacinas da AstraZeneca ou da Janssen.

        Essa dose de reforço inicialmente será feita em idosos com mais de 60 anos, que tenham recebido as duas doses de qualquer outra vacina da COVID-19 há pelo menos 6 meses, ou para pessoas com o sistema imunológico enfraquecido, que completaram o esquema de vacinação com duas doses de qualquer vacina ou dose única da Janssen há pelo menos 28 dias, e para profissionais de saúde. [5]. Veja quando tomar a terceira dose da vacina contra a COVID-19. 

        Em Portugal, a Agência Europeia de Medicamentos autorizou a aplicação da terceira dose da vacina contra a COVID-19 com Pfizer para pessoas acima dos 65 anos e que foram vacinadas com esse imunizante, e com Moderna para pessoas a partir dos 18 anos 6 a 8 meses após completar o esquema vacinal, sendo recomendada meia dose.

        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- NOVA VARIANTE ----------------------------------------


def novavariante(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton("◀️", callback_data=str(OPCOES2)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''3 - A vacina contra a nova variante

        De acordo com a OMS [3], as vacinas contra a COVID-19 deverão apresentar efeito contra as variantes do vírus que forem surgindo, já que estimulam uma complexa resposta imune de todo o organismo, que ficará "atento" para partículas do novo coronavírus, mesmo que surjam algumas modificações na sua estrutura.

        Ainda assim, mesmo que se fique infectado com uma nova variante, as chances de desenvolver uma infecção grave que coloque a vida em risco é muito inferior para quem se encontra completamente imunizado, ou seja, com mais de 2 semanas após a 2ª dose da vacina.

        É esperado que, ao longo do tempo, e à medida que vão surgindo novas variantes, que a composição das vacinas seja gradualmente atualizada, para conferir maior proteção.

        fonte: https://www.tuasaude.com/vacina-covid/
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- INTERVALO DOSE 2 ----------------------------------------


def status2dose(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ASTRA2DOSE)),
            InlineKeyboardButton("2", callback_data=str(CORONA2DOSE)),
            InlineKeyboardButton("3", callback_data=str(PFIZER2DOSE)),
        ],[
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Gostaria de saber o intervalo da segunda dose de qual vacina?

        1 - Astrazeneca 
        2 - CoronaVac
        3 - Pfizer
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- INTERVALO ASTRA ----------------------------------------


def astra2dose(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("◀️", callback_data=str(STATUS2DOSE)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Astrazeneca:

        Intervalo de 8 semanas;
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- INTERVALO CORONA ----------------------------------------


def corona2dose(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton("◀️", callback_data=str(STATUS2DOSE)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Coronavac: 
        
        Intervalo de 2 a 4 semanas;
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- INTERVALO PFIZER ----------------------------------------


def pfizer2dose(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [

            InlineKeyboardButton("◀️", callback_data=str(STATUS2DOSE)),
            InlineKeyboardButton("⏏️ Home", callback_data=str(START)),
            InlineKeyboardButton("🛑", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Pfizer:
        
        Intervalo de 8 semanas;
        ''', reply_markup=reply_markup
    )
    return FIRST

# ---------------------------------------- FIM ----------------------------------------


def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Nos vemos na próxima consulta!")
    return ConversationHandler.END

# ---------------------------------------- MAIN ----------------------------------------

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    readarq = open("token.txt")
    token = readarq.read()
    readarq.close()
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(locais, pattern='^' + str(LOC) + '$'),
                CallbackQueryHandler(
                    taxaeficacia, pattern='^' + str(TAXAEFICACIA) + '$'),
                CallbackQueryHandler(
                    efiastrazeneca, pattern='^' + str(EFIASTRAZENECA) + '$'),
                CallbackQueryHandler(
                    eficorona, pattern='^' + str(EFICORONA) + '$'),
                CallbackQueryHandler(
                    efipfizer, pattern='^' + str(EFIPFIZER) + '$'),
                CallbackQueryHandler(
                    opcoes2, pattern='^' + str(OPCOES2) + '$'),
                CallbackQueryHandler(
                    comofunciona, pattern='^' + str(COMOFUNCIONAVACINA) + '$'),
                CallbackQueryHandler(
                    terceiradose, pattern='^' + str(TERCEIRADOSE) + '$'),
                CallbackQueryHandler(
                    novavariante, pattern='^' + str(NOVAVARIANTE) + '$'),
                CallbackQueryHandler(mascaras, pattern='^' + str(MASK) + '$'),
                CallbackQueryHandler(cuidados, pattern='^' + str(CARE) + '$'),
                CallbackQueryHandler(
                    comorbidade, pattern='^' + str(COMORBIDADE) + '$'),
                CallbackQueryHandler(
                    consultar, pattern='^' + str(CONSULTAR) + '$'),
                CallbackQueryHandler(
                    imprimir, pattern='^' + str(IMPRIMIR) + '$'),
                CallbackQueryHandler(
                    imprimir, pattern='^' + str(IMPRIMIR) + '$'),
                CallbackQueryHandler(
                    linkredirecionamento, pattern='^' + str(LINKREDIRECIONAMENTO) + '$'),
                CallbackQueryHandler(
                    agendamento, pattern='^' + str(AGENDAMENTO) + '$'),
                CallbackQueryHandler(
                    status2dose, pattern='^' + str(STATUS2DOSE) + '$'),
                CallbackQueryHandler(
                    astra2dose, pattern='^' + str(ASTRA2DOSE) + '$'),
                CallbackQueryHandler(
                    corona2dose, pattern='^' + str(CORONA2DOSE) + '$'),
                CallbackQueryHandler(
                    pfizer2dose, pattern='^' + str(PFIZER2DOSE) + '$'),
                CallbackQueryHandler(
                    start_over, pattern='^' + str(START) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(END) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(
                    start_over, pattern='^' + str(START) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(END) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
