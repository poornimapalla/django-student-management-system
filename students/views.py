from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students
    })


def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            roll_number=request.POST["roll_number"],
            email=request.POST["email"],
            course=request.POST["course"],
            age=request.POST["age"]
        )
        return redirect("student_list")

    return render(request, "students/add_student.html")


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.roll_number = request.POST["roll_number"]
        student.email = request.POST["email"]
        student.course = request.POST["course"]
        student.age = request.POST["age"]
        student.save()

        return redirect("student_list")

    return render(request, "students/edit_student.html", {
        "student": student
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/delete_student.html", {
        "student": student
    })