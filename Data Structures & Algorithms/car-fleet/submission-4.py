class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        for p,s in cars:
            current_time = (target-p)/s

            if not fleets or current_time>fleets[-1]:
                fleets.append(current_time)
        
        return len(fleets)