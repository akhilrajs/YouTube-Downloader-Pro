from pytube import YouTube
import os
import sys
import time
import shutil 
import pafy

def main():
    pass
    

print("# YouTube Downloader Pro")
print("# coded by akhil raj s")
print("# no GUI icoperated")
print()
link = input("enter the video link: ")

if not os.path.exists('downloads'):
        os.makedirs('downloads')

folder = 'downloads'
directory = os.getcwd()
SAVE_PATH = os.path.join(directory, folder)

def show_progress_bar(stream, chunk: bytes, bytes_remaining: int):
  current = ((stream.filesize - bytes_remaining)/stream.filesize)
  percent = ('{0:.1f}').format(current*100)
  progress = int(50*current)
  status = '█' * progress + '-' * (50 - progress)
  sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
  sys.stdout.flush()


x=1
try:
    yt = YouTube(link)
    print("title: ", yt.title)
    from tqdm import tqdm 
    from time import sleep
    for i in tqdm (range (101), 
                   desc="Loading video details ...", 
                   ascii=False, ncols=75): 
        time.sleep(0.01)
    print("The name of the video is : " + yt.title)
    time.sleep(1)
    print("The Authour of the video is: "+ yt.author)
    time.sleep(1)
    print('the available streams that can be downloaded are as follows')
    for streams in yt.streams.filter(file_extension='mp4').all():
        print(str(x)+str(streams))
        x+=1
    itag= input(" enter the itag of the corresponding video format : ")
    streams=yt.streams.get_by_itag(itag)
    print('downloading ', yt.title) 
    yt.register_on_progress_callback(show_progress_bar)
    streams.download(SAVE_PATH)
    print('download finished ...')
    print("checking for availability of english captions... ")
    en_caption = yt.captions.get_by_language_code('en') 
    en_caption_convert_to_srt =(en_caption.generate_srt_captions()) 
    print("saving the subtitles to srt file")
    #save the caption to a file named Output.txt 
    name_of_sub = yt.title + ".srt"
    text_file = open(yt.title+".srt", "w",  encoding='utf-8')
    text_file.write(en_caption_convert_to_srt) 
    text_file.close()
    source = name_of_sub 
    destination = "downloads" 
    new_path = shutil.move(source, destination)
    time.sleep(1)
    print("subtitles has been downloaded")
    print()
    time.sleep(0.3)
    print("downloading audo of the video in highest bitrate available")
    audio_name = yt.title + ".mp3"
    result = pafy.new(link)
    best_quality_audio = result.getbestaudio() 
    print (best_quality_audio) 
    best_quality_audio.download(SAVE_PATH)
    time.sleep(0.3)
    print ("the audio has been downloaded")
    print("")
    print("")
    print("the video has been downloaded ...")
    time.sleep(0.3)
    print("the audio has been downloaded ...")
    time.sleep(0.3)
    print("the subtitles has been downloaded ...")
    time.sleep(0.3)
    print("Thank You ...")
    time.sleep(0.5)
except Exception as e:
    
    print ("error:", e)
    print ("unexpected error has occured we suggest u restart the program")
    print()
    print("error : regex_search occurs due to an unstable internet connection")
    print("error : please check the link that you have entered is correct or not please")
    input("press enter to exit")
