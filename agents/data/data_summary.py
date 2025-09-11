import pandas as pd
import matplotlib.pyplot as plt
import io

def summarize_csv(uploaded_file):
    """
    Summarize CSV data and generate a simple plot for numeric columns.
    """
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        raise ValueError(f"Failed to read CSV: {str(e)}")

    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "head": df.head(3).to_dict()
    }

    # Generate a plot for numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 0:
        fig, ax = plt.subplots()
        df[numeric_cols].mean().plot(kind="bar", ax=ax, color="#1f77b4")
        ax.set_title("Mean of Numeric Columns")
        ax.set_ylabel("Mean Value")
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)  # Close to free memory
        buf.seek(0)
        summary["output_plot"] = buf

    return summary