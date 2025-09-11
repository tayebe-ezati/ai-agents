import pandas as pd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def summarize_csv(file):
    """
    Summarize a CSV file and generate a bar plot for a numeric or categorical column.
    Returns a tuple of (summary, figure).
    """
    try:
        logger.info("Reading CSV file...")
        df = pd.read_csv(file)
        logger.info(f"CSV loaded with columns: {df.columns.tolist()}")

        # Generate summary
        summary = "Dataset Summary:\n"
        summary += f"Total Rows: {len(df)}\n"
        summary += f"Total Columns: {len(df.columns)}\n"
        summary += "\nNumeric Columns Statistics:\n"
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_cols) > 0:
            summary += df[numeric_cols].describe().to_string()
        else:
            summary += "No numeric columns found.\n"
        summary += "\n\nCategorical Columns Unique Values:\n"
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            for col in categorical_cols:
                summary += f"{col}: {df[col].nunique()} unique values\n"
        else:
            summary += "No categorical columns found.\n"

        # Generate bar plot
        plt.figure(figsize=(10, 6))
        plot_created = False
        # Try numeric columns first
        for col in numeric_cols:
            if df[col].nunique() > 1:  # Ensure enough unique values
                logger.info(f"Plotting bar chart for numeric column '{col}'...")
                df[col].value_counts().sort_index().plot(kind='bar')
                plt.title(f"Distribution of {col}")
                plt.xlabel(col)
                plt.ylabel("Count")
                plot_created = True
                break
        # Fallback to categorical columns
        if not plot_created:
            for col in categorical_cols:
                if df[col].nunique() > 1 and df[col].nunique() <= 20:  # Limit for readability
                    logger.info(f"Plotting bar chart for categorical column '{col}'...")
                    df[col].value_counts().head(10).plot(kind='bar')
                    plt.title(f"Top 10 Values in {col}")
                    plt.xlabel(col)
                    plt.ylabel("Count")
                    plot_created = True
                    break
        # If no suitable column, show placeholder
        if not plot_created:
            logger.warning("No suitable column for plotting.")
            plt.text(0.5, 0.5, "No suitable column for plotting", ha='center', va='center')
            plt.axis('off')
        fig = plt.gcf()
        logger.info("Plot generated successfully.")
        return summary, fig
    except Exception as e:
        logger.error(f"Error in summarize_csv: {str(e)}")
        raise Exception(f"Data analysis failed: {str(e)}")