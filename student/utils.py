def calculate_student_info(mssv, student_data):
    """Hàm phụ trợ tính điểm trung bình và xếp loại cho sinh viên"""
    scores = student_data.get("scores", {})
    if scores:
        avg_score = round(sum(scores.values()) / len(scores), 2)
        if avg_score >= 8.5:
            rank = "Xuất sắc"
        elif avg_score >= 7.0:
            rank = "Giỏi"
        elif avg_score >= 5.5:
            rank = "Khá"
        elif avg_score >= 4.0:
            rank = "Trung bình"
        else:
            rank = "Yếu"
    else:
        avg_score = None
        rank = "-"

    return {
        "mssv": mssv,
        "name": student_data["name"],
        "lop": student_data["lop"],
        "avg_score": avg_score,
        "rank": rank
    }