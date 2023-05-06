from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Breach, Device, BreachReport
from .forms import BreachForm

# @login_required
# @staff_member_required
# def breach_add(request):
#     if request.method == 'POST':
#         form = BreachForm(request.POST)
#         if form.is_valid():
#             breach = form.save(commit=False)
#             breach.save()
#             return redirect('breach_list')
#     else:
#         form = BreachForm()
#     return render(request, 'mobile_breach/breach_add.html', {'form': form})


@login_required
def home(request):
    devices = Device.objects.filter(user=request.user)
    breaches = Breach.objects.filter(device__in=devices)
    return render(request, "home.html", {"breaches": breaches})


@staff_member_required
def breach_list(request):
    breaches = Breach.objects.all()
    return render(request, "breach_list.html", {"breaches": breaches})


@login_required
def breach_add(request):
    if request.method == "POST":
        form = BreachForm(request.POST)
        if form.is_valid():
            device_id = form.cleaned_data["device_id"]
            description = form.cleaned_data["description"]
            breach_type = form.cleaned_data["breach_type"]
            prevention_steps = form.cleaned_data["prevention_steps"]
            device, created = Device.objects.get_or_create(
                device_id=device_id, defaults={"description": description}
            )
            breach = Breach.objects.create(
                device=device,
                breach_type=breach_type,
                prevention_steps=prevention_steps,
            )
            return redirect("breach_list")
    else:
        form = BreachForm()
    return render(request, "breach_add.html", {"form": form})
