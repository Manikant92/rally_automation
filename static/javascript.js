$document.ready(function (){
      $("#create_task").change(function() {
                if ($(this).val() == "Yes") {
                    $("#task_names").show();
                }else{
                    $("#task_names").hide();
                }
            });
        });