import random

def generate_custom_url(length=10):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    custom_url = ''.join(random.choice(characters) for _ in range(length))
    return custom_url

# Example usage
url = generate_custom_url()
print(url)
