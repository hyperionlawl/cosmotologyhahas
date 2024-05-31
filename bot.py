import discord
from discord.ext import commands

# Define your bot's prefix
bot_prefix = "!"

# Initialize the bot with the specified prefix
bot = commands.Bot(command_prefix=bot_prefix)

# Event to print a message in the console when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to kick a member
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')
    else:
        await ctx.send("You don't have permission to use this command.")

# Command to ban a member
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')
    else:
        await ctx.send("You don't have permission to use this command.")

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')
