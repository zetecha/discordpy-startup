from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
 #ここまで立ち上げ準備、いじるの厳禁で
    
#参考
　#@client.event #イベント受信に必要な構文
　#async def on_イベントに対応する関数(受け取る引数):
　　#以下よりasyncの活用例
　　#async def on_ready():　#参加したとき
　　#async def on_message(message):　#メッセージを受信したとき

@bot.event 
async def on_command_error(ctx, error):　
    
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.author.bot:　#メッセージ送信者がBotだった場合
        return　#戻る
    if message.content == '/wakeup':　    # 「/wakeup」と発言したら
        await message.channel.send('起きろ！！') #「起きろ！！」と発言


@bot.command()
async def ping(ctx):　#コマンドとして「ping」を入力されたとき
    await ctx.send('pong')　#「pong」と発言


bot.run(token) #実行
