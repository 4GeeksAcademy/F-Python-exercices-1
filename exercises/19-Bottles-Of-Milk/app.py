# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99, 2, -1):
        print(f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i -1} bottles of milk on the wall.\n", end="")

    print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.\n", end="")
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\n", end="")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.\n", end="")

number_of_bottles()
