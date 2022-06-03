import requests, base64, random, argparse, os, playsound, time

# https://twitter.com/scanlime/status/1512598559769702406

voices = [
    # DISNEY VOICES
    'en_us_ghostface',            # Ghost Face
    'en_us_chewbacca',            # Chewbacca
    'en_us_c3po',                 # C3PO
    'en_us_stitch',               # Stitch
    'en_us_stormtrooper',         # Stormtrooper
    'en_us_rocket',               # Rocket

    # ENGLISH VOICES
    'en_au_001',                  # English AU - Female
    'en_au_002',                  # English AU - Male
    'en_uk_001',                  # English UK - Male 1
    'en_uk_003',                  # English UK - Male 2
    'en_us_001',                  # English US - Female (Int. 1)
    'en_us_002',                  # English US - Female (Int. 2)
    'en_us_006',                  # English US - Male 1
    'en_us_007',                  # English US - Male 2
    'en_us_009',                  # English US - Male 3
    'en_us_010',                  # English US - Male 4

    # EUROPE VOICES
    'fr_001',                     # French - Male 1
    'fr_002',                     # French - Male 2
    'de_001',                     # German - Female
    'de_002',                     # German - Male
    'es_002',                     # Spanish - Male

    # AMERICA VOICES
    'es_mx_002',                  # Spanish MX - Male
    'br_001',                     # Portuguese BR - Female 1
    'br_003',                     # Portuguese BR - Female 2
    'br_004',                     # Portuguese BR - Female 3
    'br_005',                     # Portuguese BR - Male

    # ASIA VOICES
    'id_001',                     # Indonesian - Female
    'jp_001',                     # Japanese - Female 1
    'jp_003',                     # Japanese - Female 2
    'jp_005',                     # Japanese - Female 3
    'jp_006',                     # Japanese - Male
    'kr_002',                     # Korean - Male 1
    'kr_003',                     # Korean - Female
    'kr_004',                     # Korean - Male 2
    
    # NARRATOR
    'en_male_narration'
    
    # SINGING VOICES
    'en_female_f08_salut_damour'  # Alto
    'en_male_m03_lobby'           # Tenor
]


def tts(text_speaker: str = "en_us_002", req_text: str = "TikTok Text To Speech", filename: str = 'voice.mp3', play: bool = False):

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

    if play is True:
        playsound.playsound(filename)
        os.remove(filename)

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
    parser.add_argument("-p", "--play", action='store_true', help = "use this if you want to play your output")
    args = parser.parse_args()

    text_speaker = args.voice

    if args.file is not None:
        req_text = open(args.file, 'r', errors='ignore', encoding='utf-8').read()
    else:
        if args.text == None:
            req_text = 'TikTok Text To Speech'
            print('You need to have one form of text! (See README.md)')
        else:
            req_text = args.text

    if args.play is not None:
        play = args.play

    if args.voice == None:
        text_speaker = 'en_us_002'
        print('You need to have a voice! (See README.md)')

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

    tts(text_speaker, req_text, filename, play)


def randomvoice():
    count = random.randint(0, 15)
    text_speaker = voices[count]

    return text_speaker

def sampler():
    for item in voices:
        text_speaker = item
        filename = item
        print(item)
        req_text = 'TikTok Text To Speech Sample'
        tts(text_speaker, req_text, filename)

if __name__ == "__main__":
    main()
