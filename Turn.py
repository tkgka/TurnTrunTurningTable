import discord
from random import choice
import pw.password as pw
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    command = message.content
    user_id = str(message.author.id)

    if message.author.bot:
        return None

    if command.startswith("!돌려돌려돌림판"):
        if(message.guild):
            member = message.guild.members
            c_m = choice(member)     
            num = [e.strip() for e in command.split('!돌려돌려돌림판')][1]
            if(num == ""):
                num = 1
            elif(int(num) >= len(member)):
                num = len(member)
            print(int(num))
            print(member[0].bot)

            while(1):
                c_m = choice(member)
                if(str(c_m.bot) == "False"):
                    await message.channel.send(f"```축 당첨 \n{c_m.name}#{c_m.discriminator}```")
                    break



        else:
            await message.author.send("개인 메시지에서는 지원하지 않습니다.")
    

client.run(pw.token())
