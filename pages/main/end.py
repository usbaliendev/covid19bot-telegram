def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()

    query.edit_message_text(text="Nos vemos na próxima consulta!")
    return ConversationHandler.END