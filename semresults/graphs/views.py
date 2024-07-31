from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')  # Set the backend before importing pyplot
import matplotlib.pyplot as plt
from django.conf import settings
from io import BytesIO
import base64
from .models import students

def semmarks(request):
    return render(request, 'semmarks.html')

def check_float(val, default=0.0):
    try:
        return float(val)
    except ValueError:
        return default

def getmarks(request):
    if request.method == 'GET':
        stu1 = students()
        # Retrieve semester marks from GET request
        stu1.name = request.GET['name']
        stu1.sem1 = check_float(request.GET.get('sem1', 0))
        stu1.sem2 = check_float(request.GET.get('sem2', 0))
        stu1.sem3 = check_float(request.GET.get('sem3', 0))
        stu1.sem4 = check_float(request.GET.get('sem4', 0))
        stu1.sem5 = check_float(request.GET.get('sem5', 0))
        stu1.sem6 = check_float(request.GET.get('sem6', 0))
        stu1.sem7 = check_float(request.GET.get('sem7', 0))
        stu1.sem8 = check_float(request.GET.get('sem8', 0))

        # Save the student instance to the database
        stu1.save()

        # List of semester marks
        lis = [stu1.sem1, stu1.sem2, stu1.sem3, stu1.sem4, stu1.sem5, stu1.sem6, stu1.sem7, stu1.sem8]
        semesters = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7', 'Sem 8']

        # Create Line Graph
        fig_line, ax_line = plt.subplots()
        ax_line.plot(semesters, lis, marker='o', linestyle='-', color='b')
        ax_line.set_title('Semester Score - Line Graph')
        ax_line.set_xlabel('Semesters')
        ax_line.set_ylabel('Marks')
        plt.xticks(rotation=45)

        # Save line graph to BytesIO
        buffer_line = BytesIO()
        plt.savefig(buffer_line, format='png')
        buffer_line.seek(0)
        img_str_line = base64.b64encode(buffer_line.getvalue()).decode('utf-8')
        plt.close(fig_line)

        # Create Pie Chart
        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(lis, labels=semesters, autopct='%1.1f%%', startangle=140)
        ax_pie.set_title('Semester score - Pie Chart')

        # Save pie chart to BytesIO
        buffer_pie = BytesIO()
        plt.savefig(buffer_pie, format='png')
        buffer_pie.seek(0)
        img_str_pie = base64.b64encode(buffer_pie.getvalue()).decode('utf-8')
        plt.close(fig_pie)

        # Pass both image strings to the template
        return render(request, 'showgraphs.html', {'img_str_line': img_str_line, 'img_str_pie': img_str_pie, 'name': stu1.name})
