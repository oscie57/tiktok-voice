import requests, base64, random, argparse, os

# https://twitter.com/scanlime/status/1512598559769702406

voices = [
    # DISNEY VOICES
    'en_us_ghostface',        # Ghost Face
    'en_us_chewbacca',        # Chewbacca
    'en_us_c3po',             # C3PO
    'en_us_stitch',           # Stitch
    'en_us_stormtrooper',     # Stormtrooper
    'en_us_rocket',           # Rocket

    # ENGLISH VOICES
    'en_au_001',              # English AU - Female
    'en_au_002',              # English AU - Male
    'en_uk_001',              # English UK - Male
    'en_us_002',              # English US - Female
    'en_us_006',              # English US - Male

    # OTHER LANGUAGES
    'fr_001',                 # France - Male 01
    'fr_002',                 # France - Male 02
    'de_001',                 # Germany - Female
    'de_002',                 # Germany - Male
    'jp_001',                 # Japan - Female 01
    'jp_003',                 # Japan - Female 02
    'es_002',                 # Spain - Male
]


def tts(text_speaker: str = "en_us_002", req_text: str = "TikTok Text To Speech", filename: str = 'voice.mp3'):

    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")

    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0"

    r = requests.post(url)

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]

    b64d = base64.b64decode(vstr)

    out = open(filename, "wb")
    out.write(b64d)
    out.close()

    print(f"\n{msg.capitalize()}")

def tts_batch(text_speaker: str = 'en_us_002', req_text: str = 'TikTok Text to Speech', filename: str = 'voice.mp3'):
    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")

    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0"

    r = requests.post(url)

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]

    b64d = base64.b64decode(vstr)

    out = open(filename, "wb")
    out.write(b64d)
    out.close()

    print(f"\n{msg.capitalize()}")

def batch_create():
    out = open('voice.mp3', 'wb')
    
    for item in os.listdir('./batch/'):
        filestuff = open('./batch/' + item, 'rb').read()
        out.write(filestuff)

    out.close()

def main():
    parser = argparse.ArgumentParser(description = "Simple Python script to interact with the TikTok TTS API")
    parser.add_argument("-v", "--voice", help = "the code of the desired voice")
    parser.add_argument("-t", "--text", help = "the text to be read")
    parser.add_argument("-f", "--file", help = "use this if you wanna use 'text.txt'")
    parser.add_argument("-n", "--name", help = "The name for the output file (.mp3)")
    args = parser.parse_args()

    text_speaker = args.voice or input("Voice: ")

    if args.file is not None:
        req_text = open(args.file, 'r').read()
    else:
        req_text = args.text or input("Text:  ")

    if text_speaker == "random":
        text_speaker = randomvoice()

    if args.name is not None:
        filename = args.name
    else:
        filename = 'voice.mp3'

    if args.file is not None:
        chunks, chunk_size = len(req_text), 200
        textlist = [ req_text[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

        amount = len(textlist) 

        os.makedirs('./batch/')

        for i, item in enumerate(textlist):
            tts_batch(text_speaker, item, f'./batch/{i}.mp3')
        
        batch_create()

        for item in os.listdir('./batch/'):
            os.remove('./batch/' + item)
        
        os.removedirs('./batch/')

        return

    tts(text_speaker, req_text, filename)


def randomvoice():
    count = random.randint(0, 15)
    text_speaker = voices[count]

    return text_speaker

def sampler():
    for item in voices:
        text_speaker = item
        print(item)
        req_text = 'TikTok Text To Speech Sample'
        tts(text_speaker, req_text)

main()