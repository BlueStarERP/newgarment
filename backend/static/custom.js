
// console.log('hello custome wirk');

$(document).ready(function(){

    
      new DataTable('.table1');

      new DataTable('.table2', {
    layout: {
        topStart: {
            buttons: [
              'copy', 'csv', 'excel', 'pdf', 'print',
            //   {
            //         text: 'Green',
            //         className: 'green',
            //         action: function (e, dt, node, config) {
            //             alert('Button activated');
            //         }
            //     }
              
            ]   
        }
        
    }

});
  
// alert('hello workd');

//Deptment Delete
$("#deptList").on('click', '.delBtn', function() {
    var currenttr = $(this).closest(".depttr");
    var lid = currenttr.find(".lid").html();
    // console.log(lid);
    $.ajax({
    url: "/hrm/department_delete/"+lid,
    method: "GET",
    data:{lid:lid},
    success: function(data){
  
        alert('Department Deleted...');
        window.setTimeout(function(){ } ,100);
                        location.reload();      
    },
    error:function(){
        alert('Error contact to 09-969255445');
    },
                    
  });//end ajax
});//Deptment Deleted






});//ready function end