from hostel.models import Block
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def index_view(request):
    return render(request, "dashboard/index.html")


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def hostel_view(request):
    blocks = Block.objects.filter(level=request.user.level)

    context = {"blocks": blocks}
    return render(request, "dashboard/hostel.html", context)
