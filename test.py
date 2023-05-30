# import csv
# import json

# def count_rows(filename = 'C:\\Users\\MSI\\Desktop\\Near Earth Objects\\data\\neos.csv'):
#     with open(filename) as f:
#         reader = csv.reader(f)
#         data = list(reader)
#         row_count = len(data)
#         return row_count
    
# print(count_rows())

# #how many neos have diamters in the data set
# def count_diameters(filename = 'C:\\Users\\MSI\\Desktop\\Near Earth Objects\\data\\neos.csv'):
#     with open(filename):
#         reader = csv.DictReader(filename)
#         diameter = []
#         for row in reader:
#             diameter.append(row['diameter'])
#         return diameter
    
# # print(count_diameters())


# def find_closest_neo():
#     with open('C:\\Users\\MSI\\Desktop\\Near Earth Objects\\data\\cad.json') as f:
#         data = json.load(f)
    
#     closest_neo = None
#     closest_distance = float('inf')
    
#     for neo in data['data']:
#         if neo['close_approach_date'].startswith('2015'):
#             distance = float(neo['close_approach_data'][0]['miss_distance']['astronomical'])
#             if distance < closest_distance:
#                 closest_distance = distance
#                 closest_neo = neo['designation']
    
#     return closest_neo

# print(find_closest_neo())