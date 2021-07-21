import argparse, pdb, cv2, datetime,threading
cv2.setNumThreads(1)

print('Starting: ' + str(cv2.setNumThreads(1)) + ' ' + str(datetime.datetime.now()) )
parser = argparse.ArgumentParser(description='This command runs HMM analysis on a single row of data.')
parser.add_argument('Videofile', type = str, help = 'The name of the video file that will be used to create clips')
parser.add_argument('Outfile', type = str, help = 'The name of the video file that will be created')
parser.add_argument('Delta_xy', type = int, help = 'x and y bounds of the clip')
parser.add_argument('Delta_t', type = int, help = 'the length f the clip')
parser.add_argument('Framerate', type = float, help = 'The framerate of the video')

args = parser.parse_args()


#print(args.Outfile)
#print(args.Outfile.split('/')[-1].replace('.mp4','').split('__'))
videoID, LID, N, t, x, y = args.Outfile.split('/')[-1].replace('.mp4','').split('__')
t,x,y = int(t), int(x), int(y)

print('Args parsed: ' + str(cv2.setNumThreads(1)) + ' '+ str(datetime.datetime.now()) )
cap = cv2.VideoCapture(args.Videofile)
print('VideoOpened: ' + str(cv2.setNumThreads(1)) + ' '+ str(datetime.datetime.now()) )
	
outAll = cv2.VideoWriter(args.Outfile, cv2.VideoWriter_fourcc(*"mp4v"), args.Framerate, (2*args.Delta_xy, 2*args.Delta_xy))
print('OutvideoCreated: ' + str(cv2.setNumThreads(1)) + ' '+ str(datetime.datetime.now()) )


cap.set(cv2.CAP_PROP_POS_FRAMES, int(args.Framerate*(t) - args.Delta_t))
print('Set t position: ' + str(cv2.setNumThreads(1)) + ' '+ str(datetime.datetime.now()) )


for i in range(args.Delta_t*2):
	ret, frame = cap.read()
	if ret:
		outAll.write(frame[x-args.Delta_xy:x+args.Delta_xy, y-args.Delta_xy:y+args.Delta_xy])
	else:
		print('VideoError: BadFrame for ' + LID)
print('Reading and writing: ' + str(cv2.setNumThreads(1)) + ' '+ str(datetime.datetime.now()) )

outAll.release()
