from organizer.core import get_category, organize, unique_path


def test_get_category(tmp_path):
    assert get_category(tmp_path / "a.PNG") == "Images"
    assert get_category(tmp_path / "a.pdf") == "Documents"
    assert get_category(tmp_path / "a.xyz") == "Others"


def test_organize_moves_files(tmp_path):
    (tmp_path / "pic.jpg").write_text("x")
    (tmp_path / "notes.txt").write_text("x")
    summary = organize(tmp_path)
    assert summary == {"Images": 1, "Documents": 1}
    assert (tmp_path / "Images" / "pic.jpg").exists()
    assert (tmp_path / "Documents" / "notes.txt").exists()


def test_dry_run_changes_nothing(tmp_path):
    (tmp_path / "pic.jpg").write_text("x")
    organize(tmp_path, dry_run=True)
    assert (tmp_path / "pic.jpg").exists()
    assert not (tmp_path / "Images").exists()


def test_no_overwrite(tmp_path):
    (tmp_path / "Images").mkdir()
    (tmp_path / "Images" / "pic.jpg").write_text("old")
    (tmp_path / "pic.jpg").write_text("new")
    organize(tmp_path)
    assert (tmp_path / "Images" / "pic_1.jpg").read_text() == "new"
    assert unique_path(tmp_path / "Images" / "pic.jpg").name == "pic_2.jpg"
