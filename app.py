from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import uuid
import csv
import re

app = Flask(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

ALLOWED_EXT = {".csv", ".xls", ".xlsx"}

def clean_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace('"', "")).strip()

def clean_number(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    return digits if len(digits) >= 8 else ""

def parse_weird_excel(path):
    raw = pd.read_excel(path, header=None)
    lines = raw.iloc[:, 0].dropna().astype(str).tolist()

    rows = list(csv.reader(lines))
    header = rows[0]
    data = rows[1:]

    name_idx = header.index("nome")
    phone_idx = header.index("celular_principal")

    output = []

    for r in data:
        if len(r) <= max(name_idx, phone_idx):
            continue

        name = clean_name(r[name_idx])
        number = clean_number(r[phone_idx])

        if name and number:
            output.append({"Name": name, "Number": number})

    return pd.DataFrame(output, columns=["Name", "Number"])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return "Arquivo não enviado", 400

        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ALLOWED_EXT:
            return "Formato não suportado", 400

        input_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}{ext}")
        output_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}.csv")

        file.save(input_path)

        if ext in {".xls", ".xlsx"}:
            df = parse_weird_excel(input_path)
        else:
            df = pd.read_csv(input_path)
            df = df.iloc[:, :2]
            df.columns = ["Name", "Number"]
            df["Name"] = df["Name"].astype(str).map(clean_name)
            df["Number"] = df["Number"].astype(str).map(clean_number)
            df = df[(df["Name"] != "") & (df["Number"] != "")]

        df.to_csv(output_path, index=False, quoting=1)

        return send_file(output_path, as_attachment=True, download_name="contatos.csv")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
