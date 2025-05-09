from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from cars.models import Car


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('car_list')
    else:
        user_form = UserCreationForm()

    return render(
        request,
        'register.html',
        {'user_form': user_form}
    )


@login_required
def profile_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    favorite_cars = request.user.favorite_cars.all()
    return render(request, 'profile.html', {
        'form': form,
        'favorite_cars': favorite_cars
    })


@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.favorited_by.filter(id=request.user.id).exists():
        car.favorited_by.remove(request.user)
        messages.success(request, 'Carro removido dos favoritos.')
    else:
        car.favorited_by.add(request.user)
        messages.success(request, 'Carro adicionado aos favoritos.')
    return redirect('car_list')
