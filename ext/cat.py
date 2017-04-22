import requests
from discord.ext import commands
from discord.ext.commands import Bot


class Cat:
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(
        description='Get a random cat.'
    )
    async def cat(self):
        r = requests.get('http://random.cat/meow')
        if r.status_code == 200:
            cat = r.json()['file']
            await self.bot.say(cat)


def setup(bot):
    bot.add_cog(Cat(bot))
