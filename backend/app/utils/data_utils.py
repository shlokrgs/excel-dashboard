import pandas as pd

def merge_dataframes(dataframes, selected_columns):
    merged_df = dataframes[0]
    for i in range(1, len(dataframes)):
        merged_df = pd.merge(
            merged_df,
            dataframes[i],
            left_on=selected_columns['left'][i-1],
            right_on=selected_columns['right'][i-1],
            how="inner"
        )
    return merged_df

def filter_dataframe(df, filters):
    filtered_df = df.copy()
    for col, val in filters.items():
        filtered_df = filtered_df[filtered_df[col] == val]
    return filtered_df
