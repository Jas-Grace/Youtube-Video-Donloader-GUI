from PyQt5.QtWidgets import *
from pytube import YouTube
from time import sleep
import subprocess

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

style = '''
QWidget {
    background-color: coral; 
} 

QPushButton {
    background-color: #006325;
    font-size: 20px;
    color: white;

    min-width:  100px;
    max-width:  100px;
    min-height: 50px;
    max-height: 50px;

    border-radius: 5px;        
    border-width: 1px;
    border-color: #ae32a0;
    border-style: solid;
}
QPushButton:hover {
    background-color: #328930;
    color: yellow;
}
QPushButton:pressed {
    background-color: #80c342;
    color: red;
}
[accessibleName="namel"] {
    color: white;
}
'''

class Widgets(QWidget):
    def __init__(self, **kwargs):
        super(Widgets, self).__init__()
        
        self.vlayout = QVBoxLayout(self)
        
        # Horizontal Layout****************************
        self.hlayout_1 = QHBoxLayout(self)
        
        self.l1 = QLabel()
        self.l1.setText("Enter the link of the video that you want to download:")
        self.hlayout_1.addWidget(self.l1)
        
        self.text1 = QLineEdit()
        self.hlayout_1.addWidget(self.text1)
        
        # Button****************************************
        self.btn = QPushButton("Submit")
        self.btn.clicked.connect(self.submitBTN)
        
        # Add layouts***********************************
        self.vlayout.addLayout(self.hlayout_1)
        self.vlayout.addWidget(self.btn)
        self.setLayout(self.vlayout)
    
    def submitBTN(self):
        link = self.text1.text()
        #Creating video lists
        video_list = [link]
        #Looping through the list
        for i in video_list:
            try:
                yt = YouTube(i)
                notify('YouTube Video Downloader', f'Downloading the video: {yt.streams[0].title}')
            except:
                notify('YouTube Video Downloader', 'Connection Error')
        #filters out all the files with "mp4" extension
        stream = yt.streams.filter(res="720p").first()
        stream.download("downloads/")
        self.text1.setText('')
        notify('Youtube Video Downloader', 'Video Downloaded!')
        sleep(2)
        notify('Youtube Video Downloader', 'Enter link of any other video to download. Keep downloading!')
    
def window(): 
    app = QApplication([])
    wig = Widgets()
    wig.setStyleSheet(style)
    wig.show()
    app.exec_()
        
if __name__ == "__main__":
    window()
