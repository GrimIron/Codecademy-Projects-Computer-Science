# Calculates the force of a object
def get_force(mass, acceleration):
    return mass * acceleration


# Calculates the energy of a explosion, c's default is the speed of light which is roughly 3 x 10^8
def get_energy(mass, c=3 * 10 ** 8):
    return mass * (c ** 2)


# Calculates the work of an object
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance


# values for the train_force and bomb_energy
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Calculates, formats and displays the force of a train
train_force = get_force(train_mass, train_acceleration)
train_force_formated = ("{:,}".format(train_force))
print(f"The GE train supplies {train_force_formated} Newtons of force\n")

# Calculates, formats and displays the energy of a bomb
bomb_energy = get_energy(bomb_mass)
bomb_energy_formated = ("{:,}".format(bomb_energy))
print(f"A 1kg bomb supplies {bomb_energy_formated} Joules\n")

# Calculates, formats and displays the work of a train
train_work = get_work(train_mass, train_acceleration, train_distance)
train_work_formated = ("{:,}".format(train_work))
print(f"The GE train does {train_work_formated} Joules of work over {train_distance} meters.\n")


# Converts Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# Converts Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


# Calculates 100° Fahrenheit to Celsius and Calculates 0° Celsius to Fahrenheit and displays
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
print(f"100° Fahrenheit is {f100_in_celsius:.2f}° Celsius")
print(f"0° Celsius is {c0_in_fahrenheit:.2f}° Fahrenheit")
