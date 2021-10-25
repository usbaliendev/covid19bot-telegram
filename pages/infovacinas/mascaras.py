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