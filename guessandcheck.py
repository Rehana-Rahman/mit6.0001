# We're trying to find the cube root of some integer.
# This time YOU get to pick the number. Freedom!

x = int(input("Yo, drop a number and I'll try to cube-root it: "))

guess = 0  # the starting point of our very sophisticated algorithm

# Keep guessing until we either nail it or accept our fate
while guess**3 != x and guess <= abs(x):
    guess += 1  # brute forcing like it's our full-time job

# Did we actually find a perfect cube?
if guess**3 == x:
    print(f"Cube root of {x} is {guess}")
else:
    print(f"{x} ain't a perfect cube. Peace out >.<")
