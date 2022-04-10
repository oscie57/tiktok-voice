import requests, os, base64, time, json, string, random

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
]


def tts(text_speaker: str = "en_us_002", req_text: str = "TikTok Text To Speech"):

    req_text = req_text.replace(" ", "+")

    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0"

    r = requests.post(url)

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]

    b64d = base64.b64decode(vstr)

    out = open(f"voice.mp3", "wb")
    out.write(b64d)
    out.close()

    print(f"\n{msg.capitalize()}")


def main():
    text_speaker = input("Voice: ")
    req_text = input("Text:  ")

    if text_speaker == "random":
        text_speaker = randomvoice()

    tts(text_speaker, req_text)


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