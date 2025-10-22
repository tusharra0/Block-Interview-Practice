def percentage_time_a_greater(window, A, B):
    """
    Calculate the percentage of time during which player A's power
    was greater than player B's, given both players' timestamped power readings.
    """

    # --------------------------------------------------------
    # STEP 1 — Sort both lists by timestamp
    # --------------------------------------------------------
    # We sort them to make sure the timestamps are in increasing order.
    # This makes it possible to process them like a timeline.
    A = sorted(A)
    B = sorted(B)

    # --------------------------------------------------------
    # STEP 2 — Add a "sentinel" value at the end for each player
    # --------------------------------------------------------
    # We extend both lists to reach the total game duration.
    # This helps avoid index errors when we look at "next" timestamps.
    last_a_time = A[-1][0]
    last_b_time = B[-1][0]

    if last_a_time < window:
        # Extend A's list so its final power lasts until the end of the game.
        A.append([window, A[-1][1]])

    if last_b_time < window:
        # Extend B's list similarly.
        B.append([window, B[-1][1]])

    # --------------------------------------------------------
    # STEP 3 — Initialize pointers and variables
    # --------------------------------------------------------
    i = 0   # pointer for Player A's list
    j = 0   # pointer for Player B's list

    time_a_greater = 0.0  # total duration where A's power > B's
    current_time = 0.0    # the current time in the simulation

    # --------------------------------------------------------
    # STEP 4 — Initialize current power values
    # --------------------------------------------------------
    # If a player has no power reading yet (before their first timestamp),
    # assume their power is 0.
    current_a = 0.0
    current_b = 0.0

    # If Player A's first timestamp starts at time 0, use that initial power.
    if len(A) > 0 and A[0][0] == 0:
        current_a = A[0][1]

    # If Player B's first timestamp starts at time 0, use that initial power.
    if len(B) > 0 and B[0][0] == 0:
        current_b = B[0][1]

    # --------------------------------------------------------
    # STEP 5 — Process both lists simultaneously until we reach the end
    # --------------------------------------------------------
    while current_time < window:
        # Find when each player’s power changes next.
        if i + 1 < len(A):
            next_a_time = A[i + 1][0]
        else:
            next_a_time = window

        if j + 1 < len(B):
            next_b_time = B[j + 1][0]
        else:
            next_b_time = window

        # The next change event happens at the smaller of these two times.
        next_change_time = min(next_a_time, next_b_time, window)

        # --------------------------------------------------------
        # STEP 6 — If A's power is currently higher, accumulate that time
        # --------------------------------------------------------
        if current_a > current_b:
            # Add the duration between now and the next change
            time_a_greater += (next_change_time - current_time)

        # Move time forward to the next change
        current_time = next_change_time

        # --------------------------------------------------------
        # STEP 7 — Update the player(s) whose power changes at this time
        # --------------------------------------------------------
        if next_change_time == next_a_time and (i + 1 < len(A)):
            i = i + 1
            current_a = A[i][1]

        if next_change_time == next_b_time and (j + 1 < len(B)):
            j = j + 1
            current_b = B[j][1]

    # --------------------------------------------------------
    # STEP 8 — Compute the percentage of time A was stronger
    # --------------------------------------------------------
    percentage = (time_a_greater / window) * 100.0
    return percentage


# --------------------------------------------------------
# Example usage
# --------------------------------------------------------
window = 300.0
playerA = [[50, 60], [100.33, 40], [200, 80]]
playerB = [[1, 75], [50.5, 70]]

result = percentage_time_a_greater(window, playerA, playerB)
print(f"Percentage of time A > B: {result:.2f}%")
