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