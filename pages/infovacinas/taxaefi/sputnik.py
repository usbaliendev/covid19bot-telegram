def sputnik (update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            #Botoes de navegação padrao, SUPER ESSENCIAIS, adicionar outros botoes acima
            InlineKeyboardButton("Voltar", callback_data=str(LOC)),
            InlineKeyboardButton("Home", callback_data=str(START)),
            InlineKeyboardButton("Close", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #Aqui se edita o output da caixa de msg
    query.edit_message_text(
        text='''
        Vacina Sputnik V
        Informaçõpes e taixa de eficacia

        Funcionalidade em desenvolvimento..
        ''', reply_markup=reply_markup
    )
    return FIRST