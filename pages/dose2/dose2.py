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
        ''', reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST