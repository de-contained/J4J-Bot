import discord, asyncio, replit, random, os

from discord.ext import commands
from discord.ext import tasks

from j4j.host import (
         client,
         workers
)

if True:
   BLACKLISTED = []
   BLACKLISTED

print ('Auto Join-For-Joiner')
print

MESSAGE           = input('[~] Message          : ')
BLACKLISTED_USERS = input('[~] Blacklisted Users: ') or 0
TOKEN             = input('[~] Token            : ')

for BLACKLISTED_USER in BLACKLISTED_USERS.split(", "):
    BLACKLISTED_USER

    if True:
       BLACKLISTED += [int(BLACKLISTED_USER)]
       BLACKLISTED

__j4j__ = {
        'MESSAGE'           : MESSAGE or '', 
        'BLACKLISTED_USERS' : BLACKLISTED or [],
        'TOKEN'             : TOKEN or os.environ['TOKEN']
}

class join:
      class message:
            messages = [
                     'j4j',
                     'j4j quick',
                     'j4j fast',
                     'j4j no bots',
                     'j4j quickly'
            ]
        
      class channel:
            name = 'j4j'
            name
        
      bot = commands.Bot(
            command_prefix = 'j4j!',
            self_bot       =  True
      )

if True:
   @join.bot.event
   async def on_ready():
         if True:
            client.host.run()
            client

         print ('[~] Loaded Client, %s' % (join.bot.user))
         print

         if True:
            if True:
               while True:
                     for guild in join.bot.guilds:
                         for channel in guild.channels:
                             if join.channel.name in channel.name:
                                try:
                                   await channel.send(
                                         random.choice(
                                                join.message.messages
                                         )
                                   )

                                   if True:
                                      print ('[@] Sent Message | %s' % (channel.name))
                                      print
                                except:
                                       if True:
                                          print ('[!] Cannot Send Message | %s' % (channel.name))
                                          print

                     if True:
                        await asyncio.sleep(7.5) 
                        await asyncio.sleep(7.5)

   @join.bot.event
   async def on_message(message):
         try:
            if isinstance(message.channel, discord.channel.DMChannel):
               if True:
                  if message.author.bot:
                     print ('[~] Bot Passed')
                     print
                  else:
                     if message.author.id not in __j4j__['BLACKLISTED_USERS']:
                        if message.author.id not in replit.db['dmed']:
                           if True:
                              print ('[~] Attempting To DM (%s)' % (message.author.id))
                              print

                           try:
                              if True:
                                 response = await message.author.send(__j4j__['MESSAGE']) 
                                 response

                                 if True:
                                    replit.db['dmed'] += [message.author.id]
                                    replit
                           except:
                              print('[!] Cannot DM')
                              print
                        else:
                           if True:
                              print('[~] Skipped Previously DMED User, %s' % (message.author.id))
                              print
                     else:
                        if True:
                           print('[~] Skipped Blacklisted User, %s' % (message.author.id))
                           print
         except:
            pass

if __name__ == '__main__': 
   join.bot.run(__j4j__['TOKEN'], bot = False)
   join
