import project

# -------------------- load_data --------------------

def test_load_data():
    """Test loading data when file does not exist."""
    data = project.load_data()
    assert isinstance(data, list)


# -------------------- save_to_file --------------------

def test_save_to_file(tmp_path, monkeypatch):
    """Test saving a study log entry."""
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


# -------------------- calculate_streak --------------------

def test_calculate_streak(monkeypatch, tmp_path):
    """Test streak calculation logic."""
    test_file = tmp_path / "study_data.json"
    monkeypatch.setattr(project, "DATA_FILE", test_file)

    project.save_to_file({
        "date": "2025-12-14",
        "subject": "Math",
        "time": 30,
        "mood": "neutral"
    })

    streak = project.calculate_streak()
    assert isinstance(streak, int)


# -------------------- generate_weekly_report --------------------

def test_generate_weekly_report(capsys, monkeypatch, tmp_path):
    """Test weekly report runs without crashing."""
    test_file = tmp_path / "study_data.json"
    monkeypatch.setattr(project, "DATA_FILE", test_file)

    project.save_to_file({
        "date": "2025-12-15",
        "subject": "Python",
        "time": 90,
        "mood": "happy"
    })

    project.generate_weekly_report()
    captured = capsys.readouterr()
    assert "Weekly Study Report" in captured.out