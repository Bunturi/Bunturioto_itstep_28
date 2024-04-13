from abc import ABC, abstractmethod

# Define interface for media player
class MediaPlayer(ABC):
    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def rewind(self, seconds):
        pass

    @abstractmethod
    def fast_forward(self, seconds):
        pass

# Define interface for audio player
class AudioPlayer(MediaPlayer):
    @abstractmethod
    def play_audio(self):
        pass


# Define interface for video player
class VideoPlayer(MediaPlayer):
    @abstractmethod
    def play_video(self):
        pass


# Define interface for streaming player
class StreamingPlayer(MediaPlayer):
    @abstractmethod
    def play_stream(self, url):
        pass


# Implement AudioPlayer
class MyAudioPlayer(AudioPlayer):
    def play_audio(self):
        print("Playing audio...")

    def pause(self):
        print("Audio paused...")

    def stop(self):
        print("Audio stopped...")

    def rewind(self, seconds):
        print(f"Rewinding audio by {seconds} seconds...")

    def fast_forward(self, seconds):
        print(f"Fast forwarding audio by {seconds} seconds...")


# Implement VideoPlayer
class MyVideoPlayer(VideoPlayer):
    def play_video(self):
        print("Playing video...")

    def pause(self):
        print("Video paused...")

    def stop(self):
        print("Video stopped...")

    def rewind(self, seconds):
        print(f"Rewinding video by {seconds} seconds...")

    def fast_forward(self, seconds):
        print(f"Fast forwarding video by {seconds} seconds...")


# Implement StreamingPlayer
class MyStreamingPlayer(StreamingPlayer):
    def play_stream(self, url):
        print(f"Streaming from {url}...")

    def pause(self):
        print("Streaming paused...")

    def stop(self):
        print("Streaming stopped...")

    def rewind(self, seconds):
        print(f"Rewinding stream by {seconds} seconds...")

    def fast_forward(self, seconds):
        print(f"Fast forwarding stream by {seconds} seconds...")


# Usage
audio_player = MyAudioPlayer()
audio_player.play_audio()
audio_player.pause()
audio_player.stop()
audio_player.rewind(10)
audio_player.fast_forward(20)

video_player = MyVideoPlayer()
video_player.play_video()
video_player.pause()
video_player.stop()
video_player.rewind(30)
video_player.fast_forward(40)

streaming_player = MyStreamingPlayer()
streaming_player.play_stream("http://heyho.com/stream")
streaming_player.pause()
streaming_player.stop()
streaming_player.rewind(15)
streaming_player.fast_forward(25)