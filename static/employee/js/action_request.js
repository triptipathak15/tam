$(function() {
    $('.table').DataTable();
    var nav = document.getElementById('sidebar_ul')
    var anchor = nav.getElementsByTagName('a')
    var current = window.location.pathname.split('/')[1];
    for (var i = 0; i < anchor.length; i++) {
        split_array = anchor[i].href.split('/')
        selected = split_array[split_array.length-1]
        if(selected == current) {
        console.log(anchor[i])
            anchor[i].className="active nav-link"
        }
    }
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