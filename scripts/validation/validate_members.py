import pandas as pd
from pathlib import Path
import datetime

# ======= Configuration =======
BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_DIR = BASE_DIR / "data" / "sample"
OUTPUT_DIR = BASE_DIR / "data" / "validated"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REQUIRED_COLUMNS = [
    "nama_lengkap",
    "jenis_kelamin",
    "tanggal_lahir",
    "organisasi",
    "ranting",
    "tahun_masuk",
]

VALID_ORGANIZATIONS = ["IPNU", "IPPNU"]
VALID_GENDERS = ["L", "P"]

# ======= Helper Functions =======
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_row(row):
    errors = []

    for col in REQUIRED_COLUMNS:
        if pd.isna(row[col]) or str(row[col]).strip() == "":
            errors.append(f"{col} kosong")

    if row["jenis_kelamin"] not in VALID_GENDERS:
        errors.append("jenis_kelamin tidak valid")

    if row["organisasi"] not in VALID_ORGANIZATIONS:
        errors.append("organisasi tidak valid")

    if row["organisasi"] == "IPPNU" and row["jenis_kelamin"] != "P":
        errors.append("jenis_kelamin harus 'P' untuk organisasi IPPNU")

    if row["organisasi"] == "IPNU" and row["jenis_kelamin"] != "L":
        errors.append("jenis_kelamin harus 'L' untuk organisasi IPNU")

    if not is_valid_date(str(row["tanggal_lahir"])):
        errors.append("tanggal_lahir tidak valid")

    current_year = datetime.datetime.now().year
    if not str(row["tahun_masuk"]).isdigit():
        errors.append("tahun_masuk harus berupa angka")
    elif int(row["tahun_masuk"]) > current_year:
        errors.append("tahun_masuk tidak boleh di masa depan")

    return errors


# ======= Main Validation Logic =======
print("Membaca data dari:", INPUT_DIR.resolve())

all_data = []
for file in INPUT_DIR.glob("*.csv"):
    print("Reading:", file.name)
    df = pd.read_csv(file)
    df["source_file"] = file.name
    all_data.append(df)

if not all_data:
    raise ValueError(f"Tidak ada file CSV ditemukan di {INPUT_DIR}")

data = pd.concat(all_data, ignore_index=True)

# Validate Data
validation_results = []
for _, row in data.iterrows():
    errors = validate_row(row)
    validation_results.append(
        "valid" if not errors else "invalid: " + "; ".join(errors)
    )

data["validation_result"] = validation_results

# Detect duplicates
data["duplicate_key"] = (
    data["nama_lengkap"].str.lower().str.strip()
    + "_"
    + data["tanggal_lahir"].astype(str)
)

duplicates = data.duplicated("duplicate_key", keep=False)
data.loc[duplicates, "validation_result"] = "invalid: duplikat data"

# Save Validated Data
output_file = OUTPUT_DIR / "validated_members.csv"
data.drop(columns=["duplicate_key"]).to_csv(output_file, index=False)

print(f"✅ Validasi selesai. File disimpan di {output_file}")
