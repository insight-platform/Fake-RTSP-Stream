FROM balenalib/raspberry-pi-debian:latest

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# sudo docker run -it --rm --privileged -v /dev:/dev ffmpeg-pi ffmpeg -hwaccel rpi -nostdin -nostats 
# -loglevel error -i 'rtsp://rtsp:bitworks1!@192.168.1.92:554/1/h264major' -f:v fps=10  -filter:v "crop=400:400:400:400" 
# -f:f transpose=2 -pix_fmt yuv420p -c:v h264_v4l2m2m -f rtsp rtsp://server:8554/cam1
