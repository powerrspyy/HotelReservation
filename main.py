import time
def checkout(hotel, floor, room_number):
    cot = time.time()
    if cot > hotel[floor][room_number][4]:
        fee = hotel[floor][room_number][3] * (hotel[floor][room_number][4] - hotel[floor][room_number][2])
        late_checkout_fee = hotel[floor][room_number][3]*2 *(cot-hotel[floor][room_number][4])
        total_time = cot - hotel[floor][room_number][2]
        total = hotel[floor][room_number][3] * (hotel[floor][room_number][4] - hotel[floor][room_number][2]) + hotel[floor][room_number][3]*2 *(cot-hotel[floor][room_number][4])
    else:
        fee = hotel[floor][room_number][3] * (cot - hotel[floor][room_number][2])
        late_checkout_fee = 0.00
        total_time = cot - hotel[floor][room_number][2]
        total = hotel[floor][room_number][3] * (hotel[floor][room_number][4] - hotel[floor][room_number][2])

    print(f"Total time in hotel: {round(total_time, 2)}\n")
    print(f"Base fee: {round(fee,2)}\n")
    print(f"Late Check Out Fee: {round(late_checkout_fee, 2)}\n")
    print(f"Total: ${round(total,2)}\n")
    hotel[floor][room_number] = (False)

def checkin(hotel, name, time_in, rate, floor, room_number, time_out):
    if hotel[floor][room_number] == (False):
        hotel[floor][room_number] = (True, name, time_in, rate, time_out)
    else:
        print(f"Occupied by {hotel[floor][room_number][1]}")

def main():
    hotel = {1: {1: (False), 2: (False), 3: (False), 4: (False), 5: (False)}, 2: {1: (False), 2: (False), 3: (False), 4: (False), 5: (False)}, 3: {1: (False), 2: (False), 3: (False), 4: (False), 5: (False)}}#{i : {i : ((False),) for i in range(1,6)}for i in range(1,4)}
    while True:
        cmd = input().split()
        if cmd[0] == "exit":
            break
        elif cmd[0].lower() == "checkin" or cmd[0].lower() == "check-in" or cmd[0].lower() == "co":
            checkin(hotel, cmd[1], time.time(), float(cmd[2]), int(cmd[3]), int(cmd[4]), time.time() + float(cmd[5]))
        elif cmd[0].lower() == "checkout" or cmd[0].lower() == "check-out" or cmd[0].lower() == "co":
            checkout(hotel, int(cmd[1]), int(cmd[2]))
if __name__ == "__main__":
    main()