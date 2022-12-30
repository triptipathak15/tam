$(function() {
    $('#list_table').DataTable();
    $('#manager_table').DataTable();
});

function reload(){
    location.reload()
}
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
       $.ajax({
        url : '/change_request_status',
        data : { leave_request_ids : result.join(), status : new_status},
        success : function(value) {
            $("#confirmation_modal").show()
        }
    });
}

function cancel_request() {

}