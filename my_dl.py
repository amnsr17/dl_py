import os
import sys
import re
import requests

"""
For test run: python my_dl https://www.youtube.com/watch?v=wb0n-6LiXNc

"""

def qualtiy_show(vid_link):
    """shows all formats available to download
    :param vid_link: link of the youtube video
    :return: None
    """
    try:
        print(os.system("youtube-dl --list-formats "+str(vid_link)))
    except Exception:
        print(Exception)


def download_vid(vid_link, quality_num=None):
    """downloads a youtube video from the provided link
    :param vid_link: link of the youtube video
    :param quality: quality selection number which defines 360p or 480p or 720p
    :return: None
    """
    if quality_num is not None:
        # if quality_num provided
        try:
            os.system("youtube-dl -f "+str(quality_num)+" \'"+str(vid_link)+"\'")
        except Exception:
            print(Exception)
    else:
        # by default the best quality is downloaded
        try:
            os.system("youtube-dl "+str(vid_link))
        except Exception:
            print(Exception)

def main():
    args_num = len(sys.argv)
    print("args_num: ",args_num, sys.argv)

    if args_num>2:
        print("Please enter 1 argument at max. It is the video link.")
        return

    # list of command line arguments
    args_list = sys.argv
    vid_url = args_list[1]
    print("url is: ",vid_url)

    # checking if the url is of youtube
    url_chk = re.match("^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$",vid_url)
    if url_chk is None:
        print("The link is not of youtube or it is incomplete.")
        return

    # checking video availability
    response = requests.get(str(vid_url))
    if "Video unavailable"in response.text:
        print("Link does not contain a video. Please provide a valid link.")
        return

    print("To find the quality options of a youtube video link, enter 'q'.")
    print("To download the best quality video form a link, enter 'd'")
    choice_input = input()

    if  choice_input.isalpha() and len(choice_input)==1:
        if choice_input=='q' or choice_input=='Q':
            qualtiy_show(vid_url)
            print("Enter the quality selection number")
            quality_code = input()
            if quality_code.isdigit():
                download_vid(vid_link=vid_url, quality_num=quality_code)

        elif choice_input=='d' or choice_input=='D':
            download_vid(vid_link=vid_url, quality_num=None)

if __name__ == '__main__':
    main()