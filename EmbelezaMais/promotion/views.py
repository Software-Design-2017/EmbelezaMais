from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.shortcuts import (
    render, redirect
)


from user.decorators import (
    user_is_company
)

from .forms import (
    PromotionRegisterForm,
    PromotionEditForm
)

from .models import (
    Promotion
)


class PromotionList(ListView):
    model = Promotion
    template_name = 'promotion_list.html'
    context_object_name = 'promotion'
    paginate_by = 10

    def get_queryset(self):
        promotion = Promotion.objects.filter(company=self.request.user.company)
        return promotion

    @login_required
    @user_is_company
    def delete_promotion(request, id):
        promotion = Promotion.objects.get(id=id)
        promotion.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Create your views here.
class PromotionRegister(FormView):
    template_name = 'promotionRegister.html'
    form_class = PromotionRegisterForm
    success_url = '/promotion/list/'

    def dispatch(self, *args, **kwargs):
        return super(PromotionRegister, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.promotion = form.save(commit=False)
        self.promotion.company = self.request.user.company
        self.promotion.save()

        return super(PromotionRegister, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PromotionRegister, self).get_context_data(**kwargs)
        return context


class PromotionEdit(FormView):
    @login_required
    @user_is_company
    def promotion_edit(request, id):
        promotion = Promotion.objects.get(id=id)
        form = PromotionEditForm(request.POST or None, instance=promotion)

        if request.method == "POST":
            if form.is_valid():
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                price = form.cleaned_data.get('price')

                if len(name) != 0:
                    promotion.name = name
                else:
                    pass

                if len(description) != 0:
                    promotion.description = description
                else:
                    pass

                if price >= 0:
                    promotion.price = price
                else:
                    pass

                promotion.save()

                return redirect('promotion_list')
            else:
                pass
        else:
            pass

        return render(request, 'promotionEdit.html', {'form': form, 'promotion': promotion})
