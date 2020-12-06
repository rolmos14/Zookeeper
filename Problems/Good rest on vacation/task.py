# put your python code here
days = int(input())
food_day = int(input())
one_way_flight = int(input())
hotel_night = int(input())

print(days * food_day + 2 * one_way_flight + (days - 1) * hotel_night)
