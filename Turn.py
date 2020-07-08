import discord
#from random import choice
import pw.password as pw
client = discord.Client()
import random

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    member = message.guild.members
    members = []

    for i in member:
        if(str(i.bot)=="False"):
            members.append(i)
                    
    command = message.content
    user_id = str(message.author.id)

    if message.author.bot:
        return None

    if command.startswith("!돌려돌려돌림판"):
        if(message.guild):                 
            #c_m = choice(members)     
            num = [e.strip() for e in command.split('!돌려돌려돌림판')][1]
            
            if(num == ""):
                num = 1
            elif(num.isdigit() == False):
                num =1
            elif(int(num) >= len(members)):
                num = len(members)

            
            
            out = random.sample(members,int(num))
            await message.channel.send("```당첨자```")
            for i in range(0,len(out)):
                await message.channel.send(f"\n @{out[i].nick} ({out[i]})")
            

        else:
            await message.author.send("개인 메시지에서는 지원하지 않습니다.")
    

client.run(pw.token())
