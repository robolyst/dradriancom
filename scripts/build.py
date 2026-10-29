"""Build the dependency-free static website."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
out = root / 'dist'
out.mkdir(exist_ok=True)
for name in ('index.html', 'styles.css', 'favicon.svg', 'favicon.ico'):
    shutil.copy2(root / name, out / name)
print('Built static site in dist/')
