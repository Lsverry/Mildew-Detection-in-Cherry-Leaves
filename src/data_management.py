import base64
from datetime import datetime
import joblib

def export_results_as_csv(df):
    """
    Export the results DataFrame as a CSV file that can be downloaded by the user.
    
    Args:
    df (pd.DataFrame): DataFrame to export.
    
    Returns:
    str: A hyperlink allowing the user to download the CSV file.
    """
    datetime_now = datetime.now().strftime("%d%B%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Mildew_Report_{datetime_now}.csv" '
        f'target="_blank">Download Mildew Detection Report</a>'
    )
    return href

def load_model_or_data(file_path):
    """
    Load a .pkl file (model or data) from the specified file path.
    
    Args:
    file_path (str): Path to the pickle (.pkl) file.
    
    Returns:
    Object: Loaded model or data.
    """
    return joblib.load(filename=file_path)
