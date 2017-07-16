$( document ).ready(function() {
    $("#urlForm").submit(function (e) {

        var url = "/shorten/";
        $("#shortUrlPanel").hide();

        $.ajax({
            type: "POST",
            url: url,
            data: $("#urlForm").serialize(),
            dataType: 'json',
            success: function (data) {
                $("#shortUrlPanel").show();
                $("#shortUrl").val(location.href + data.short_url).focus().select();
            }
        });

        e.preventDefault();
    });
});
