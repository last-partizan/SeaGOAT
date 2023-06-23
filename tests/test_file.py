import time
from codector.file import File


# pylint: disable-next=too-few-public-methods
class Commit:
    def __init__(self, message, committed_date=0):
        self.message = message
        self.committed_date = committed_date


def test_file_returns_global_metadata_1():
    my_file = File("hello.md")
    my_file.add_commit(Commit("First commit for this"))
    my_file.add_commit(Commit("Another commit for this"))

    assert (
        my_file.get_metadata()
        == """###
Another commit for this
First commit for this"""
    )


def test_file_returns_global_metadata_2():
    my_file = File("hello.md")
    my_file.add_commit(Commit("Unrelated commit"))

    assert (
        my_file.get_metadata()
        == """###
Unrelated commit"""
    )


def test_handles_files_that_were_edited_today():
    my_file = File("hello.md")
    my_file.add_commit(Commit("Unrelated commit", int(time.time())))

    assert (
        my_file.get_metadata()
        == """###
Unrelated commit"""
    )