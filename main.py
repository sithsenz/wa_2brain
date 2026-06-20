import re
from datetime import datetime, timedelta
from pathlib import Path


nama_file = {
    "WhatsApp Chat with Mikrob (Official).txt": "WA Mikrob.txt",
}

def main():
    root_dir = Path(input("Masukkan alamat direktori:"))

    date_pattern = re.compile(r'^(\d{2})[/](\d{2})[/](\d{4})(.*)')

    folder_log = Path("logWA")
    folder_log.mkdir()

    for lama, baharu in nama_file.items():
        outbaharu = folder_log / Path(baharu)

        filepath = next(root_dir.rglob(lama), None)

        with filepath.open() as infile, outbaharu.open(mode="w") as outfile:
            for baris in infile:
                jumpa = date_pattern.match(baris)

                if jumpa:
                    hari, bulan, tahun, teks = jumpa.groups()
                    baris_iso = f'{tahun}-{bulan}-{hari}{teks}\n'
                    outfile.write(baris_iso)
                else:
                    outfile.write(baris)


if __name__ == "__main__":
    main()
