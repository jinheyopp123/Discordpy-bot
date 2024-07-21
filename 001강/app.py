import discord
from discord.ext import commands
import sqlite3

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

conn = sqlite3.connect('data.db')
