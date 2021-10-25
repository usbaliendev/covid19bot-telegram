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