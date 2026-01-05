import pandas as pd
from pathlib import Path
from datetime import datetime

# ======= Configuration =======
INPUT_FILE = Path("data/validated/validated_members.csv")
OUTPUT_DIR = Path("data/ready_for_kta")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

KODE_KECAMATAN = "TGD"
TAHUN = datetime.now().year % 100  # Last two digits of the current year

# ======= Load Data =======
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE)

# ======= Basic Validation =======
REQUIRED_COLUMNS = [
    "nama_lengkap",
    "organisasi",
    "ranting",
    "validation_result",
]

missing = set(REQUIRED_COLUMNS) - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# ======= Filter Valid Data =======
df_valid = df[df['validation_result'] == 'valid'].copy()

if df_valid.empty:
    raise ValueError("No valid data found to generate KTA numbers.")

# ======= Sorting Data =======
df_valid = df_valid.sort_values(
    by=['organisasi', 'ranting', 'nama_lengkap'],
).reset_index(drop=True)

# ======= Generate KTA Numbers =======
kta_numbers = []
counter = {}

for _, row in df_valid.iterrows():
    key = f"{row['organisasi']}-{TAHUN}"
    counter[key] = counter.get(key, 0) + 1
    
    nomor_urut = str(counter[key]).zfill(4)
    nomor_kta = f"{row['organisasi']}-{KODE_KECAMATAN}-{TAHUN}-{nomor_urut}"
    kta_numbers.append(nomor_kta)
    
df_valid["nomor_kta"] = kta_numbers
df_valid["tanggal_terbit_kta"] = datetime.now().strftime("%Y-%m-%d")
df_valid["status_kta"] = "belum dicetak"

# ======= Save Output =======
output_file = OUTPUT_DIR / "members_with_kta_numbers.csv"
df_valid.to_csv(output_file, index=False)

print(f"✅ Nomor KTA berhasil dibuat")
print(f"📁 File tersimpan di: {output_file.resolve()}")
print(f"👥 Total anggota: {len(df_valid)}")