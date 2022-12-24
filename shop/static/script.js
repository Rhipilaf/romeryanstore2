class UTILS {

    vivisti_uvedomlenie(telo, zagolovok = 'Уведомление', type = 'success', delay = 2000) {

        const uvedomlenie = $('#uvedomlenie');
        uvedomlenie.find('.uvedomlenie-header').removeClass('bg-info').removeClass('bg-danger').removeClass('text-dark').removeClass('text-light');
        if (type === 'success') {
            uvedomlenie.find('.uvedomlenie-header').addClass('bg-info').addClass('text-dark');
        }
        if (type === 'error') {
            uvedomlenie.find('.uvedomlenie-header').addClass('bg-danger').addClass('text-light');
        }
        uvedomlenie.find('.uvedomlenie-title').html(zagolovok);
        uvedomlenie.find('.uvedomlenie-telo').html(telo);

        uvedomlenie.toast({delay: delay}).toast('show');

    }
}
$(function (){



    $('.modal-login').submit(function (e) {
            e.preventDefault();
            const self = this;

            let data = {};
            $.each($(self).serializeArray(), function (i, field) {
                data[field.name] = field.value;
            });

            $.ajax({
                type: 'POST',
                url: self.action,
                headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
                data: JSON.stringify(data),
                contentType: "application/json",
                dataType: 'json'
            }).fail(function () {
                new UTILS().vivisti_uvedomlenie('Ошибка авторизации', 'Уведомление', 'error')
            }).then(function () {
                window.location.href = '/';
            });
        });

        $('.modal-reg').submit(function (e) {
            e.preventDefault();
            const self = this;

            let data = {};
            $.each($(self).serializeArray(), function (i, field) {
                data[field.name] = field.value;
            });

            $.ajax({
                type: 'POST',
                url: self.action,
                headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
                data: JSON.stringify(data),
                contentType: "application/json",
                dataType: 'json'
            }).fail(function (req) {
                  if (req.responseJSON) {
                    new UTILS().vivisti_uvedomlenie(req.responseJSON.text, 'Уведомление', 'error')
                } else {
                   new UTILS().vivisti_uvedomlenie('Непредвиденная ошибка. Попробуйте ещё раз', 'Уведомление', 'error')
                }
            }).then(function () {
                window.location.href = '/';
            });
        });
})

