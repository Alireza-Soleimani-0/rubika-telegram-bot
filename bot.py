from rubpy import Client

sessions = {}

async def start(message):
    user_id = message.author_guid
    sessions[user_id] = {"step": "phone"}
    await message.reply("📱 شماره تلفن را ارسال کنید\nمثال: 09123456789")


async def handler(message):
    user_id = message.author_guid

    if user_id not in sessions:
        return

    step = sessions[user_id]["step"]

    # مرحله دریافت شماره
    if step == "phone":
        phone = message.text.strip()
        sessions[user_id]["phone"] = phone

        client = Client(phone_number=phone)
        await client.connect()

        sent = await client.send_code(phone)

        sessions[user_id]["client"] = client
        sessions[user_id]["phone_code_hash"] = sent.phone_code_hash
        sessions[user_id]["step"] = "code"

        await message.reply("📩 کد تایید ارسال شد، کد را بفرستید:")

    # مرحله دریافت کد
    elif step == "code":
        code = message.text.strip()

        client = sessions[user_id]["client"]
        phone = sessions[user_id]["phone"]
        hash_ = sessions[user_id]["phone_code_hash"]

        try:
            await client.sign_in(phone, hash_, code)

            # ذخیره سشن
            await client.save_session()

            sessions[user_id]["step"] = "done"
            await message.reply("✅ لاگین انجام شد")

        except Exception as e:
            await message.reply(f"❌ خطا در لاگین: {e}")
