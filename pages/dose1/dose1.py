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
        ''', reply_markup=reply_markup
    )
    return FIRST