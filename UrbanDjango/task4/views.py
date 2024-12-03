from django.shortcuts import render
from django.views.generic import TemplateView


class PageMain(TemplateView):
    template_name = 'fourth_task/main.html'

    def get_context_data(self, **kwargs):
        context = super(PageMain, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class Shop(TemplateView):
    template_name = 'fourth_task/shop.html'

    def get_context_data(self, **kwargs):
        context = super(Shop, self).get_context_data(**kwargs)
        context['games'] = {
            'pc_games': ["Atomic Heart", "Cyberpunk 2077"],
            'board_games': ['Catan', 'Brass']}
        context['title'] = 'Магазин'
        return context


class Basket(TemplateView):
    template_name = 'fourth_task/basket.html'

    def get_context_data(self, **kwargs):
        context = super(Basket, self).get_context_data(**kwargs)
        context['title'] = 'Корзина'
        return context
