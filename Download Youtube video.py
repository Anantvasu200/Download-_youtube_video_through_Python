import pytube

def download_video(url, download_folder):
    yt = pytube.YouTube(url)
    download_from_server = yt.streams.get_highest_resolution()
    download_from_server.download(download_folder)
    print("Download complete")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_folder = input("Enter the download folder path: ")
    download_video(video_url, download_folder)
