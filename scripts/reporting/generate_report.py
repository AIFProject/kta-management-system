import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_FILE = BASE_DIR / "data" / "validated" / "validated_members.csv"
OUTPUT_DIR = BASE_DIR / "data" / "reports"


def generate_report():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    REQUIRED_COLUMNS = [
        "nama_lengkap",
        "jenis_kelamin",
        "organisasi",
        "validation_result",
    ]

    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df_valid = df[df["validation_result"] == "valid"]
    df_invalid = df[df["validation_result"] != "valid"]

    summary = {
        "total_data": len(df),
        "total_valid": len(df_valid),
        "total_invalid": len(df_invalid),
    }

    pd.DataFrame([summary]).to_csv(
        OUTPUT_DIR / "summary_report.csv", index=False
    )

    df_valid.groupby("organisasi").size().reset_index(
        name="count"
    ).to_csv(OUTPUT_DIR / "organization_report.csv", index=False)

    df_valid.groupby("jenis_kelamin").size().reset_index(
        name="count"
    ).to_csv(OUTPUT_DIR / "gender_report.csv", index=False)

    df_valid.groupby(["organisasi", "jenis_kelamin"]).size().reset_index(
        name="count"
    ).to_csv(OUTPUT_DIR / "organization_gender_report.csv", index=False)

    df_valid.to_csv(OUTPUT_DIR / "valid_members.csv", index=False)
    df_invalid.to_csv(OUTPUT_DIR / "invalid_members.csv", index=False)

    print("📊 REPORT GENERATION SELESAI")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    generate_report()