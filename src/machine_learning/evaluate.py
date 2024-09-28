from src.data_management import load_model_or_data

def load_mildew_test_evaluation(version):
    """
    Load the evaluation results for the mildew detection model from a .pkl file.

    Args:
    version (str): The version of the model ('v1').

    Returns:
    dict: Loaded evaluation metrics (e.g., accuracy, loss).
    """
    return load_model_or_data(f'outputs/{version}/evaluation.pkl')
