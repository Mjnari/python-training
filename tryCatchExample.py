def div42by(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print("Error: You tried to divide by o")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
