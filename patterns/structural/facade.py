from typing import Any


class FileLoader:
    @staticmethod
    def load_file(filename: str) -> str:
        return f"Loading file {filename}"


class VideoDecoder:
    @staticmethod
    def decode(data: Any) -> str:
        return f"Decode data {data}"


class AudioDecoder:
    @staticmethod
    def decode(data: Any) -> str:
        return f"Decode audio {data}"


class Screen:
    @staticmethod
    def display_video(video_data: Any) -> str:
        return f"Displaying video {video_data}"


class Speaker:
    @staticmethod
    def play_audio(audio_data: Any) -> str:
        return f"Playing audio {audio_data}"


class MediaFacade:
    """
    Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

    This pattern lives up to its name, as the facade is the outer, front part of a building.
    """

    def __init__(self) -> None:
        self.file_loader = FileLoader()
        self.video_decoder = VideoDecoder()
        self.audio_decoder = AudioDecoder()
        self.screen = Screen()
        self.speaker = Speaker()

    def play_media(self, filename: str) -> str:
        # Easy-to-use interface
        file_data = self.file_loader.load_file(filename)
        video_data = self.video_decoder.decode(file_data)
        audio_data = self.audio_decoder.decode(file_data)

        video_output = self.screen.display_video(video_data)
        audio_output = self.speaker.play_audio(audio_data)
        return f"{video_output}\n{audio_output}"
