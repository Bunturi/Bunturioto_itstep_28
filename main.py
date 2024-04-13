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