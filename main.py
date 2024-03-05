import requests, base64, random, argparse, os, playsound, time, re, textwrap
from constants import voices

API_BASE_URL = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/"
USER_AGENT = f"com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)"


def tts(session_id: str, text_speaker: str = "en_us_002", req_text: str = "TikTok Text To Speech",
        filename: str = 'voice.mp3', play: bool = False):
    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")
    req_text = req_text.replace("ä", "ae")
    req_text = req_text.replace("ö", "oe")
    req_text = req_text.replace("ü", "ue")
    req_text = req_text.replace("ß", "ss")

    r = requests.post(
        f"{API_BASE_URL}?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0&aid=1233",
        headers={
            'User-Agent': USER_AGENT,
            'Cookie': f'sessionid={session_id}'
        }
    )

    if r.json()["message"] == "Couldn't load speech. Try again.":
        output_data = {"status": "Session ID is invalid", "status_code": 5}
        print(output_data)
        return output_data

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]
    scode = [r.json()["status_code"]][0]
    log = [r.json()["extra"]["log_id"]][0]

    dur = [r.json()["data"]["duration"]][0]
    spkr = [r.json()["data"]["speaker"]][0]

    b64d = base64.b64decode(vstr)

    with open(filename, "wb") as out:
        out.write(b64d)

    output_data = {
        "status": msg.capitalize(),
        "status_code": scode,
        "duration": dur,
        "speaker": spkr,
        "log": log
    }

    print(output_data)

    if play is True:
        playsound.playsound(filename)
        os.remove(filename)

    return output_data


def batch_create(filename: str = 'voice.mp3'):
    out = open(filename, 'wb')

    def sorted_alphanumeric(data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)

    for item in sorted_alphanumeric(os.listdir('./batch/')):
        filestuff = open('./batch/' + item, 'rb').read()
        out.write(filestuff)

    out.close()


def main():
    parser = argparse.ArgumentParser(description="Simple Python script to interact with the TikTok TTS API")
    parser.add_argument("-v", "--voice", help="the code of the desired voice")
    parser.add_argument("-t", "--text", help="the text to be read")
    parser.add_argument("-s", "--session", help="account session id")
    parser.add_argument("-f", "--file", help="use this if you wanna use 'text.txt'")
    parser.add_argument("-n", "--name", help="The name for the output file (.mp3)")
    parser.add_argument("-p", "--play", action='store_true', help="use this if you want to play your output")
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

    if args.session is None:
        print('FATAL: You need to have a TikTok session ID!')
        exit(1)

    if args.file is not None:
        chunk_size = 200
        textlist = textwrap.wrap(req_text, width=chunk_size, break_long_words=True, break_on_hyphens=False)

        batch_dir = './batch/'

        if not os.path.exists(batch_dir):
            os.makedirs(batch_dir)

        for i, item in enumerate(textlist):
            tts(args.session, text_speaker, item, f'{batch_dir}{i}.mp3', False)

        batch_create(filename)

        for item in os.listdir(batch_dir):
            os.remove(batch_dir + item)

        if os.path.exists:
            os.removedirs(batch_dir)

        return

    tts(args.session, text_speaker, req_text, filename, play)


def randomvoice():
    count = random.randint(0, len(voices))
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
