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