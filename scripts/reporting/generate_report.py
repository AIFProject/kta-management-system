import pandas as pd
from pathlib import Path

# ======= Configuration =======
BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = BASE_DIR / 'data' / 'validated' / 'validated_members.csv'
OUTPUT_DIR = BASE_DIR / 'data' / 'reports'

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ======= Load Data =======
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE)

# ======= Basic Validation =======
REQUIRED_COLUMNS = [
    "nama_lengkap",
    "jenis_kelamin",
    "organisasi",
    "validation_result",
]

missing = set(REQUIRED_COLUMNS) - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# ======= Filter Valid Data =======
df_valid = df[df['validation_result'] == 'valid']
df_invalid = df[df['validation_result'] != 'valid']

# ======= Summary Statistic =======
summary = {
    "total_data": len(df),
    "total_valid": len(df_valid),
    "total_invalid": len(df_invalid),
}

summary_df = pd.DataFrame([summary])

#======= Grouping Reports =======
org_report = (
    df_valid.groupby('organisasi')
    .size()
    .reset_index(name='count')
)

gender_report = (
    df_valid.groupby("jenis_kelamin")
    .size()
    .reset_index(name='count')
)

org_gender_report = (
    df_valid.groupby(['organisasi', 'jenis_kelamin'])
    .size()
    .reset_index(name='count')
)

df_valid.to_csv(OUTPUT_DIR / 'valid_members.csv', index=False)
df_invalid.to_csv(OUTPUT_DIR / 'invalid_members.csv', index=False)

summary_df.to_csv(OUTPUT_DIR / 'summary_report.csv', index=False)
org_report.to_csv(OUTPUT_DIR / 'organization_report.csv', index=False)
gender_report.to_csv(OUTPUT_DIR / 'gender_report.csv', index=False)
org_gender_report.to_csv(OUTPUT_DIR / 'organization_gender_report.csv', index=False)

# ======= Console Output =======
print("📊 REPORT GENERATION SELESAI")
print(f"Total data     : {summary['total_data']}")
print(f"Data valid     : {summary['total_valid']}")
print(f"Data invalid   : {summary['total_invalid']}")
print(f"Output folder  : {OUTPUT_DIR.resolve()}")