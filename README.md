# CichlidActionDetection

This repository contains code for analyzing videos of Lake Malawi male cichlids building sand bowers to attract female mates in naturalistic environments. Using Hidden Markov Models (HMMs) to identify long-lasting changes in pixel color followed by spatial, distance based clustering using dbSCAN, individual sand manipulation events are identified, including scoops and spits using the fishes mouth along with other sand changes caused by fins and the body. 

testScript.py

An example of how the analysis can be run.

VideoFocus.py

Master script that runs analysis of a mp4 movie file (typically 10 hours long with a frame rate of 30 frames/second), to identify parts of the video where fish have manipulated sand using their mouth, body, or fins, resulting in the creation of short video clip containing each sand manipulation event. This script runs 1) HMM analysis of pixel color through time to identify time points when fish manipulate sand in a single pixel, 2) Cluster analysis to group nearby pixels together that have been manipulated in the same event, and 3) Clip creation to generate videos surrounding each cluster.

The videos created by this script can be used for 3D Resnet based classification in to 10 different types of sand manipulation actions. The repository for this code is contained in:

Arguments for this script include the ability to parallelize it’s running using the Num_workers argument, specify output file names and locations, and modify key parameters for each aspect of the analysis.

This script also creates video and frame files that can be used for manual annotation for various purposes.

 VideoFocus.yaml

Anaconda environment for running this repository

Utils/calculateHMM.py

Master script for calculating HMM values for each pixel. This script:

1.	Decompresses an mp4 video file into numpy arrays for each row of data, containing pixel values at 1 frame/sec. This data is stored in a large temp directory that is deleted at the end of analysis.
2.	Runs HMM analysis on each npy array.
3.	Converts each HMM transition to a coordinate file used for cluster analysis.

Utils/calculateClusters.py

Master script for calculating Clusters from HMM transitions. This script
1.	Clusters HMM transitions together into groups, assigning a clusterID for each transition. -1 cluster ID indicates transitions that could not be clustered.
2.	Generates video clips surrounding each cluster
3.	Generates pictures of random frames taken from the video that can be used for manual annotation.

Utils/Decompress_block.py

Utility script used by calculateHMM.py to decompress mp4 file into individual npy arrays for each row of the video.

Utils/HMM_Analyzer.py

Utility class used for storing and analyzing HMM data.

Utils/HMM_row.py

Utility script used by calculateHMM.py to calculate HMMs for each npy row file.

Utils/createClip.py

Utility script used by calculateClusters.py to calculate Clusters in specified time blocks.


