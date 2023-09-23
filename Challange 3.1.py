"""
Write a function called linear search product that takes the ist of products and a target product
name as input. The function should perform a near search to find the target product in the int and
return a Int of indices of a occurrences of the product it found, or an empty list if the product is not
found
"""


def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# example usage 
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
