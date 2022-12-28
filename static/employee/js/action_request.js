
function perform_manager_action(button_id) {
      var result = []
      var status_mapper = { 'btn_approve':'Approved','btn_deny':'Denied','btn_cancel':'Cancelled'}
      new_status = status_mapper[button_id]
      $('input:checkbox:checked').each(function() {
        var row = [];
        $(this).closest('tr').children(':first').each(function(){
          row.push($(this).text());
        });
        result.push(row[0]);
      });
      console.log(result.join())

       $.ajax({
        url : '/change_request_status',
        data : { leave_request_ids : result.join(), status : new_status},
        success : function(value) {
           $('#confirmation_modal').addClass("active")
           location.reload()
        }
    });
}

function cancel_request() {

}