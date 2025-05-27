import argparse
from dotenv import load_dotenv
import video.video_splitter as video_splitter


#comentario


def about():
    """
    Displays information about the program.
    """
    print("Tribu AI Social Content Agent")
    print("Version: 1.0.0")
    print("Author: Tribu AI")



def main():
    """
    Main function to parse arguments and execute the program.
    """
    parser = argparse.ArgumentParser(description="Tribu AI Social Content Agent")
    parser.add_argument('--about', action='store_true', help="Display information about the program")
    parser.add_argument('--video_splitter', type=str)
    parser.add_argument('--source', type=str)

    
    args = parser.parse_args()
    
    load_dotenv()

    if args.about:
        about()
    elif args.video_splitter:
        source_path = args.video_splitter
        target_path = None
        chunk_size = 600
        overlap = 30

        # Call the video splitter function
        video_splitter.split_video(source_path, target_path, chunk_size, overlap)

    else:
        print("No arguments provided. Use --about to see information about the program.")


if __name__ == "__main__":
    main()