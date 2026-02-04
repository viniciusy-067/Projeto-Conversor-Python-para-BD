from flask import Flask, render_template, request, send_file
import pandas as pd
import re
import os
import tempfile

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

ALLOWED_EXT = {".csv", ".xls", ".xlsx"}


def clean_name(v):
    if pd.isna(v):
        return ""
    return re.sub(r"\s+", " ", str(v)).strip()


def clean_number(v):
    if pd.isna(v):
        return ""
    s = str(v).replace(",", ".")
    try:
        if "e" in s.lower():
            s = str(int(float(s)))
    except Exception:
        pass
    digits = re.sub(r"\D", "", s)
    return digits if len(digits) >= 8 else ""


def read_csv_rows(path):
    for chunk in pd.read_csv(
        path,
        chunksize=100_000,
        sep=None,
        engine="python",
        on_bad_lines="skip",
    ):
        name_col = chunk.columns[0]
        num_col = chunk.columns[1]

        for _, r in chunk.iterrows():
            nome = clean_name(r[name_col])
            numero = clean_number(r[num_col])
            if nome and numero:
                yield nome, numero


def read_excel_rows(path):
    df = pd.read_excel(path)
    name_col = df.columns[0]
    num_col = df.columns[1]

    for _, r in df.iterrows():
        nome = clean_name(r[name_col])
        numero = clean_number(r[num_col])
        if nome and numero:
            yield nome, numero


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "Arquivo inválido", 400

        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ALLOWED_EXT:
            return "Formato não suportado", 400

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            file.save(tmp.name)
            input_path = tmp.name

        rows = (
            read_csv_rows(input_path)
            if ext == ".csv"
            else read_excel_rows(input_path)
        )

        # 🔹 DataFrame FINAL no padrão do chatbot
        df_out = pd.DataFrame(rows, columns=["nome", "numero"])
        df_out["e-mail"] = ""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as out:
            output_path = out.name

        df_out.to_excel(output_path, index=False)

        return send_file(
            output_path,
            as_attachment=True,
            download_name="contatos.xlsx",
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
