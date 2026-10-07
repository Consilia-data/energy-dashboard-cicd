from src.energy import total_capacity

def test_total_capacity():
    capacities = [8.5, 12, 6, 20, 35, 15]

    result = total_capacity(capacities)

    print("Capacité totale :", result)

    assert result == 96.5