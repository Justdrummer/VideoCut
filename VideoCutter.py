from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def start_time(hour, minute, second):
    hour = hour * 60 * 60
    minute = minute * 60
    second = second
    overall = hour + minute + second
    return overall


start = start_time(0, 58, 30)


def stop_time (hour, minute, second):
    hour = hour * 3600
    minute = minute * 60
    second = second
    overall = hour + minute + second
    return overall


stop = stop_time(3, 43, 50)

ffmpeg_extract_subclip("GMT20200402-122752_EMEA-Virtu_2560x1440.mp4", start, stop, targetname="Edited.mp4")
