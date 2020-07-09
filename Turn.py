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
    if(message.guild):
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
                         
                #c_m = choice(members)     
                num = [e.strip() for e in command.split('!돌려돌려돌림판')][1]
            
                if(num == ""):
                    num = 1
                elif(num.isdigit() == False):
                    num =1
                elif(int(num) >= len(members)):
                    num = len(members)

            
            
                out = random.sample(members,int(num))
                await message.channel.send("```당첨자\n```")
                k=""
                for i in range(0,len(out)):
                #await message.channel.send(f"\n <@{out[i].id}> ({out[i]})")
                    k+=f"<@{out[i].id}> ({out[i]})\n"
                await message.channel.send(f"{k}")       
        
        if command.startswith("!help"):
            await message.channel.send("```'!돌려돌려돌림판' 으로 작동시킬수있습니다. \n 뒤에 붙인 숫자만큼 사람을 뽑습니다.```")

    else:
        await message.author.send("개인 메시지에서는 지원하지 않습니다.\n```'!돌려돌려돌림판' 으로 작동시킬수있습니다. \n 뒤에 붙인 숫자만큼 사람을 뽑습니다.```")
    

client.run(pw.token())
