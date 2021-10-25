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