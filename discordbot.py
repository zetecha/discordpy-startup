from discord.ext import commands
import os
import traceback
CHANNEL_ID = 810883304790163456
SERVER_ID = 789462551917363200
client = discord.Client() 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

async def reply(message):
 reply = f'{message.author.mention} が通話に参加したよ！'
 await message.channel.send(reply)
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@client.event 
async def on_voice_state_update(before, after): 
        if after.server.id == SERVER_ID: 
        nowtime = datetime.datetime.utcnow() 
        nowtime = nowtime + datetime.timedelta(hours=9) 
        nowtime = nowtime.strftime("%m/%d-%H:%M") 
        vcchannel = client.get_channel('通知させたいテキストチャンネルid') 
 
        if(before.voice_channel is None): 
            jointext=nowtime + "に　"+ after.name + "　が　"+ after.voice_channel.name + " に参加しました。" 
            await client.send_message(vcchannel, jointext) 
        elif(after.voice_channel is None): 
            outtext=nowtime + "に　"+ before.name + "　が　"+ before.voice_channel.name + " から退出しました。" 
            await client.send_message(vcchannel, outtext) 

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
client.run(token) 
