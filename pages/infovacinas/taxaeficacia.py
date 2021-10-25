def taxaefic(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(SEVEN)),
            InlineKeyboardButton("2", callback_data=str(SEVEN)),
            InlineKeyboardButton("3", callback_data=str(SEVEN)),
            InlineKeyboardButton("4", callback_data=str(SEVEN)),
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='''TAIXA DE EFICACIA DAS VACINAS
        
        1 - Vacina Oxford, AstraZeneca
        2 - Vacina CoronaVac
        3 - Vacina BioNTech, Pfizer
        4 - Vacina Sputnik V
        5 - Vacina Johnson & JohnsonS

        Funcionalidade em desenvolvimento''', reply_markup=reply_markup
    )
    return FIRST