# 1-1.

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name: {self.restaurant_name}, Cuisine type: {self.cuisine_type}')

    def open_restaurant(self):
        print('Restaurant is open!')


restaurant = Restaurant('Palace','Turkish')

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 1-2.

restaurant1 = Restaurant('McDonalds','Fast food')
restaurant2 = Restaurant('Shangan','Vietnam')
restaurant3 = Restaurant('Taco','Mexican')

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# 1-3.

class User:

    def __init__(self, first_name, last_name, age, location, prompt):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.prompt = prompt

    def describe_user(self):
        print(f"First Name: {self.first_name} \nLast Name: {self.last_name} \nUser's Age : {self.age} \nUser's Location: {self.location} \nUser's title: {self.prompt}")

    def greet_user(self):
        print(f'Hi, {self.first_name} {self.last_name}.Nice to meet you!\n')


user1 = User('John', 'Doe', 25, 'Vietnam', 'Full')
user2 = User('Daniel', 'Gabriella', 20, 'USA', 'Limited')
user3 = User('Maxim', 'Ivanovic', 19, 'Russia', 'Limited')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# Test