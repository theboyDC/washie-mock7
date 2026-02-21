def clean_and_format_data(raw_data):
    """
    Standardizes a list of package IDs and weights.
    
    Task: 
    1. Remove whitespace from string IDs.
    2. Convert all weights to floats.
    3. Filter out any entries where weight is negative.
    
    :param raw_data: List of tuples (str, val)
    :return: List of dicts {'id': str, 'weight': float}
    """
    pass

def get_total_weight_recursive(manifest):
    """
    Calculates total weight of a nested shipping container.
    
    The manifest is a nested list that can contain:
    - Floats (representing package weights)
    - Lists (representing sub-containers with more packages)
    
    Task: Use recursion to find the sum of all weights regardless of depth.
    
    :param manifest: List[Union[float, list]]
    :return: float (total weight)
    """
    pass

def generate_shipping_label(package_id, weight, destination):
    """
    Creates a formatted string for a shipping label.
    
    Task: Use f-strings to return a label in the exact format:
    "ID: [ID] | Weight: [WEIGHT]kg | Dest: [DESTINATION]"
    Weight must be rounded to 2 decimal places.
    
    :param package_id: str
    :param weight: float
    :param destination: str
    :return: str
    """
    pass
