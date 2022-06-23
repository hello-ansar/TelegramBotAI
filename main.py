import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Тезис на консоле
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
#
#
# # Определение обработчиков команд
# # Это start, help, echo
# def start(update: Update, context: CallbackContext) -> None:
#     """При команде /start отправляется приветственное сообщение."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Привет {user.mention_markdown_v2()}\!',
#         reply_markup=ForceReply(selective=True),
#     )
#
#
# def help_command(update: Update, context: CallbackContext) -> None:
#     """При команде /help отправляется сообщение."""
#     update.message.reply_text('Help!')
#
#
def echo(update: Update, context: CallbackContext) -> None:
    """Повтор сообщения пользователя."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Начало бота."""
    # Токен бота
    updater = Updater(token='5130381939:AAGa371mHApKhOZZi213hAv08q5KWfhUKV4')

    # Диспетчер должен зарегистрировать обработчики
    dispatcher = updater.dispatcher

    # # По разным командам - ответ идет в Telegram
    # dispatcher.add_handler(CommandHandler("start", start))
    # dispatcher.add_handler(CommandHandler("help", help_command))

    # Повторение сообщении
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print(MessageHandler(Filters.text & ~Filters.command, echo))
    # Старт бота
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

