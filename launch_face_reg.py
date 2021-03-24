import os 
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", help="path to input directory of faces + images",required=True )
ap.add_argument("-e", "--encodings_path", help="path to serialized db of facial encodings", required=True)
ap.add_argument("-u", "--user_id", help="path to serialized db of facial encodings", required=True)
ap.add_argument("-n", "--user_name", help="path to serialized db of facial encodings", required=True)
args = vars(ap.parse_args())

os.system('ssh -i /home/ubuntu/arc-development-gpu.key ubuntu@158.101.174.57 "bash arc-cv/registration.sh '+args['dataset']+' '+args['encodings_path']+' '+args['user_id']+' '+args['user_name']+'"')
