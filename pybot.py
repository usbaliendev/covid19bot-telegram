"""Simple bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
LOC, DOSE1, DOSE2, DOSER85, PNOTURNO, SIX, SEVEN, CARE, MASK, START, END = range(
    11)


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
            InlineKeyboardButton("4", callback_data=str(SEVEN)),
            InlineKeyboardButton("5", callback_data=str(SEVEN)),
            InlineKeyboardButton("6", callback_data=str(SEVEN)),
            InlineKeyboardButton("outro", callback_data=str(SEVEN)),
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
        5 - Tempo de intervalo das doses (Remind me)
        6 - Outras funcionalidades em desenvolvimento..
        7 - TESTE DE ATUALIZACAO
        ''', reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


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
            InlineKeyboardButton("4", callback_data=str(SEVEN)),
            InlineKeyboardButton("5", callback_data=str(SEVEN)),
            InlineKeyboardButton("6", callback_data=str(SEVEN)),
            InlineKeyboardButton("6", callback_data=str(SEVEN)),
            InlineKeyboardButton("Outro", callback_data=str(SEVEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(
        text='''Fluxo reinciado. Selecione a ação desejada:

        1 - Locais Postos de vacinação
        2 - Máscaras Recomendadas
        3 - Cuidados e Profilaxia
        4 - Taxa de eficácia das vacinas
        5 - Tempo de intervalo das doses (Remind me)
        6 - Outras funcionalidades em desenvolvimento..
        7 - TESTE DE ATUALIZACAO
        ''', reply_markup=reply_markup)
    return FIRST


def locais(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("D1", callback_data=str(DOSE1)),
            InlineKeyboardButton("D2", callback_data=str(DOSE2)),
            InlineKeyboardButton("D85+",
                                 callback_data=str(DOSER85)),
            InlineKeyboardButton(
                "PN", callback_data=str(PNOTURNO)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''Qual a dose você procura?

        D1 - Primeira dose
        D2 - Segunda dose
        D85+ - Dose de reforço +85
        PN - Postos Noturnos

        Home - Inicio
        Close - Fechar
        ''', reply_markup=reply_markup
    )
    return FIRST


def dose1(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(SEVEN)),
            InlineKeyboardButton("2", callback_data=str(SEVEN)),
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
        Primeira dose. Qual grupo você faz parte?
        
        1 - Tem entre 13 e 17 anos?
        (Também gestantes e puéperas a partir dessa idade)
        2 - Tem 18 anos ou mais?

        Home - Inicio
        Close - Fechar
        ''', reply_markup=reply_markup
    )
    return FIRST


def dose2(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(SEVEN)),
            InlineKeyboardButton("2", callback_data=str(SEVEN)),
            InlineKeyboardButton("3", callback_data=str(SEVEN)),
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''
        Segunda dose. Qual grupo você faz parte?
        
        1 - D2 ASTRAZENECA
        2 - D2 CORONAVAC
        3 - D2 PFIZER-BIONTECH

        Home - Inicio
        Close - Fechar
        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST


def doseR85(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''DOSE DE REFORÇO
        
        Funcionalidade em desenvolvimento''', reply_markup=reply_markup
    )
    return FIRST


def pnoturno(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''POSTOS NOTURNOS
        
        Funcionalidade em desenvolvimento''', reply_markup=reply_markup
    )
    return FIRST


def six(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''**************
        
        Funcionalidade em desenvolvimento''', reply_markup=reply_markup
    )
    return FIRST


def seven(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''***************
        
        Funcionalidade em desenvolvimento''', reply_markup=reply_markup
    )
    return FIRST


def mascaras(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''2 - Máscaras Recomendadas contra a Covid-19: guia mostra os melhores tipos e as combinações mais eficientes
        
        - Máscaras PFF2 (ou N95)
        - Máscaras KN95
        - Máscaras elastoméricas
        - Máscaras com válvula
        - Máscaras cirúrgicas ou de procedimentos
        - Máscaras de pano com 3 camadas (Apenas em ultimo caso de falta/emergencia)
        ''', reply_markup=reply_markup
    )
    return SECOND


def cuidados(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
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



def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()

    query.edit_message_text(text="Nos vemos na próxima consulta!")
    return ConversationHandler.END


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
                CallbackQueryHandler(dose1, pattern='^' + str(DOSE1) + '$'),
                CallbackQueryHandler(dose2, pattern='^' + str(DOSE2) + '$'),
                CallbackQueryHandler(
                    doseR85, pattern='^' + str(DOSER85) + '$'),
                CallbackQueryHandler(
                    pnoturno, pattern='^' + str(PNOTURNO) + '$'),
                CallbackQueryHandler(six, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(seven, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(mascaras, pattern='^' + str(MASK) + '$'),
                CallbackQueryHandler(cuidados, pattern='^' + str(CARE) + '$'),
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
