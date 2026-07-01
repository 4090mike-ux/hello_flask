from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "skills.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill TEXT NOT NULL,
            level TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def get_skills():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM skills ORDER BY id DESC")
    skills = cur.fetchall()

    conn.close()
    return skills


def get_skill(skill_id):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM skills WHERE id = ?",
        (skill_id,)
    )
    skill = cur.fetchone()

    conn.close()
    return skill


def add_skill(skill, level, status):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO skills (skill, level, status) VALUES (?, ?, ?)",
        (skill, level, status)
    )

    conn.commit()
    conn.close()


def update_skill(skill_id, skill, level, status):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "UPDATE skills SET skill = ?, level = ?, status = ? WHERE id = ?",
        (skill, level, status, skill_id)
    )

    conn.commit()
    conn.close()


def delete_skill(skill_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM skills WHERE id = ?",
        (skill_id,)
    )

    conn.commit()
    conn.close()


def delete_selected_skills(skill_ids):
    if not skill_ids:
        return

    placeholders = ",".join(["?"] * len(skill_ids))
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        f"DELETE FROM skills WHERE id IN ({placeholders})",
        skill_ids
    )

    conn.commit()
    conn.close()


def delete_all_skills():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM skills")

    conn.commit()
    conn.close()


@app.route("/")
def home():
    skills = [
        "[BACKEND] Python",
        "HTML",
        "[DB] SQL",
        "BASH",
    ]
    messages = get_skills()
    return render_template("index.html", skills=skills, messages=messages)


@app.route("/send", methods=["POST"])
def send():
    skill = request.form.get("skill", "").strip()
    level = request.form.get("level", "").strip()
    status = request.form.get("status", "").strip()

    if skill == "" or level == "" or status == "":
        return redirect("/")

    add_skill(skill, level, status)
    return redirect("/")


@app.route("/delete/<int:skill_id>", methods=["POST"])
def delete(skill_id):
    delete_skill(skill_id)
    return redirect("/")


@app.route("/delete_all", methods=["POST"])
def delete_all():
    delete_all_skills()
    return redirect("/")


@app.route("/delete_selected", methods=["POST"])
def delete_selected():
    skill_ids = request.form.getlist("delete_ids")
    delete_selected_skills(skill_ids)
    return redirect("/")


@app.route("/edit/<int:skill_id>")
def edit(skill_id):
    item = get_skill(skill_id)

    if item is None:
        return redirect("/")

    return render_template("edit.html", item=item)


@app.route("/update/<int:skill_id>", methods=["POST"])
def update(skill_id):
    skill = request.form.get("skill", "").strip()
    level = request.form.get("level", "").strip()
    status = request.form.get("status", "").strip()

    if skill == "" or level == "" or status == "":
        return redirect(f"/edit/{skill_id}")

    update_skill(skill_id, skill, level, status)
    return redirect("/")


init_db()


if __name__ == "__main__":
    app.run(debug=True)
