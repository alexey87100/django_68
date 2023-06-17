from django.shortcuts import render
from django.http import Http404
from .data import EMPLOYEES, SKILLS
from datetime import datetime


def index(request):
    """Главная страница."""
    employees = []
    for employee in EMPLOYEES:
        skills = []
        for skill_id in employee['skills']:
            skills.append(SKILLS[skill_id])
        employee_with_skills = employee.copy()
        employee_with_skills['skills'] = skills
        employees.append(employee_with_skills)
    context = {
        'employees': employees,
        'skills': SKILLS
    }

    return render(request, 'index.html', context=context)

def skill(request, skill_id):
    skill = None
    for _skill in SKILLS:
        if _skill['id'] == skill_id:
            skill = _skill
            break
    if skill is None:
        raise Http404('Скила с указанным id не существует')

    employees = []
    for employee in EMPLOYEES:
        if skill_id in employee['skills']:
            employees.append(employee)
    context = {
        'employees': employees,
        'skill': skill,

    }
    return render(request, 'skill.html', context=context)
