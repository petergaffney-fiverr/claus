  let check=0;
        function reset(){
            $('.b_form,.b_btn_1,.s_btn_1,.type_1,.b_email,.b_pass1,.b_pass2,.b_check,.b_next,.b_back,.b_submit,.b_email_error').css('display','none');

            $('.s_form,.b_btn_2,.s_btn_2,.type_2,.s_email,.s_pass1,.s_pass2,.s_check,.s_next,.s_back,.s_submit').css('display','none');
            $('.b_pass_error').css('display','none');
            $('.s_pass_error').css('display','none');

        }
        $(document).on('click','.b_next',function(e){
            e.preventDefault();
            reset();
            check=0;
            $('.b_form').css('display','');
            $('.type_1').css('display','');
            $('.b_pass1').css('display','');
            $('.b_pass2').css('display','');
            $('.b_back').css('display','');
            $('.b_check').css('display','');
            $('.b_submit').css('display','');
   
        });
        $(document).on('click','.s_next',function(e){
            e.preventDefault();
            reset();
            check=1;
            $('.s_form').css('display','');
            $('.type_2').css('display','');
            $('.s_pass1').css('display','');
            $('.s_pass2').css('display','');
            $('.s_back').css('display','');
            $('.s_check').css('display','');
            $('.s_submit').css('display','');
        });
        $(document).on('click','.b_back',function(e){
            e.preventDefault();
            reset();
            $('.b_form').css('display','');
            $('.b_email').css('display','');
            $('.b_next').css('display','');

            $('.b_btn_1').css('display','');
            $('.s_btn_1').css('display','');
        });
        $(document).on('click','.s_back',function(e){
            e.preventDefault();
            reset();
            $('.s_form').css('display','');
            $('.s_email').css('display','');
            $('.s_next').css('display','');

            $('.b_btn_2').css('display','');
            $('.s_btn_2').css('display','');
        });

        $(document).on('click','.b_btn_1',function(e){
            e.preventDefault();
            reset();
            $('.b_form').css('display','');

            $('.b_btn_1').css('display','');
            $('.s_btn_1').css('display','');

            $('.b_email').css('display','');
            $('.b_next').css('display','');
        });

        $(document).on('click','.b_btn_2',function(e){
            e.preventDefault();
            reset();
            $('.b_form').css('display','');

            $('.b_btn_1').css('display','');
            $('.s_btn_1').css('display','');

            $('.b_email').css('display','');
            $('.b_next').css('display','');
        });


        $(document).on('click','.s_btn_1',function(e){
            e.preventDefault();
            reset();
            $('.s_form').css('display','');

            $('.b_btn_2').css('display','');
            $('.s_btn_2').css('display','');

            $('.s_email').css('display','');
            $('.s_next').css('display','');
        });

        $(document).on('click','.s_btn_2',function(e){
            e.preventDefault();
            reset();
            $('.s_form').css('display','');

            $('.b_btn_2').css('display','');
            $('.s_btn_2').css('display','');

            $('.s_email').css('display','');
            $('.s_next').css('display','');
        });