largest_palindrome = 0

# for i in range(999, 99, -1):
#     for j in range(i, 99, -1):
#         product = i * j
#         if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
#             if product > largest_palindrome:
#                 largest_palindrome = product
# print(largest_palindrome)


largest_palindrome  = 0 #We initialize the value

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i*j
        if str(product) == str(product)[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
print(largest_palindrome)
