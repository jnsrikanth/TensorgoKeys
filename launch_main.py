import os 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--vid_Path", required=True,help="Please direct the path to the video")
parser.add_argument("-n", "--vid_name", required=True,help="Please do not add the tag ex:.mp4,webm,mp4v etc")
parser.add_argument("-o","--out_name",required=True,help="Path to output the video")
parser.add_argument("-e","--encodings_path",required=True,help="Path to encodings")
parser.add_argument("-u","--users_id",required=True,help="Please enter user_id, if multipe use Comma seprted values.")
parser.add_argument("-vu","--video_url",required=True,help="Please provide Video URL. Pass None if no argumnts.")
args = vars(parser.parse_args())
print(args['video_url'])
os.system('ssh -i /home/ubuntu/arc-development-gpu.key ubuntu@158.101.174.57 "bash arc-cv/main.sh '+args['vid_Path']+' '+args['vid_name']+' '+args['out_name']+' '+args['encodings_path']+' '+args['users_id']+' \''+args['video_url']+'\'"')
