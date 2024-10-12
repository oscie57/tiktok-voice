# TikTok Text-to-speech API

## FOR DOCUMENTATION, VISIT THE [WIKI](https://github.com/oscie57/tiktok-voice/wiki)

This is a simple Python program that accesses the TikTok API and gives you an `.mp3` file with what it says in the specified voice.

If you are stuck and need assistance, please ask me in my [Discord server](https://discord.gg/ymb84qM54A) in [#tiktok-voice](https://discord.com/channels/804449200921509913/963871023252533288) (quickest response) or via the Issues tab.

If you like this project, feel free to support me via [Ko-Fi]([https://oscie.net/support](https://ko-fi.com/oscie))!

If you're a creator using this for a project, thank you! I'm glad my project can help with your own. All I ask is that you credit this repository in your README file.

If you're creating a project relating to a content farm (i.e. Reddit story readers, TikTok/Reels/YouTube Shorts generators), please do not use my project (or any other projects that use/are based off of this), nor any of the documentation included. **I do not support content farms.**

## Usage

To use this, you need Python 3.8+ and all of the required packages installed.

To install required packages, run `pip3 install playsound requests` or `pip3 install -r requirements.txt`

### Read from file
1. Make sure you have your text in plaintext. You can name it anything
2. Run `py main.py -v VOICE -f FILENAME.txt --session SESSION_ID` (see voices below)

There is no character limit, though only latin characters are supported.

### Read from argument
1. Run `py main.py -v VOICE -t TEXT -n FILENAME.mp3 --session SESSION_ID` (see voices below)

This has a 200 character limit, but you can have non-latin characters (as long as it has a TTS supported voice)

### Play from text
Optionally, if you want to listen to the file instead of saving to a file, you can use the `-p` argument to play directly and then delete. If you get error `263`, ignore it, it doesn't affect the program itself.

### Session ID
[Get session id](https://github.com/oscie57/tiktok-voice/wiki/Obtaining-SessionID)

## Voice Options

**Since the list has gotten quite large, I have moved it to [the wiki](https://github.com/oscie57/tiktok-voice/wiki/Voice-Codes)**

Languages Supported:
- Portuguese (Brazil)
- German
- English (Australia)
- English (United Kingdom)
- English (United States)
- English (Disney)
- Spanish
- Spanish (Mexico)
- French
- Indonesian
- Japanese
- Korean

## Samples

You can find samples of all the voices in [/samples/](https://github.com/oscie57/tiktok-voice/blob/main/samples/)

## Credits
- [Spotlight](https://twitter.com/xibwrangler) for giving me the idea for this program
- [Myself](https://oscie.net) for creating this
- [scanlime](https://twitter.com/scanlime) for giving the voice options
- [Komfudo](https://github.com/Komfudo/) for translating the sample text to German
- [Philemax](https://twitter.com/Philemax1) for translating the sample text to French
- [Ash](https://github.com/ashmonty) for adding command line arguments
- [BigJ64](https://github.com/BigJ64/tiktok-voice) for adding a play argument
