# ======== اینجا توکن ربات تلگرام را بگذار ========
TOKEN = ""
# ===============================================

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from rubpy import Client

users = {}

# شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users[update.effective_user.id] = {"step": "phone"}
    await update.message.reply_text("📱 شماره تلفن را ارسال کنید")

# دریافت پیام‌ها
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    text = update.message.text

    if uid not in users:
        return

    step = users[uid]["step"]

    # مرحله شماره
    if step == "phone":
        phone = text.strip()
        client = Client(f"session_{uid}")
        await client.connect()

        sent = await client.send_code(phone)

        users[uid]["client"] = client
        users[uid]["phone"] = phone
        users[uid]["hash"] = sent.phone_code_hash
        users[uid]["step"] = "code"

        await update.message.reply_text("📩 کد تایید ارسال شد، کد را بفرستید")

    # مرحله کد
    elif step == "code":
        code = text.strip()
        client = users[uid]["client"]

        try:
            await client.sign_in(
                users[uid]["phone"],
                users[uid]["hash"],
                code
            )
            await client.save_session()

            users[uid]["step"] = "done"
            await update.message.reply_text("✅ ورود موفق انجام شد")

        except Exception as e:
            await update.message.reply_text(f"❌ خطا: {e}")

# اجرای ربات
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

    print("Bot running ...")
    app.run_polling()

if __name__ == "__main__":
    main()
