"""
Twitch Cinema Listener Bot - Desktop Application for johnplayz1900
GUI application for managing the Twitch cinema bot
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from twitchio.ext import commands

# Load environment variables
load_dotenv()


class TwitchCinemaBot(commands.Bot):
    """Twitch bot for cinema listener"""
    
    def __init__(self, token, channel, status_callback=None, chat_callback=None):
        self.token = token
        self.channel = channel
        self.status_callback = status_callback
        self.chat_callback = chat_callback
        
        super().__init__(
            token=self.token,
            prefix='!',
            initial_channels=[self.channel]
        )

    async def event_ready(self):
        """Called when the bot is ready"""
        if self.status_callback:
            self.status_callback("Connected", "green")
        if self.chat_callback:
            self.chat_callback(f"✅ Bot connected as {self.nick}")

    async def event_message(self, message):
        """Handle all incoming messages"""
        if message.echo:
            return
        
        await self.handle_commands(message)
        
        if message.content and self.chat_callback:
            self.chat_callback(f"{message.author.name}: {message.content}")

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


class CinemaBotApp:
    """Main GUI Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Twitch Cinema Listener - johnplayz1900")
        self.root.geometry("800x600")
        self.root.configure(bg='#0e0e10')
        
        # Bot variables
        self.bot = None
        self.bot_thread = None
        self.bot_loop = None
        self.is_running = False
        
        # Create UI
        self.create_widgets()
        
        # Load saved settings
        self.load_settings()

    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#0e0e10', padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🎬 Twitch Cinema Listener Bot", 
            font=('Arial', 18, 'bold'),
            bg='#0e0e10',
            fg='#9146ff'
        )
        title_label.pack(pady=(0, 10))
        
        # Configuration Frame
        config_frame = tk.LabelFrame(
            main_frame,
            text="Configuration",
            font=('Arial', 10, 'bold'),
            bg='#18181b',
            fg='white',
            padx=10,
            pady=10
        )
        config_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Bot Username
        tk.Label(
            config_frame, 
            text="Bot Username:", 
            bg='#18181b', 
            fg='white',
            anchor='w'
        ).grid(row=0, column=0, sticky='w', pady=5)
        self.username_entry = tk.Entry(config_frame, width=30, bg='#1f1f23', fg='white', insertbackground='white')
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)
        self.username_entry.insert(0, 'johnplayz1900')
        
        # Channel Name
        tk.Label(
            config_frame, 
            text="Channel Name:", 
            bg='#18181b', 
            fg='white',
            anchor='w'
        ).grid(row=1, column=0, sticky='w', pady=5)
        self.channel_entry = tk.Entry(config_frame, width=30, bg='#1f1f23', fg='white', insertbackground='white')
        self.channel_entry.grid(row=1, column=1, pady=5, padx=5)
        self.channel_entry.insert(0, 'johnplayz1900')
        
        # OAuth Token
        tk.Label(
            config_frame, 
            text="OAuth Token:", 
            bg='#18181b', 
            fg='white',
            anchor='w'
        ).grid(row=2, column=0, sticky='w', pady=5)
        self.token_entry = tk.Entry(
            config_frame, 
            width=30, 
            bg='#1f1f23', 
            fg='white', 
            insertbackground='white',
            show='*'
        )
        self.token_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Load token from .env if exists
        env_token = os.getenv('OAUTH_TOKEN', '')
        if env_token:
            self.token_entry.insert(0, env_token)
        
        # Control Buttons Frame
        control_frame = tk.Frame(main_frame, bg='#0e0e10')
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.start_button = tk.Button(
            control_frame,
            text="▶ Start Bot",
            command=self.start_bot,
            bg='#00ad7c',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=5,
            cursor='hand2'
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(
            control_frame,
            text="⏹ Stop Bot",
            command=self.stop_bot,
            bg='#e91916',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=5,
            state=tk.DISABLED,
            cursor='hand2'
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Status Frame
        status_frame = tk.Frame(main_frame, bg='#0e0e10')
        status_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            status_frame,
            text="Status:",
            bg='#0e0e10',
            fg='white',
            font=('Arial', 10, 'bold')
        ).pack(side=tk.LEFT, padx=5)
        
        self.status_label = tk.Label(
            status_frame,
            text="Disconnected",
            bg='#0e0e10',
            fg='#e91916',
            font=('Arial', 10)
        )
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Chat Log Frame
        log_frame = tk.LabelFrame(
            main_frame,
            text="Chat Log",
            font=('Arial', 10, 'bold'),
            bg='#18181b',
            fg='white',
            padx=10,
            pady=10
        )
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.chat_log = scrolledtext.ScrolledText(
            log_frame,
            bg='#1f1f23',
            fg='#efeff1',
            font=('Consolas', 9),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_log.pack(fill=tk.BOTH, expand=True)
        
        # Add welcome message
        self.log_message("🎬 Twitch Cinema Listener Bot Ready!")
        self.log_message("Configure your settings above and click 'Start Bot' to begin.")
        
    def log_message(self, message):
        """Add a message to the chat log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, f"[{timestamp}] {message}\n")
        self.chat_log.see(tk.END)
        self.chat_log.config(state=tk.DISABLED)
        
    def update_status(self, status, color="red"):
        """Update status label"""
        self.status_label.config(text=status, fg=color)
        
    def chat_callback(self, message):
        """Callback for bot chat messages"""
        self.root.after(0, self.log_message, message)
        
    def status_callback(self, status, color):
        """Callback for bot status updates"""
        self.root.after(0, self.update_status, status, color)
        
    def load_settings(self):
        """Load settings from environment"""
        username = os.getenv('BOT_USERNAME', 'johnplayz1900')
        channel = os.getenv('CHANNEL', 'johnplayz1900')
        
        if self.username_entry.get() == 'johnplayz1900' and username != 'johnplayz1900':
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, username)
            
        if self.channel_entry.get() == 'johnplayz1900' and channel != 'johnplayz1900':
            self.channel_entry.delete(0, tk.END)
            self.channel_entry.insert(0, channel)
            
    def start_bot(self):
        """Start the bot"""
        token = self.token_entry.get().strip()
        channel = self.channel_entry.get().strip()
        
        if not token:
            messagebox.showerror("Error", "Please enter your OAuth Token!")
            return
            
        if not channel:
            messagebox.showerror("Error", "Please enter a channel name!")
            return
            
        if not token.startswith('oauth:'):
            token = f'oauth:{token}' if not token.startswith('oauth:') else token
        
        try:
            self.log_message(f"🔄 Starting bot for channel: {channel}")
            self.update_status("Connecting...", "yellow")
            
            # Create bot instance
            self.bot = TwitchCinemaBot(
                token=token,
                channel=channel,
                status_callback=self.status_callback,
                chat_callback=self.chat_callback
            )
            
            # Start bot in separate thread
            self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            self.bot_thread.start()
            
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.token_entry.config(state=tk.DISABLED)
            self.channel_entry.config(state=tk.DISABLED)
            self.username_entry.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start bot: {str(e)}")
            self.log_message(f"❌ Error: {str(e)}")
            self.update_status("Error", "red")
            
    def stop_bot(self):
        """Stop the bot"""
        self.log_message("🛑 Stopping bot...")
        self.is_running = False
        
        # Close bot connection if it exists
        if self.bot:
            try:
                if hasattr(self.bot, '_ws') and self.bot._ws:
                    asyncio.run_coroutine_threadsafe(self.bot._ws.close(), self.bot.loop)
            except:
                pass
        
        self.update_status("Disconnected", "red")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.token_entry.config(state=tk.NORMAL)
        self.channel_entry.config(state=tk.NORMAL)
        self.username_entry.config(state=tk.NORMAL)
        
        self.log_message("✅ Bot stopped")
        
    def run_bot(self):
        """Run the bot in a new event loop"""
        try:
            # twitchio's bot.run() handles the event loop internally
            self.bot.run()
        except Exception as e:
            self.log_message(f"❌ Bot error: {str(e)}")
            self.root.after(0, self.update_status, "Error", "red")
            self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.stop_button.config(state=tk.DISABLED))


if __name__ == '__main__':
    root = tk.Tk()
    app = CinemaBotApp(root)
    root.mainloop()
