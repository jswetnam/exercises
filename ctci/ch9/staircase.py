# A child is running up a staircase with N steps, and can hop either 1 step,
# 2 steps, or 3 steps.  Implement a method to count how many possible ways
# the child can run up the stairs.

# Idea: Recurse over the three possibilities

def CountWaysToAscendSteps(total_steps):
  # Add a base case of 0 for step 0
  return CountStepsTakenBottomUp(total_steps, [0 for step in range(total_steps + 1)])

# Each step can be reached by at most 3 other steps:
# step - 1, step - 2, step - 3.
# Thus, a recursive definition is
# (num steps to get to step n - 1 + 1 ) +
# (num steps to get to step n - 2 + 1 ) +
# (num steps to get to step n - 3 + 1 ) +
def CountStepsTakenBottomUp(total_steps, memo):
  if not memo[total_steps]:
    if total_steps > 0:
      memo[total_steps] += 1 + CountStepsTakenBottomUp(total_steps - 1, memo)
    if total_steps > 1:
      memo[total_steps] += 1 + CountStepsTakenBottomUp(total_steps - 2, memo)
    if total_steps > 2:
      memo[total_steps] += 1 + CountStepsTakenBottomUp(total_steps - 3, memo)

  return memo[total_steps]


def main():
  num_steps = 1
  print "Steps: %d Number of ways: %d " % (num_steps, CountWaysToAscendSteps(num_steps))

  num_steps = 2
  print "Steps: %d Number of ways: %d " % (num_steps, CountWaysToAscendSteps(num_steps))

  num_steps = 3
  print "Steps: %d Number of ways: %d " % (num_steps, CountWaysToAscendSteps(num_steps))

  num_steps = 36
  print "Steps: %d Number of ways: %d " % (num_steps, CountWaysToAscendSteps(num_steps))

if __name__ == '__main__':
  main()


