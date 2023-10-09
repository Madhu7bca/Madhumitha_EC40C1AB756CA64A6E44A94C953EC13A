def linear_search_product(products, target_product):
    """
    Perform a linear search to find the target product in the list.

    Parameters:
    products (list): A list of product names.
    target_product (str): The product name to search for.

    Returns:
    list: A list of indices of all occurrences of the product, or an empty list if not found.
    """
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage
products_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product_name = "Apple"
result = linear_search_product(products_list, target_product_name)
print("Indices of", target_product_name, ":", result)
