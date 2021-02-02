from src.audio_file_server_app.schemas import AudioFileShcema


def test_audio_file_schema():
    audio_file_schema = AudioFileShcema(
        **{"file_type": "song", "file_metadata": {"name": "test"}}
    )
    import pdb;pdb.set_trace()
    assert audio_file_schema.file_type == "song"
    assert audio_file_schema.file_metadata["name"] == "test"
