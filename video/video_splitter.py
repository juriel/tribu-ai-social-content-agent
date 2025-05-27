from moviepy import *
import os


def split_video(source_path, target_path:str=None, chunk_size:int =600 , ovelap:int = 30):
    """
    Splits a video file into smaller segments.
    :param source_path: Path to the source video file.
    :param target_path: Path to save the split video file.
    :param chunk_size: Size of each chunk in seconds.
    :param ovelap: Overlap between chunks in seconds.
    """

    if target_path is None:
        video_name = source_path.split("/")[-1].split(".")[0]
        target_path = "video_chunks/" + video_name
    # Create target directory if it doesn't exist
    
    if not os.path.exists(target_path):
            os.makedirs(target_path)

    # Load the video file
    video = VideoFileClip(source_path)
    total_duration = video.duration

    start = 0 
    end = chunk_size
    while end < total_duration:
        # Create a subclip
        cut_video = video.subclip(start, end)
        
        # Write the result to a file
        cut_video.write_videofile(f"{target_path}/chunk_{start}_{end}.mp4", codec="libx264")
        
        # Update start and end for the next chunk
        start += chunk_size - ovelap
        end = start + chunk_size
    # Handle the last chunk
    if start < total_duration:
        cut_video = video.subclip(start, total_duration)
        cut_video.write_videofile(f"{target_path}/chunk_{start}_{total_duration}.mp4", codec="libx264")
    # Close the video file
    video.close()
    
