def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    try:
        return time_seconds / (1 - speed_of_light_fraction)
    except ZeroDivisionError:
        return float('inf')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено нечислове значення. Спробуйте ще раз.")

def main():
    while True:
        print("\nКалькулятор 'Таємниці Всесвіту'")
        print("1 - Космічна відстань")
        print("2 - Спрощена гравітація")
        print("3 - Наближення сповільнення часу")
        print("4 - Вихід")

        choice = input("Оберіть опцію (1-4): ")

        if choice == '1':
            speed = get_float_input("Введіть частку швидкості світла (0-1): ")
            time = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(speed, time)
            print(f"Приблизна космічна відстань становить: {result} світлових років.")
        elif choice == '2':
            mass1 = get_float_input("Введіть масу першого об'єкта: ")
            mass2 = get_float_input("Введіть масу другого об'єкта: ")
            factor_input = input("Введіть космічний фактор (або натисніть Enter для значення за замовчуванням): ")
            cosmic_factor = float(factor_input) if factor_input.strip() else 1.0
            result = calculate_simplified_gravity(mass1, mass2, cosmic_factor)
            print(f"Спрощена гравітація: {result}")
        elif choice == '3':
            speed = get_float_input("Введіть частку швидкості світла (0-1): ")
            time = get_float_input("Введіть час у секундах: ")
            result = calculate_time_dilation_approximation(speed, time)
            print(f"Наближене сповільнення часу становить: {result} секунд.")
        elif choice == '4':
            print("Роботу завершено.")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
