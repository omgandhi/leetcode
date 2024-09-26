# passes.com

class PaymentDict:
    def __init__(self):
        self.payments = []  # (timestamp, amount, cumulative_sum)
        self.payment_ids = set()

    def binary_search(self, target_time: int, left: int = 0) -> int:
        right = len(self.payments) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.payments[mid][0] < target_time:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def insert(self, payment_id: str, timestamp: int, amount: int):
        if payment_id in self.payment_ids:
            raise ValueError("Payment ID already exists")

        self.payment_ids.add(payment_id)

        index = self.binary_search(timestamp)
        cumulative_sum = amount
        if index > 0:
            cumulative_sum += self.payments[index - 1][2]

        self.payments.insert(index, (timestamp, amount, cumulative_sum))

        # Update cumulative sums for all subsequent payments
        for i in range(index + 1, len(self.payments)):
            self.payments[i] = (self.payments[i][0], self.payments[i][1], self.payments[i][2] + amount)

    def range_query(self, start_time: int, end_time: int) -> int:
        if not self.payments or start_time > self.payments[-1][0] or end_time < self.payments[0][0]:
            return 0

        start_index = self.binary_search(start_time)
        end_index = self.binary_search(end_time + 1) - 1  # +1 to include end_time

        end_sum = self.payments[end_index][2]
        start_sum = self.payments[start_index - 1][2] if start_index > 0 else 0

        return end_sum - start_sum
