$(function () {

  /* Functions */

  var showService = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-service .modal-content").html("");
        $("#modal-service").modal("show");
      },
      success: function (data) {
        $("#modal-service .modal-content").html(data.html_show);
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
          $("#service-table tbody").html(data.html_service_list);
          $("#modal-service").modal("hide");
        }
        else {
          $("#modal-service .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */


  $("#service-table").on("click", ".js-show-service", showService);
  // Create service
  // $(".js-create-service").click(loadForm);
  // $("#modal-service").on("submit", ".js-service-create-form", saveForm);
  //
  // // Update service
  // $("#service-table").on("click", ".js-update-service", loadForm);
  // $("#modal-service").on("submit", ".js-service-update-form", saveForm);
  //
  // // Delete service
  // $("#service-table").on("click", ".js-delete-service", loadForm);
  // $("#modal-service").on("submit", ".js-service-delete-form", saveForm);

});
