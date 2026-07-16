from django.shortcuts import render, get_object_or_404
from .models import Level, Myth
def index(request):
    """Главная страница сайта"""
    return render(request, 'archive/index.html')
def levels_list(request):
    """Страница со всеми уровнями айсберга"""
    levels = Level.objects.all().order_by('depth_score')
    return render(request, 'archive/levels_list.html', {'levels':levels})
def level_detail(request, level_id):
    """Страница конкретного уровня айсберга"""
    level = get_object_or_404(Level, id=level_id)
    myths = Myth.objects.filter(level=level)
    return render(request, 'archive/level_detail.html', {'level': level, 'myths': myths})

