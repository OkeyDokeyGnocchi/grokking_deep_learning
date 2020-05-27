weight = 0.5
input = 2
goal_pred = 0.8
learn_rate = 0.1

for i in range(20):
    pred = weight * input
    error = (pred - goal_pred) ** 2
    delta = (pred - goal_pred)
    weight -= (delta * learn_rate)

    print(f'Error: {error} ... Prediction: {pred}')
