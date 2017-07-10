$( document ).ready(function() {
    $("#urlForm").submit(function (e) {

        var url = "/shorten/";
        $("#shortUrlPanel").hide();

        $.ajax({
            type: "POST",
            url: url,
            data: $("#urlForm").serialize(),
            success: function (data) {
                $("#shortUrlPanel").show();
                $("#shortUrl").text(data);
            }
        });

        e.preventDefault();
    });
});
