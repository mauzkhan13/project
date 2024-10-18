# from itemadapter import ItemAdapter
# import pandas as pd
# import os
#
# class ProPipeline:
#     def __init__(self):
#         self.data_list = []
#
#     def process_item(self, item, spider):
#         self.data_list.append(item)
#         return item
#
#     def close_spider(self, spider):
#         df = pd.DataFrame(self.data_list)
#         current_directory = os.getcwd()
#         csv_folder = os.path.join(current_directory, 'csv')
#
#         if not os.path.exists(csv_folder):
#             os.makedirs(csv_folder)
#
#         file_path = os.path.join(csv_folder, 'Myotcstore file.csv')
#         print(file_path)
#
#         df.to_csv(file_path, index=False)
#         print(f"DataFrame saved as CSV at {file_path}")
