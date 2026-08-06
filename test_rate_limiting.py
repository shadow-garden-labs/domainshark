import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = float(capacity)
        self._tokens = float(capacity)
        self.fill_rate = float(fill_rate)  # Tokens per second
        self.timestamp = time.time()

    def consume(self, tokens=1):
        now = time.time()
        # Add tokens accumulated since last check
        self._tokens += (now - self.timestamp) * self.fill_rate
        if self._tokens > self.capacity:
            self._tokens = self.capacity
        self.timestamp = now

        if tokens <= self._tokens:
            self._tokens -= tokens
            return True
        return False

# Usage: 10 max capacity, recovers 2 tokens per second
bucket = TokenBucket(capacity=10, fill_rate=2)
if bucket.consume():
    # Execute rate-limited action
    pass
