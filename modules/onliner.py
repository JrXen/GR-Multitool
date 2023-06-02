import discord
import asyncio
from datetime import datetime

intents = discord.Intents.default()
intents.presences = True
intents.typing = False

tokens_file = 'config/tokens.txt'

async def set_activity(token):
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Connected using token: {token}")

        activity_name = input("Enter the activity name: ")
        start_time = datetime.now()

        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            elapsed_time = datetime.now() - start_time

            activity = discord.Activity(
                name=f"{activity_name} | Elapsed Time: {elapsed_time}",
                type=discord.ActivityType.playing,
                url="https://discord.gg/EA6JcYfXfa"
            )
            await client.change_presence(status=discord.Status.dnd, activity=activity)

            await asyncio.sleep(1)  

    await client.start(token, bot=False)

async def main():
    with open(tokens_file, 'r') as file:
        tokens = file.read().splitlines()

    tasks = []
    for token in tokens:
        tasks.append(asyncio.ensure_future(set_activity(token)))

    await asyncio.wait(tasks)

asyncio.run(main())
