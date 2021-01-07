from pydub import AudioSegment     #导入pydub库
song  = AudioSegment.from_mp3("[PATH]")
length = song.duration_seconds * 1000 #millionseconds
sliceSong = song[-(length-21*1000):]
outLouder = sliceSong + 1     #将song音量+1
outLouder.export("outLouder.mp3",format="mp3")    #导出