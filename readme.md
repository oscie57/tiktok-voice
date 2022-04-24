# TikTok Text-to-speech API

This is a simple Python program that accesses the TikTok API and gives you an `.mp3` file with what it says in the specified voice.

## Usage

To use this, you need Python 3.8+ and all of the required packages installed.

### Read from file
1. Make sure you have your text in plaintext. You can name it anything
2. Run `py main.py -v VOICE -f FILENAME.txt` (see voices below)

There is no character limit.

### Read from text
1. Run `py main.py -v VOICE -t TEXT` (see voices below)

This has a 200 character limit!

## Need help?
If you are stuck and are unsure what to do, please ask me in my [Discord server](https://discord.gg/ymb84qM54A) in [#tiktok-voice](https://discord.com/channels/804449200921509913/963871023252533288) (quickest response) or via the Issues tab.

## Voice Options

| Language              | Voice Code           |
| :-------------------- | :------------------- |
| Ghost Face (Disney)   | `en_us_ghostface`    |
| Chewbacca (Disney)    | `en_us_chewbacca`    |
| C3PO (Disney)         | `en_us_c3po`         |
| Stitch (Disney)       | `en_us_stitch`       |
| Stormtrooper (Disney) | `en_us_stormtrooper` |
| Rocket (Disney)       | `en_us_rocket`       |
|                       |                      |
| English AU - Female   | `en_au_001`          |
| English AU - Male     | `en_au_002`          |
| English UK - Male     | `en_uk_002`          |
| English US - Female   | `en_us_002`          |
| English US - Male     | `en_us_006`          |
|                       |                      |
| French - Male 1       | `fr_001`             |
| French - Male 2       | `fr_002`             |
| German - Female       | `de_001`             |
| German - Male         | `de_002`             |
| Japanese - Female 1   | `jp_001`             |
| Japanese - Female 2   | `jp_003`             |
| Spanish - Male        | `es_002`             |


## Samples

You can find samples of all the voices in [/samples/](https://github.com/oscie57/tiktok-voice/blob/main/samples/)

## Credits
- [Spotlight](https://twitter.com/xibwrangler) for giving me the idea for this program
- [Myself](https://oscie.net) for creating this
- [scanlime](https://twitter.com/scanlime) for giving the voice options
- [Komfudo](https://github.com/Komfudo/) for translating the sample text to German
- [Philemax](https://twitter.com/Philemax1) for translating the sample text to French
- [Ash](https://github.com/ashmonty) for adding command line arguments
