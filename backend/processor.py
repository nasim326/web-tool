import pandas as pd
import os

def process_files():
    try:
        shipper_df = pd.read_excel('uploads/shipper_list.xlsx')
        status_df = pd.read_excel('uploads/spool_status.xlsx')
        joint_df = pd.read_excel('uploads/spool_joint_data.xlsx')

        # Merging based on 'Spool ID' or 'ISO Drawing No.'
        merged_df = pd.merge(shipper_df, status_df, on='Spool ID', how='outer')
        merged_df = pd.merge(merged_df, joint_df, on='Spool ID', how='outer')

        output_path = 'uploads/master_file.xlsx'
        merged_df.to_excel(output_path, index=False)
        return output_path
    except Exception as e:
        raise Exception(f"Error processing files: {e}")
