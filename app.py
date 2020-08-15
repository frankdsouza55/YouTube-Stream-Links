from flask import Flask, render_template, request
import pafy
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html')


@app.route("/results", methods=['POST'])
def showResults():
    domains = ['youtube.com', 'youtu.be']
    data = {}
    validURL = False

    if request.method == 'POST':
        url = request.values.get('inputURL')
        print(url)
        if any(x in url for x in domains):
            validURL = True

            video = pafy.new(url)
            data["title"] = video.title
            data["author"] = video.author
            data["id"] = video.videoid
            data["duration"] = video.duration
            data["views"] = video.viewcount

            bestAudio = video.getbestaudio()
            data["bitRate"] = bestAudio.quality
            data["audioLink"] = bestAudio.url

            bestVideo = video.getbest()
            data["resolution"] = bestVideo.quality
            data["videoLink"] = bestVideo.url

    return render_template('results.html', data=data, validURL=validURL)


if __name__ == '__main__':
    app.run(debug=True)
