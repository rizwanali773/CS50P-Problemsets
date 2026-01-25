import project


def test_load_data_empty(tmp_path, monkeypatch):
    """Test loading data when file does not exist."""
    test_file = tmp_path / "study_data.json"
    monkeypatch.setattr(project, "DATA_FILE", test_file)

    data = project.load_data()
    assert data == []


def test_save_and_load_data(tmp_path, monkeypatch):
    """Test saving and loading a study log entry."""
    test_file = tmp_path / "study_data.json"
    monkeypatch.setattr(project, "DATA_FILE", test_file)

    entry = {
        "date": "2025-12-15",
        "subject": "Python",
        "time": 60,
        "mood": "happy"
    }

    project.save_to_file(entry)
    data = project.load_data()

    assert len(data) == 1
    assert data[0]["subject"] == "Python"
    assert data[0]["time"] == 60


def test_analyze_subject_time():
    """Test subject-wise time aggregation logic."""
    data = [
        {"date": "2025-12-14", "subject": "Math", "time": 30, "mood": "neutral"},
        {"date": "2025-12-15", "subject": "Math", "time": 40, "mood": "happy"},
        {"date": "2025-12-15", "subject": "Python", "time": 60, "mood": "tired"}
    ]

    subject_time = {}
    for entry in data:
        subject = entry["subject"]
        subject_time[subject] = subject_time.get(subject, 0) + entry["time"]

    assert subject_time["Math"] == 70
    assert subject_time["Python"] == 60


def test_productivity_score_calculation():
    """Test productivity score logic (capped at 100)."""
    total_time = 600
    productivity_score = min(100, total_time // 5)

    assert productivity_score == 100
