import math

def distance(p1, p2):
    """
    Calculates the Euclidean distance between two points.
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def closest_pair(points):
    """
    Finds the closest pair of points in 2D space using divide and conquer.
    """
    def divide_and_conquer(points):
        n = len(points)

        # Base case: if there are only 2 or 3 points, calculate distances directly
        if n <= 3:
            return brute_force(points)

        mid = n // 2
        mid_point = points[mid]

        # Divide the points into two halves
        left_points = points[:mid]
        right_points = points[mid:]

        # Recursively find the closest pairs in the left and right halves
        left_pair = divide_and_conquer(left_points)
        right_pair = divide_and_conquer(right_points)

        # Determine the smaller distance between the left and right pairs
        min_distance = min(distance(left_pair[0], left_pair[1]), distance(right_pair[0], right_pair[1]))

        # Find the potential closest pairs near the mid line
        mid_pairs = find_mid_pairs(points, mid_point, min_distance)

        # Check for potential closer pairs within the mid pairs
        closest_pair = check_mid_pairs(mid_pairs, min_distance)

        # Return the closest pair found among the left, right, and mid pairs
        candidates = [pair for pair in [left_pair, right_pair, closest_pair] if pair is not None]
        return min(candidates, key=lambda x: distance(x[0], x[1])) if candidates else None

    def brute_force(points):
        """
        Finds the closest pair of points using brute force.
        """
        min_distance = float('inf')
        closest = None

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    closest = (points[i], points[j])

        return closest

    def find_mid_pairs(points, mid_point, min_distance):
        """
        Finds the potential closest pairs near the mid line.
        """
        mid_pairs = []
        for point in points:
            if abs(point[0] - mid_point[0]) < min_distance:
                mid_pairs.append(point)
        return mid_pairs

    def check_mid_pairs(mid_pairs, min_distance):
        """
        Checks for potential closer pairs within the mid pairs.
        """
        closest_pair = None
        mid_pairs.sort(key=lambda x: x[1])

        for i in range(len(mid_pairs) - 1):
            for j in range(i + 1, len(mid_pairs)):
                if mid_pairs[j][1] - mid_pairs[i][1] >= min_distance:
                    break
                dist = distance(mid_pairs[i], mid_pairs[j])
                if dist < min_distance:
                    min_distance = dist
                    closest_pair = (mid_pairs[i], mid_pairs[j])

        return closest_pair

    # Sort the points based on x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Start the divide-and-conquer algorithm
    return divide_and_conquer

