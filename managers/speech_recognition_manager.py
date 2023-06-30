class SpeechRecognitionManager:
    def __init__(self, max_attempts: int = 2):
        self.max_attempts = max_attempts
        self.attempts = 0
        self.success = False

    def can_recognize(self):
        return not self.success and not self.attempts >= self.max_attempts

    def attempt_failed(self):
        self.attempts += 1

    def attempt_succeeded(self):
        self.success = True

    def reset(self):
        self.attempts = 0
        self.success = False