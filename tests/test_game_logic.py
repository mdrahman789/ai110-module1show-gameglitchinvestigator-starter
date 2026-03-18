from logic_utils import check_guess, reset_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


def test_reset_game_state_restarts_round():
    # Set up a fake session_state with non-default values
    class DummyState:
        pass

    state = DummyState()
    state.secret = 999
    state.attempts = 5
    state.status = "won"
    state.history = [10, 20]
    state.score = 123

    low, high = 1, 50

    # When we reset the game state, per-round values should be reset
    reset_game_state(state, low=low, high=high)

    # Secret should be within the current difficulty range
    assert low <= state.secret <= high
    # Attempts, status, and history should be reset for a new round
    assert state.attempts == 1
    assert state.status == "playing"
    assert state.history == []
    # Overall score should be preserved across rounds
    assert state.score == 123


def test_hint_when_guess_higher_than_secret():
    """Guess above secret → 'Too High' outcome and hint."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()


def test_hint_when_guess_lower_than_secret():
    """Guess below secret → 'Too Low' outcome and hint."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


def test_hint_when_guess_is_correct():
    """Exact match → 'Win' outcome and success hint."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()
