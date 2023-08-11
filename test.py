from edamino import Bot

bot = Bot( , ,  )

@bot.ready("Bot is ready")
async def on_start(ctx):
    profile = await ctx.client.get_user_info(ctx.client.uid)
    print(profile)

@bot.event()
async def on_message(ctx):
    print(ctx.msg.content)

bot.start()

