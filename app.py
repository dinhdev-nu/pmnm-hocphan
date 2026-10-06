from flask import Flask, render_template, request, jsonify
from student.utils import calculate_student_info

app = Flask(__name__)


STUDENTS = {
    "23T1020001": {"name": "Nguyễn Văn An", "lop": "K47A",
        "scores": {"PMMNM": 8.5, "CSDL": 7.0, "MMT": 9.0}},
    "23T1020002": {"name": "Trần Thị Bình", "lop": "K47A",
        "scores": {"PMMNM": 6.0, "CSDL": 5.5, "MMT": 7.0}},
    "23T1020003": {"name": "Lê Hoàng Cường", "lop": "K47B",
        "scores": {"PMMNM": 9.5, "CSDL": 9.0}},
    "23T1020004": {"name": "Phạm Minh Dũng", "lop": "K47B",
        "scores": {"PMMNM": 4.0, "CSDL": 3.5, "MMT": 5.0}},
    "23T1020005": {"name": "Hoàng Thu Hà", "lop": "K47A",
        "scores": {}},
    "23T1020006": {"name": "Võ Quốc Khánh", "lop": "K47C",
        "scores": {"PMMNM": 7.5, "MMT": 8.0}},
}

@app.route("/")
def index():
    total_students = len(STUDENTS)
    
    classes = sorted(list(set(std["lop"] for std in STUDENTS.values())))
    total_classes = len(classes)
    
    return render_template("index.html", 
                           total_students=total_students, 
                           total_classes=total_classes)

@app.route("/api/students")
def api_students():
    result = [calculate_student_info(mssv, data) for mssv, data in STUDENTS.items()]
    return jsonify(result)

@app.route("/students")
def list_students():
    selected_lop = request.args.get("lop", "").strip()
    
    all_classes = sorted(list(set(std["lop"] for std in STUDENTS.values())))
    
    filtered_students = []
    
    for mssv, data in STUDENTS.items():
        if selected_lop:
            if data["lop"].lower() != selected_lop.lower():
                continue
                
        student_info = calculate_student_info(mssv, data)
        filtered_students.append(student_info)
        
    return render_template("students.html", 
                           students=filtered_students, 
                           classes=all_classes, 
                           selected_lop=selected_lop)

if __name__ == "__main__":
  app.run(debug=True)
