from whisper_mic.whisper_mic import WhisperMic
import threading
def stt(speaker='speaker', callback=print):
    whisper = WhisperMic(model='small')
    def listen():
        while True:
            try:
                speech = whisper.listen()
                callback(speaker, speech)
            except Exception as e:
                print('listen failed')
                pass
    thread = threading.Thread(target=listen)
    thread.start()
    print('listening...')

if __name__ == "__main__":
    def callback(c, speaker, speech):
        print(f'{speaker}: {speech}')
    my_stt = stt(speaker='speaker', callback=callback)
