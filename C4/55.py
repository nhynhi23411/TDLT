def hours(t):
    hour = (t // 3600) % 24
    minute = (t % 3600) // 60
    second = (t % 3600) % 60

    s = "AM" * (t < 43200) + "PM" * (t >= 43200)

    hour = hour - 12 * (hour > 12) * (t >= 43200) + 12 * (hour == 0) * (t >= 43200)

    print(f"{hour}:{minute}:{second} {s}")

t = int(input("Input seconds: "))
hours(t)