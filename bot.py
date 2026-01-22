"""
Twitch Cinema Listener Bot for johnplayz1900
Listens to Twitch chat and handles cinema/movie-related commands
"""

import os
from dotenv import load_dotenv
from twitchio.ext import commands

# Load environment variables
load_dotenv()


class TwitchCinemaBot(commands.Bot):
    def __init__(self):
        # Bot configuration
        self.bot_username = os.getenv('BOT_USERNAME', 'johnplayz1900')
        self.token = os.getenv('OAUTH_TOKEN')
        self.channel = os.getenv('CHANNEL', 'johnplayz1900')
        
        super().__init__(
            token=self.token,
            prefix='!',
            initial_channels=[self.channel]
        )
        
        print(f"🎬 Twitch Cinema Listener Bot initialized for {self.channel}")

    async def event_ready(self):
        """Called when the bot is ready"""
        print(f'✅ Logged in as {self.nick}')
        print(f'📺 Connected to channel: #{self.channel}')

    async def event_message(self, message):
        """Handle all incoming messages"""
        # Ignore messages from the bot itself
        if message.echo:
            return
        
        # Process commands
        await self.handle_commands(message)
        
        # Log chat messages (optional)
        if message.content:
            print(f'💬 {message.author.name}: {message.content}')

    @commands.command(name='cinema')
    async def cinema_command(self, ctx: commands.Context):
        """Display cinema information"""
        await ctx.send('🎬 Welcome to the Cinema! Type !movies to see available movies, or !nowplaying to see what\'s currently showing!')

    @commands.command(name='movies')
    async def movies_command(self, ctx: commands.Context):
        """List available movies"""
        await ctx.send('🎥 Available movies: Use !request [movie name] to request a movie! (Example: !request The Matrix)')

    @commands.command(name='request')
    async def request_command(self, ctx: commands.Context, *, movie_name: str = None):
        """Request a movie"""
        if not movie_name:
            await ctx.send('❌ Please specify a movie name! Usage: !request [movie name]')
            return
        
        await ctx.send(f'🎬 {ctx.author.name} requested: {movie_name} - Request received!')

    @commands.command(name='nowplaying')
    async def nowplaying_command(self, ctx: commands.Context):
        """Show what's currently playing"""
        await ctx.send('🎬 Currently playing: Welcome to Twitch Cinema! 🎥✨')

    @commands.command(name='schedule')
    async def schedule_command(self, ctx: commands.Context):
        """Show cinema schedule"""
        await ctx.send('📅 Cinema Schedule: Movies play continuously! Check back for updates! 🎬')

    @commands.command(name='help')
    async def help_command(self, ctx: commands.Context):
        """Display help information"""
        help_text = (
            '🎬 Cinema Commands: '
            '!cinema - Cinema info | '
            '!movies - List movies | '
            '!request [movie] - Request a movie | '
            '!nowplaying - Current movie | '
            '!schedule - Show schedule'
        )
        await ctx.send(help_text)

    @commands.command(name='hello')
    async def hello_command(self, ctx: commands.Context):
        """Greet the user"""
        await ctx.send(f'👋 Hello {ctx.author.name}! Welcome to the Twitch Cinema! 🎬')


if __name__ == '__main__':
    bot = TwitchCinemaBot()
    try:
        bot.run()
    except KeyboardInterrupt:
        print('\n👋 Bot shutting down...')
    except Exception as e:
        print(f'❌ Error: {e}')
