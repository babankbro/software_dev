#color = "Green"
#size = 20
#weight = 1.5
#print("Ball:")
#print(f"\tColor: {color}")
#print(f"\tSize: {size} cm.")
#print(f"\tWeight: {weight} kg.")
def display_ball(b):
    print("Ball:")
    print(f"\tColor: {b['color']}")
    print(f"\tSize: {b['size']} cm.")
    print(f"\tWeight: {b['weight']} kg.")


ball1 = {"color": "Green",
        "size": 20,
        "weight": 1.5}
ball2 = {"color": "Red",
        "size": 10,
        "weight": 5}
display_ball(ball1)
display_ball(ball2)

