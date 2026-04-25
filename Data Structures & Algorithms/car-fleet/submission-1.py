class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*combined)
        time = []
        for i in range(len(position)):
            current_time = (target-position[i])/speed[i]
            if not time:
                time.append(current_time)
            else:
                if current_time not in time and not current_time<time[-1]:
                    time.append(current_time)
        print(time)
        return len(time)