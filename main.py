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