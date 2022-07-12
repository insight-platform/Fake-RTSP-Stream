# Fake RTSP Stream

## Requirements:

- docker installed
- docker-compose installed

## Features:

- stream as many RTSP streams from local files as you want;
- streams are translated in a loop;
- source is FFmpeg, so you can utilize its power to implement extra transformations, transcoding, etc.

To understand what to do next, look at [docker-compose.yml](docker-compose.yml); it provides all the necessary
information to understand what to do to add additional RTSP sources.

## Running the Streaming

To run the streaming, type `docker-compose up` or `docker-compose up -d` if you want to launch in the background.

To get the access to streams use: `rtsp://machine-ip:8554/<stream-name>` URL.

Compose service `looping-sample` starts infinitely looping stream from sample video.

Compose service `concatenated-sample` starts a stream with every video from `samples/input_files` directory in sequential order. Script assumes there are only videos in the directory, and these videos are all in the same format (able to be concatenated without reencoding).

## Additional Configuration

To have a stable IP, which is convenient for development purposes, in Linux, you can set up a dummy
network device like that:

```bash
auto dummy0
iface dummy0 inet static
  address 10.0.0.1
  netmask 255.255.255.0
  pre-up rmmod dummy; modprobe dummy numdummies=1
```

Now, you will be able to connect to RTSP streams on `rtsp://10.0.0.1:8554/<name>` URL.
