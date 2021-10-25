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
            InlineKeyboardButton("outro", callback_data=str(SEVEN)),
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