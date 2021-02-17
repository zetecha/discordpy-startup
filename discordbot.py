from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
 
@bot.event 
async def on_command_error(ctx, error):
#わかんね
    
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

#@client.event
#async def on_message(message):
#    if message.author.bot:　#メッセージ送信者がBotだった場合(条件の絞り込みの為先に書く)
#        return　#戻る
#    if message.content == '/wakeup':　    # 「/wakeup」と発言したら
#        await message.channel.send('起きろ！！') #「起きろ！！」と発言


@bot.command()
async def ping(ctx):
#コマンドとして「ping」を入力されたとき?わかんね
    await ctx.send('pong')
#「pong」と発言(テキスト形式で)


bot.run(token)
#実行
