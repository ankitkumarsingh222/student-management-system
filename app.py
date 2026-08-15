from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "student-management-secret-key"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "student_management"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def index():
    search = request.args.get("search", "").strip()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if search:
        cursor.execute("""
            SELECT * FROM students
            WHERE name LIKE %s
               OR email LIKE %s
               OR department LIKE %s
               OR roll_no LIKE %s
            ORDER BY id DESC
        """, tuple([f"%{search}%"] * 4))
    else:
        cursor.execute("SELECT * FROM students ORDER BY id DESC")

    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", students=students, search=search)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        data = (
            request.form["roll_no"],
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["department"],
            request.form["year"],
            request.form["address"]
        )

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO students
                (roll_no, name, email, phone, department, year, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, data)
            conn.commit()
            flash("Student added successfully.", "success")
        except Error as e:
            conn.rollback()
            flash(f"Error: {e}", "danger")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for("index"))

    return render_template("student_form.html", student=None, title="Add Student")

@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        data = (
            request.form["roll_no"],
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["department"],
            request.form["year"],
            request.form["address"],
            student_id
        )

        cursor.execute("""
            UPDATE students
            SET roll_no=%s, name=%s, email=%s, phone=%s,
                department=%s, year=%s, address=%s
            WHERE id=%s
        """, data)
        conn.commit()
        cursor.close()
        conn.close()

        flash("Student updated successfully.", "success")
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()

    if not student:
        flash("Student not found.", "danger")
        return redirect(url_for("index"))

    return render_template("student_form.html", student=student, title="Edit Student")

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        flash("Student deleted successfully.", "success")
    except Error as e:
        conn.rollback()
        flash(f"Error: {e}", "danger")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("index"))

@app.route("/student/<int:student_id>")
def student_details(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()

    if not student:
        flash("Student not found.", "danger")
        return redirect(url_for("index"))

    return render_template("student_details.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)
