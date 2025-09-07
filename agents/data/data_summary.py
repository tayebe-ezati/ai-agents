import pandas as pd
import matplotlib.pyplot as plt
import io

def summarize_csv(uploaded_file):
    """
    خلاصه‌ای از دیتای CSV برمی‌گردونه + نمودار ساده (اگر ستون‌های مناسب موجود باشن)
    """
    df = pd.read_csv(uploaded_file)

    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "head": df.head(3).to_dict()
    }

    # مثال: اگر دیتاست Titanic باشه
    if "Survived" in df.columns and "Sex" in df.columns:
        fig, ax = plt.subplots()
        df.groupby("Sex")["Survived"].mean().plot(kind="bar", ax=ax)
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        summary["output_plot"] = buf

    return summary
