from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class platform(TemplateView):
    template_name = 'third_task/platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'

        return context


class Cart(TemplateView):
    template_name = 'third_task/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Игры'

        context['text'] = 'Извините, ваша корзина пуста'
        return context


class Games(TemplateView):
    template_name = 'third_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Игры'
        context['buy'] = 'Купить'
        context['g1'] = 'Portal 2'
        context['g2'] = 'Limbus Company'
        context['g3'] = 'Payday 3'
        return context
