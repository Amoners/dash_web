 $(document).click(function (e) {
                var v_id = $(e.target).attr('class');
                $("." + v_id).addClass('active');
                });