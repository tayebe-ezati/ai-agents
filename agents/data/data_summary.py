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
        summary += df.describe().to_string()
        if df.select_dtypes(include=['object']).columns.any():
            summary += "\n\nCategorical Columns Unique Values:\n"
            for col in df.select_dtypes(include=['object']).columns:
                summary += f"{col}: {df[col].nunique()} unique values\n"

        # Generate bar plot (use 'release_year' for Netflix dataset)
        plt.figure(figsize=(10, 6))
        if 'release_year' in df.columns:
            logger.info("Plotting bar chart for 'release_year'...")
            df['release_year'].value_counts().sort_index().plot(kind='bar')
            plt.title("Distribution of Release Years")
            plt.xlabel("Release Year")
            plt.ylabel("Count")
        else:
            # Fallback to first categorical column
            cat_columns = df.select_dtypes(include=['object']).columns
            if len(cat_columns) > 0:
                logger.info(f"Plotting bar chart for '{cat_columns[0]}'...")
                df[cat_columns[0]].value_counts().head(10).plot(kind='bar')
                plt.title(f"Top 10 Values in {cat_columns[0]}")
                plt.xlabel(cat_columns[0])
                plt.ylabel("Count")
            else:
                logger.warning("No suitable column for plotting.")
                plt.text(0.5, 0.5, "No categorical/numeric column available", ha='center')
                plt.axis('off')
        fig = plt.gcf()
        logger.info("Plot generated successfully.")
        return summary, fig
    except Exception as e:
        logger.error(f"Error in summarize_csv: {str(e)}")
        raise Exception(f"Data analysis failed: {str(e)}")