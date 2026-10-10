from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATABASE_DIR = Path(__file__).resolve().parent.parent

SQL_FILE = DATABASE_DIR / "db" / "heat_transfer.sql"
DB_PATH = DATABASE_DIR / "db" / "heat_transfer.db"

RESULTS_DIR = PROJECT_ROOT / "resources" / "results"
PLOTS_DIR = PROJECT_ROOT / "resources" / "plots"