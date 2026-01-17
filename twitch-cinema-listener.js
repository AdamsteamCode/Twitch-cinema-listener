// This code listens to Twitch chat for "Cinema" from Adamsteamguy and plays a sound.

const tmi = require('tmi.js');
const { exec } = require('child_process');
const path = require('path');

// Configuration
const channel = 'adamsteamguy'; // Twitch channel to listen to
const targetUsername = 'adamsteamguy'; // Case-insensitive username to listen for
const targetMessage = 'cinema'; // Case-insensitive message to listen for

// Sound file path (you can change this to your sound file)
// For Windows, you can use a .wav or .mp3 file
const soundFile = path.join(__dirname, 'sound.mp3'); // Change this to your sound file

// Play sound function - works with .wav and .mp3 files on Windows
function playSound() {
    const fs = require('fs');
    
    if (fs.existsSync(soundFile)) {
        const ext = path.extname(soundFile).toLowerCase();
        let command;
        
        if (ext === '.wav') {
            // Use SoundPlayer for .wav files (simpler, faster)
            command = `powershell -c (New-Object Media.SoundPlayer "${soundFile}").PlaySync()`;
        } else {
            // Use PowerShell to play .mp3 and other audio formats
            const escapedPath = soundFile.replace(/'/g, "''").replace(/"/g, '""');
            command = `powershell -c $player = New-Object -ComObject WMPlayer.OCX; $player.URL = "${escapedPath}"; Start-Sleep -Seconds 2`;
        }
        
        exec(command, (error) => {
            if (error) {
                console.log('Error playing sound file, using system beep instead');
                console.log('\x07'); // System beep
            }
        });
    } else {
        // System beep as fallback
        console.log('\x07');
        console.log('💥 Cinema detected from Adamsteamguy! Playing sound...');
    }
}

// Define Twitch client options
// Note: For public channels, you can connect anonymously (no identity needed)
// Uncomment the identity section below if you need authentication
const opts = {
    // identity: {
    //     username: 'your_bot_username', // Optional: replace with your Twitch bot username
    //     password: 'oauth:your_oauth_token' // Optional: get this from https://twitchtokengenerator.com/
    // },
    channels: [
        channel
    ]
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Called every time a message comes in
function onMessageHandler(target, context, msg, self) {
    if (self) { return; } // Ignore messages from the bot

    const username = context.username.toLowerCase();
    const message = msg.trim().toLowerCase();

    // Check if the message is from the target user and contains the target word
    if (username === targetUsername.toLowerCase() && message.includes(targetMessage)) {
        console.log(`\n🎬 Cinema detected from ${context.username}!`);
        console.log(`Message: "${msg}"`);
        playSound();
    }
}

// Called every time the bot connects to Twitch chat
function onConnectedHandler(addr, port) {
    console.log(`✅ Connected to Twitch chat at ${addr}:${port}`);
    console.log(`👂 Listening for "${targetMessage}" from "${targetUsername}" in channel #${channel}`);
}

// Connect to Twitch
console.log('🚀 Starting Twitch chat listener...');
client.connect().catch((error) => {
    console.error('❌ Error connecting to Twitch:', error);
    console.log('\n📝 Troubleshooting:');
    console.log('   - Make sure you have internet connection');
    console.log('   - If authentication is needed, uncomment the identity section in opts');
    console.log('   - Get an OAuth token from https://twitchtokengenerator.com/ if needed');
});
