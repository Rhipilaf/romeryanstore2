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

function poisk() {
    const term = $('.search-form-txt').val();
    const type = $('.search-form-type').val();
    const platforma = $('.search-form-platformi').val();

    $.ajax({
        type: 'GET',
        url: `/avtodopolnenie/?term=${term}&type=${type}&platforma=${platforma}`,
    }).fail(function () {
        alert('Что-то пошло не так')
    }).then(function (data) {
        $('.card-place').empty();
        if (data.length > 0) {
            data.forEach((i_account) => {
                const verstka = `
                 <div class="card-anim pt-4 col-12 col-md-3 mb-4">
                            <div class="card-img">
                                    <img class="card-img" src="${i_account.img} " style="border-radius: 20px">
                            </div>
                            <div class="card-body-2">
                                <span class="bt"></span>
                                <span class="bt"></span>
                                <span class="bt"></span>
                                <div class="content">
                                    <h5 class="title">${i_account.title}</h5>
                                    <p class="par">${i_account.description}</p>
                                    <a href="/" style="border-radius: 20px">
                                        <i class="bi bi-arrow-right arrow"></i>
                                    </a>
                                </div>
                            </div>
                      </div>
                `
                $('.card-place').append(verstka);
            })
        } else {
            $('.card-place').append(`<p>Сори мой друг. Ничего не найдено=(</p>`);
        }


    });
}

$(function () {
    $('.search-form-txt').keyup(function () {
        poisk()
    })

    $('.search-form-type').change(function () {
        poisk()
    });

    $('.search-form-platformi').change(function () {
        poisk()
    });

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
    $(".avatar-input").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.profile_img').attr('src', e.target.result);
                var data = new FormData();
                data.append('image', $('.avatar-input')[0].files[0]);
                console.log($('.avatar-input')[0].files[0])

                $.ajax({
                    type: 'POST',
                    url: '/change_photo',
                    headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
                    data: data,
                    // contentType: "application/json",
                    dataType: 'json',
                    contentType: false,
                    processData: false,
                })
                    .fail(function () {
                        new UTILS().vivisti_uvedomlenie('Ошибка', 'Уведомление', 'error')
                    })
                    .then(function () {
                        new UTILS().vivisti_uvedomlenie('Фото успешно обновлено', 'Уведомление', 'success')
                    })

            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    $('.profile_img').click(function () {
        $(".avatar-input").click();
    })
})

document.addEventListener('DOMContentLoaded', () => { // Структура страницы загружена и готова к взаимодействию

    const tabs = (tabsSelector, tabsHeadSelector, tabsBodySelector, tabsCaptionSelector, tabsCaptionActiveClass, tabsContentActiveClass) => { // объявляем основную функцию tabs, которая будет принимать CSS классы и селекторы

        const tabs = document.querySelector(tabsSelector) // ищем на странице элемент по переданному селектору основного элемента вкладок и записываем в константу
        const head = tabs.querySelector(tabsHeadSelector) // ищем в элементе tabs элемент с кнопками по переданному селектору и записываем в константу
        const body = tabs.querySelector(tabsBodySelector) // ищем в элементе tabs элемент с контентом по переданному селектору и записываем в константу

        const getActiveTabName = () => { // функция для получения названия активной вкладки
            return head.querySelector(`.${tabsCaptionActiveClass}`).dataset.tab // возвращаем значение data-tab активной кнопки
        }

        const setActiveContent = () => { // функция для установки активного элемента контента
            if (body.querySelector(`.${tabsContentActiveClass}`)) { // если уже есть активный элемент контента
                body.querySelector(`.${tabsContentActiveClass}`).classList.remove(tabsContentActiveClass) // то скрываем его
            }
            body.querySelector(`[data-tab=${getActiveTabName()}]`).classList.add(tabsContentActiveClass) // затем ищем элемент контента, у которого значение data-tab совпадает со значением data-tab активной кнопки и отображаем его
        }

        // проверяем при загрузке страницы, есть ли активная вкладка
        if (!head.querySelector(`.${tabsCaptionActiveClass}`)) { // если активной вкладки нет
            head.querySelector(tabsCaptionSelector).classList.add(tabsCaptionActiveClass) // то делаем активной по-умолчанию первую вкладку
        }

        setActiveContent(getActiveTabName()) // устанавливаем активный элемент контента в соответствии с активной кнопкой при загрузке страницы

        head.addEventListener('click', e => { // при клике на элемент с кнопками
            const caption = e.target.closest(tabsCaptionSelector) // узнаем, был ли клик на кнопке
            if (!caption) return // если клик был не на кнопке, то прерываем выполнение функции
            if (caption.classList.contains(tabsCaptionActiveClass)) return // если клик был на активной кнопке, то тоже прерываем выполнение функции и ничего не делаем

            if (head.querySelector(`.${tabsCaptionActiveClass}`)) { // если уже есть активная кнопка
                head.querySelector(`.${tabsCaptionActiveClass}`).classList.remove(tabsCaptionActiveClass) // то удаляем ей активный класс
            }

            caption.classList.add(tabsCaptionActiveClass) // затем добавляем активный класс кнопке, на которой был клик

            setActiveContent(getActiveTabName()) // устанавливаем активный элемент контента в соответствии с активной кнопкой
        })
    }

    tabs('.section__tabs', '.tabs__head', '.tabs__body', '.tabs__caption', 'tabs__caption_active', 'tabs__content_active') // вызываем основную функцию tabs для синих вкладок .section__tabs

    tabs('.about__tabs', '.tabs__head', '.tabs__body', '.tabs__caption', 'tabs__caption_active', 'tabs__content_active') // вызываем основную функцию tabs для зелёных вкладок .about__tabs

})

var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 4,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true
});
$('.play').on('click', function () {
    owl.trigger('play.owl.autoplay', [1000])
})
$('.stop').on('click', function () {
    owl.trigger('stop.owl.autoplay')
})

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplayTimeout: 3000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})
// var randomScrolls = Math.floor(Math.random() * 5) + 1;

// При нажатии кнопки запускаем карусель на случайное количество прокруток
// document.getElementById('start-carousel').addEventListener('click', function () {
//     $('.owl-carousel').trigger('owl.carousel', [randomScrolls]);
// });

