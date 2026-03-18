def get_cost(num_beds, num_bath):
    base_cost = 8000
    bed_base_cost = 3000
    bath_base_cost = 1000
    total_cost = base_cost + num_bath * bath_base_cost + num_beds * bed_base_cost
    return total_cost

def main():
    print(get_cost(2, 4))

if __name__ == "__main__":
    main()