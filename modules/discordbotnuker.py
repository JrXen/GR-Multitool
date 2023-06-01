import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command(name='start')
async def start(ctx):
    global stop_flag  # Use the global stop_flag variable

    await ctx.send("Please enter the base name for the new channels.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await bot.wait_for('message', timeout=60.0, check=check)
        base_name = message.content

        await ctx.send("How many channels would you like to create?")

        try:
            message = await bot.wait_for('message', timeout=60.0, check=check)
            num_channels = int(message.content)

            guild = ctx.guild

            # Delete existing channels (excluding the command invocation channel)
            existing_channels = guild.text_channels
            channels_to_delete = [
                channel for channel in existing_channels if channel != ctx.channel and channel.name.startswith(base_name)
            ]
            await asyncio.gather(*[channel.delete() for channel in channels_to_delete])

            await ctx.send("Please enter the messages you want to send (separated by new lines).")
            message = await bot.wait_for('message', timeout=60.0, check=check)
            messages = message.content.split('\n')

            stop_flag = False  # Reset the stop_flag
            await send_messages_to_channels(guild, base_name, num_channels, messages)

            await ctx.send(f"{num_channels} new channels have been created and messages are being sent!")
        except ValueError:
            await ctx.send("Invalid input for the number of channels. Operation cancelled.")
    except asyncio.TimeoutError:
        await ctx.send("No base name provided. Operation cancelled.")

async def send_messages_to_channels(guild, base_name, num_channels, messages):
    global stop_flag, running_tasks  # Use the global stop_flag and running_tasks variables

    tasks = []

    for i in range(1, num_channels + 1):
        if stop_flag:  # Check the stop_flag before creating each channel
            break

        channel_name = f"{base_name}-{i}"
        channel = await guild.create_text_channel(channel_name)
        task = asyncio.create_task(send_messages_to_channel(channel, messages))
        tasks.append(task)

    running_tasks.extend(tasks)  # Add the tasks to the running tasks list
    await asyncio.gather(*tasks)

async def send_messages_to_channel(channel, messages):
    global stop_flag  # Use the global stop_flag variable

    while not stop_flag:
        for message in messages:
            await asyncio.sleep(0)  # Yield control to prevent blocking
            await channel.send(message)


@bot.command(name='dc')
async def delete_channels(ctx):
    guild = ctx.guild
    existing_channels = guild.text_channels

    # Filter channels to exclude the command invocation channel
    channels_to_delete = [channel for channel in existing_channels if channel != ctx.channel]

    # Delete channels concurrently
    await asyncio.gather(*[channel.delete() for channel in channels_to_delete])

    await ctx.send("All existing channels, except the command invocation channel, have been deleted.")

bot_token = input("Enter your bot token: ")
bot.run(bot_token)
