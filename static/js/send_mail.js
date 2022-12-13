$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-mail .modal-content").html("");
        $("#modal-mail").modal("show");
      },
      success: function (data) {
        $("#modal-mail .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-mail").modal("hide");
          $("#modal-contact").modal("show");
        }
        else {
          $("#modal-mail .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-send-mail").click(loadForm);
  $("#modal-mail").on("submit", ".js-send-mail-form", saveForm);

 });