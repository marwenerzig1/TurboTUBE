from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube #pip install pytube https://pypi.org/project/pytube/
from pathlib import Path #pip install pathlib https://pypi.org/project/pathlib/
import os
import re

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def indexANDdownloadVideo():  
    if request.method == 'POST' and request.form["video_url"] != '' :  
        mesage = ''
        errorType = 0
        try:
            if request.method == 'POST' and 'video_url' in request.form:
                youtubeUrl = request.form["video_url"]
                selected_format = request.form["format"]
                if(youtubeUrl):
                    validateVideoUrl = (
                    r'(https?://)?(www\.)?'
                    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                    '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
                    validVideoUrl = re.match(validateVideoUrl, youtubeUrl)
                    if validVideoUrl:
                        url = YouTube(youtubeUrl)
                        if selected_format == "mp3":
                            downloadFolder = str(os.path.join(Path.home(), "Downloads"))
                            video = url.streams.filter(only_audio=True).first().download(downloadFolder)
                            new_name = os.path.splitext(video)
                            os.rename(video,new_name[0]+'.mp3')
                            mesage = 'audio Downloaded Successfully!'
                            errorType = 1
                        elif selected_format == "mp4":
                            video = url.streams.get_highest_resolution()
                            downloadFolder = str(os.path.join(Path.home(), "Downloads"))
                            video.download(downloadFolder)
                            mesage = 'Video Downloaded Successfully!'
                            errorType = 1
                    else:
                        mesage = 'Enter Valid YouTube Video URL!'
                        errorType = 0
                else:
                    mesage = 'Enter YouTube Video Url.'
                    errorType = 0       
        except:
            mesage = 'Enter Valid YouTube Video URL!'
            errorType = 0 
        return render_template('index.html', mesage = mesage, errorType = errorType) 
    else :
       return render_template("index.html") 
    
if __name__ == "__main__":
    app.run(debug=True)
