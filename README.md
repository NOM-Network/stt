#  speech to text

first, you must `pip install whisper`,
then call stt with a callback, e.g.

```
    def callback(_, speaker, speech):
        print(f'{speaker}: {speech}')
    my_stt = stt(speaker='speaker', callback=callback)
```
