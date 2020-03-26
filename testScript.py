import subprocess, os

subprocess.run(['rclone', 'copy', 'cichlidVideo:McGrath/Apps/CichlidPiData/__TestData/15_minute_clip.mp4', os.getenv('HOME') + '/Temp/'])

args = ['python3', 'VideoFocus.py']
args.extend(['--Movie_file', os.getenv('HOME') + '/Temp/15_minute_clip.mp4'])
args.extend(['--Num_workers', '24'])
args.extend(['--HMM_temp_directory', os.getenv('HOME') + '/Temp/TestHMM/TempHMMFiles/'])
args.extend(['--HMM_filename', os.getenv('HOME') + '/Temp/TestHMM/Test.hmm'])
args.extend(['--HMM_transition_filename', os.getenv('HOME') + '/Temp/TestHMM/TestCoords.npy'])
args.extend(['--Cl_labeled_transition_filename', os.getenv('HOME') + '/Temp/TestHMM/TestLabeledCoords.npy'])
args.extend(['--Cl_labeled_cluster_filename', os.getenv('HOME') + '/Temp/TestHMM/TestClusters.csv'])
args.extend(['--Cl_videos_directory', os.getenv('HOME') + '/Temp/TestHMM/AllClips'])
args.extend(['--ML_frames_directory', os.getenv('HOME') + '/Temp/TestHMM/MLFrames'])
args.extend(['--ML_videos_directory', os.getenv('HOME') + '/Temp/TestHMM/AllClips'])
args.extend(['--Video_start_time', '2020-03-25 11:40:23.417207'])
args.extend(['--VideoID', 'MC6_5,0002_vid'])

subprocess.run(args)
