class Comparer:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.data1 = self.read_excel(file1)
        self.data2 = self.read_excel(file2)

    def read_excel(self, file):
        import pandas as pd
        return pd.read_excel(file)

    def compare(self, criteria):
        if criteria not in ['item_number', 'part_number', 'item_name', 'item_price']:
            raise ValueError("Invalid comparison criteria")
        
        comparison_result = self.data1.merge(self.data2, on=criteria, how='outer', suffixes=('_file1', '_file2'))
        return comparison_result

    def handle_duplicates(self, comparison_result):
        grouped_result = comparison_result.groupby(['item_number']).agg({
            'quantity_file1': 'sum',
            'quantity_file2': 'sum',
            'item_name_file1': 'first',
            'item_price_file1': 'first',
            'item_name_file2': 'first',
            'item_price_file2': 'first'
        }).reset_index()
        return grouped_result

    def save_to_excel(self, comparison_result, output_file):
        comparison_result.to_excel(output_file, index=False)

    def price_unpriced_items(self, comparison_result):
        # Logic to price unpriced items based on criteria
        pass

    def run_comparison(self, criteria, output_file):
        comparison_result = self.compare(criteria)
        final_result = self.handle_duplicates(comparison_result)
        self.save_to_excel(final_result, output_file)