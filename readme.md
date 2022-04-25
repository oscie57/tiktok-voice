# TikTok Text-to-speech API

This is a simple Python program that accesses the TikTok API and gives you an `.mp3` file with what it says in the specified voice.

## Usage

To use this, you need Python 3.8+ and all of the required packages installed.

### Read from file
1. Make sure you have your text in plaintext. You can name it anything
2. Run `py main.py -v VOICE -f FILENAME.txt` (see voices below)

There is no character limit, though only latin characters are supported.

### Read from argument
1. Run `py main.py -v VOICE -t TEXT -n FILENAME.mp3` (see voices below)

This has a 200 character limit, but you can have non-latin characters (as long as it has a TTS supported voice)

## Need help?
If you are stuck and are unsure what to do, please ask me in my [Discord server](https://discord.gg/ymb84qM54A) in [#tiktok-voice](https://discord.com/channels/804449200921509913/963871023252533288) (quickest response) or via the Issues tab.

## Voice Options

| Language                          | Voice Code           |
| :-------------------------------- | :------------------- |
| Ghost Face (Disney)               | `en_us_ghostface`    |
| Chewbacca (Disney)                | `en_us_chewbacca`    |
| C3PO (Disney)                     | `en_us_c3po`         |
| Stitch (Disney)                   | `en_us_stitch`       |
| Stormtrooper (Disney)             | `en_us_stormtrooper` |
| Rocket (Disney)                   | `en_us_rocket`       |
|                                   |                      |
| English AU - Female               | `en_au_001`          |
| English AU - Male                 | `en_au_002`          |
| English UK - Male 1               | `en_uk_001`          |
| English UK - Male 2               | `en_uk_003`          |
| English US - Female 1             | `en_us_001`          |
| English US - Female 1 (duplicate) | `en_us_002`          |
| English US - Male 1               | `en_us_006`          |
| English US - Male 2               | `en_us_007`          |
| English US - Male 3               | `en_us_009`          |
| English US - Male 4               | `en_us_010`          |
|                                   |                      |
| French - Male 1                   | `fr_001`             |
| French - Male 2                   | `fr_002`             |
| German - Female                   | `de_001`             |
| German - Male                     | `de_002`             |
| Indonesian - Female               | `id_001`             |
| Japanese - Female 1               | `jp_001`             |
| Japanese - Female 2               | `jp_003`             |
| Japanese - Female 3               | `jp_005`             |
| Japanese - Male                   | `jp_006`             |
| Korean - Male 1                   | `kr_002`             |
| Korean - Female                   | `kr_003`             |
| Korean - Male 2                   | `kr_004`             |
| Spanish - Male                    | `es_002`             |
| Spanish MX - Male                 | `es_mx_002`          |

## Samples

You can find samples of all the voices in [/samples/](https://github.com/oscie57/tiktok-voice/blob/main/samples/)

## Credits
- [Spotlight](https://twitter.com/xibwrangler) for giving me the idea for this program
- [Myself](https://oscie.net) for creating this
- [scanlime](https://twitter.com/scanlime) for giving the voice options
- [Komfudo](https://github.com/Komfudo/) for translating the sample text to German
- [Philemax](https://twitter.com/Philemax1) for translating the sample text to French
- [Ash](https://github.com/ashmonty) for adding command line arguments
