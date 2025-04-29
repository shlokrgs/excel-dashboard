import pandas as pd
import io
from app.utils.data_utils import merge_dataframes, filter_dataframe

class FileService:
    def __init__(self):
        self.dataframes = []
        self.merged_df = None
        self.filtered_df = None

    async def upload_files(self, files):
        self.dataframes = []
        for file in files:
            contents = await file.read()
            df = pd.read_excel(io.BytesIO(contents))
            self.dataframes.append(df)
        return {"message": f"Uploaded {len(files)} files successfully."}

    def merge_files(self, selected_columns):
        if not self.dataframes:
            return {"error": "No files uploaded"}

        self.merged_df = merge_dataframes(self.dataframes, selected_columns)
        return {"columns": self.merged_df.columns.tolist()}

    def filter_data(self, filters):
        if self.merged_df is None:
            return {"error": "No merged data"}

        self.filtered_df = filter_dataframe(self.merged_df, filters)
        return {"filtered_data_preview": self.filtered_df.head(100).to_dict(orient="records")}

    def get_filtered_file(self):
        if self.filtered_df is None:
            return None

        output = io.BytesIO()
        self.filtered_df.to_excel(output, index=False, engine="openpyxl")
        output.seek(0)
        return output.read()
