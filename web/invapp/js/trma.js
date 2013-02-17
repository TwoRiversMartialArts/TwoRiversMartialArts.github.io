// Set up a place for func and data objects to live
jQuery.trma = { pyurl : '/cgi-bin/recpt.py' };

jQuery(function($){
$("#TRMA_UI_TABS").tabs();
$("#TRMA_UI").hide();
var pyurl = $.trma.pyurl || '/cgi-bin/recpt.py';
var dpOps = { onSelect: function() { this.focus(); } };
var uid = "";
var pwd = "";
//-----------------------------------------------------------
$("#log_in_dlg").dialog({
  width : 600,height : 300,
  buttons: {
    OK : function() {
       var dlg = $(this); 
       $("#log_in_msg").text("Trying...");
       uid = $("#auth_uid").val().trim();
       pwd = $("#auth_pwd").val().trim();
       var params = { uid:uid,pwd:pwd,action: "log_in" }; 
       $.ajax({url:pyurl,data:params,
          type:"POST",dataType:"json",
          error:function() {
             $("#log_in_msg").text("Error, try clicking OK again...");
          },
          success: function(data) {
             if( data.msg != "SUCCESS" ) {
               $("#log_in_msg").text(data.msg);
               setTimeout(function(){$("#log_in_msg").text("Try again")},2000);
               return;
             }
             uid = data.uid; pwd = '';
             dlg.dialog("close");
             if( data.needemail ) { $("#email_dlg").dialog("open"); }
             else $("#TRMA_UI").show();
        }}); 
    }}});
//-----------------------------------------------------------
var addnote_txt = {recpt:"",stock:""};
var addnote_which = "";
$("#addnote_dlg").dialog({autoOpen:false,width:600,height:450,
    buttons: { OK:function() {
       addnote_txt[addnote_which] = $("#noteText").val();
       $(this).dialog("close"); } } });
function addnote(valnm) {
   $("#noteText").val(addnote_txt[valnm]);
   addnote_which = valnm;
   $("#addnote_dlg").dialog("open");
};
//----
$("#recpt_add_note").click(function() { addnote("recpt"); });
$("#stk_add_note").click(function() { addnote("stock"); });
    
//-----------------------------------------------------------
$("#email_dlg").dialog({autoOpen:false,width:600,
    buttons: {OK:function() {
       var dlg=$(this);
       $.ajax({url:pyurl,
          data:{action:"email",uid:uid,email:$("#email_addr").val()},
          type:"POST",dataType:"json",
          success: function(data) {
             if( data.msg != "SUCCESS" ) {
               $("#email_msg").text(data.msg);
               return;
             }
             dlg.dialog("close");
             $("#TRMA_UI").show();
        }}); 
      },Cancel:function(){ $(this).dialog("close"); }
    }});
//-----------------------------------------------------------
$("#rpemail_dlg").dialog({autoOpen:false,width:600,
    buttons: {
       OK:function() {
       var dlg=$(this);
       $.ajax({url:pyurl,
          data:{action:"rpemail",uid:uid,
            name: $("#rpname").val(),email:$("#rpemail_addr").val()},
          type:"POST",dataType:"json",
          success: function(data) {
             if( data.msg != "SUCCESS" ) {
               $("#rpemail_msg").text(data.msg);
               return;
             }
             $("#rpname").val("");$("#rpemail_addr").val("");
             dlg.dialog("close");
        }}); 
      },Cancel:function(){ $("#rpname").val("");$("#rpemail_addr").val("");
                            $(this).dialog("close"); }
    }});
//-----------------------------------------------------------
var beltpull_names = [];
$("#beltpull_dlg").dialog({autoOpen:false,width:650,modal:true,
   buttons:{Cancel:function(){ $(this).dialog("close"); },
     OK:function(){ var dlg=$(this);
        var p = {uid:uid,dt:$("#stk_date").val(),
           names:beltpull_names.join(",")};
        $.each(beltpull_names,function(i,v) {
           var val = $("#"+v).val();
           if(val.length>0) p[v] = val;
        });
        dlg.dialog("close");
        p.action = 'beltpull';
        $.ajax({url:pyurl,data:p,
            type:'POST',dataType:'json',
            success:function(data) {
               $("#stk_msg").text(data.msg);
            }});
     }}
  });
//-----------------------------------------------------------
$("#beltpull_btn").click(function(){
   $("#beltpull_inner").empty();
   $("#stk_msg").text("");
   if( ! $("#stk_date").val() ) {
      $("#stk_msg").text("Must set a date before entering belt pull numbers");
      return;
   }
   $.ajax({url:pyurl,data:{action:"beltdlg"},type:"POST",
     dataType:"json",success:function(data) {
       $("#beltpull_inner").html(data.html);
       beltpull_names = data.names;
       $(".blt_num_inp").autoNumeric({aSep:'',vMin:0,mDec:0});
       $("#beltpull_dlg").dialog("open");
     }});
});
//-----------------------------------------------------------
function commit() {
  var p = getData();
  p["action"] = "store";
  p["uid"] = uid;
  $.ajax({
     url:pyurl,data:p,
     type:'POST',
     dataType: 'json',
     success: function(data) {
        $("#commit_result").text( data.msg );
        $("#recpt_revcount").text( data.cnt );
        $("#recpt_revno").text( data.cnt );
        setTimeout(function(){$("#commit_result").text("")},5000);
     }
  });
}

//-----------------------------------------------------------
function search(revno) {
  var p = getData();
  p["recpt_revno"] = revno;
  p["action"] = "search";
  var d = { recpt_no : p.recpt_no }
  putData(d);
  $.ajax({
     url:pyurl,data:p,
     type:'POST',
     dataType: 'json',
     success: function(data) {
        $("#commit_result").text( data.msg );
        setTimeout(function(){$("#commit_result").text("")},5000);
        if( data.data ) { 
           putData(data.data);        
           disable("recpt_search");
           disable("recpt_no");
        }
     }
  });
}
   
//-----------------------------------------------------------
var recptFields = ["recpt_item","recpt_qty"];
var reconFields = ["recon_item","recon_rqty","recon_pqty",
                   "recon_chkn","recon_paid","recon_pdate","recon_rdate"];
var hdrFields = ["recpt_no","recpt_date","recpt_branch",
                 "recpt_outby","recpt_recvby"];
function getData() {
   var d={};
   d.note = addnote_txt.recpt;
   $.each(hdrFields,function(i,v){ d[v] = $("#"+v).val(); });
   $.map({recpt:recptFields,recon:reconFields},function(flds,nm) {
      $("#"+nm+"_rows tbody tr").each( function(n) {
         $.each(flds,function(i,v){
           d[v+n] = $("#"+v+n).val();
         });
      });
   });
   return d;
}
//-----------------------------------------------------------
function putData(d) {
   $("table.varrows tbody").empty();
   $("#recpt_revcount").text(d.recpt_revcount || "0");
   $("#recpt_revno").text(d.recpt_revno || "0");
   addnote_txt.recpt = d.note || "";
   $.each(hdrFields,function(i,v){ $("#"+v).val(d[v] || ''); });
   $.map({recpt:recptFields,recon:reconFields},function(flds,nm) {
      var n = 0;
      while(true) {
         if( d[nm+"_item"+n] ) {
            if(nm=="recpt") addRecptRow();else addReconRow();
            $.map( flds, function(fld) {
               var fldn = fld+n;
               $("#"+fldn).val( d[fldn] ); });
            n=n+1;
         } 
         else { break; }
      }
   });
}
//-----------------------------------------------------------
function changeRev(n) {
   var rno = $("#recpt_revno").text().trim();
   var maxno = $("#recpt_revcount").text().trim();
   if( rno.length>0 && maxno.length>0) {
      var nn = parseInt(rno) + n;
      maxno = parseInt(maxno);
      if( nn <= maxno && nn > 0 ) {
         search(""+nn);
      }
   }
}
//-----------------------------------------------------------
$("#rev_minus").click(function() { changeRev(-1); });
//-----------------------------------------------------------
$("#rev_plus").click(function() { changeRev(1); });
//-----------------------------------------------------------
function addRecptRow() {
   var tbl=$("#recpt_rows");
   var nrows=$("tbody tr",tbl).length;
   var newrow="<tr id=\"recpt_row" + nrows + "\" >"+
     "<td><input id=\"recpt_item"+nrows+"\" size=\"32\"/></td>"+
     "<td><input id=\"recpt_qty"+nrows+"\" size=\"6\" class=\"qty\"/></td>"+
     "</tr>";
   newrow = $(newrow);
   tbl.append( newrow );
   $("#recpt_row"+nrows+" .qty").autoNumeric({aSep:'',mDec:0});
   $("#recpt_item"+nrows).autocomplete(
      {serviceUrl:pyurl,
       params: { action:'suggitem' },
       minChars:2,width:450});
}
//-----------------------------------------------------------
function addReconRow() {
   var tbl=$("#recon_rows");
   var nrows=$("tbody tr",tbl).length;
   var newrow="<tr id=\"recon_row" + nrows +"\" >"+
     "<td><input id=\"recon_item"+nrows+"\" size=\"32\"/></td>"+
     "<td><input id=\"recon_rqty"+nrows+"\" size=\"6\" class=\"qty\" /></td>"+
     "<td><input id=\"recon_rdate"+nrows+"\" size=\"9\" class=\"inp_date\" /></td>"+
     "<td><input id=\"recon_pqty"+nrows+"\" size=\"6\" class=\"qty\" /></td>"+
     "<td><input id=\"recon_chkn"+nrows+"\" size=\"6\" class=\"inp_chkn\" /></td>" +
     "<td><input id=\"recon_paid"+nrows+"\" size=\"9\" class=\"currency\" /></td>"+
     "<td><input id=\"recon_pdate"+nrows+"\" size=\"12\" class=\"inp_date\" /></td>"+
     "</tr>";
   newrow = $(newrow);
   tbl.append( newrow );
   $("#recon_row"+nrows+" .inp_date").datepicker(dpOps); 
   $("#recon_row"+nrows+" .qty").autoNumeric({mDec:0,aSep:''}); 
   $("#recon_row"+nrows+" .currency").autoNumeric({aSep:'',aSign:"$",mDec:2}); 
   $("#recon_item"+nrows).autocomplete(
      {serviceUrl:pyurl,
       params : {action : 'suggitem'},
       minChars:2,width:450});
}
function rptSimple(method,data) {
   var params = data || {};
   params.action = method;
   $.ajax({ url:pyurl,type:"POST",
            data:params,
            dataType:"JSON",
            success: function(data) {
              $("#report_out_grid").empty();
              if(data.txt) {
                $("#report_out_txt").show();
                $("#reportText").val(data.txt);
              } else {
                 $("#report_out_txt").hide();
                 $("#report_out_grid").html('<table id="report_out_tbl"></table>');
                 var tbl = $("#report_out_tbl");
                 tbl.flexigrid($.extend({dataType:'json'},data.grid));
                 tbl[0].p.params=data.param
                 tbl[0].p.url = pyurl;
                 tbl.flexReload();
              }
            }
          });
}
//-----------------------------------------------------------
$("#stk_search").click(function() {
   addnote_txt.stock = "";
   var p = {action:"stock_search",item:$("#stk_item").val() };
   $.ajax({ url:pyurl,type:"POST",data:p,
            dataType:"JSON",
            success: function(data) {
              var msg = "Currently " + data.count + " in stock";
              if(data.reord) { msg += ", reorder level is " + data.reord; } 
              $("#stk_cnt").text(msg);
          }});
});
//-----------------------------------------------------------
$("#stk_commit").click(function() {
  $("#stk_msg").text("");
  var p = {action:"stock_store",dt:$("#stk_date").val(),
       addqty:$("#stk_add").val(),setqty:$("#stk_set").val(),
       item:$("#stk_item").val(),uid:uid,
       note: addnote_txt.stock.trim(),
       reord:$("#stk_reord").val() };
  if( p.dt && (p.addqty || p.setqty || p.reord) && p.item ) {
     $.ajax({
        url:pyurl,data:p,type:'POST',dataType:'json',
        success: function(data) {
           $("#stk_msg").text( data.msg );
           $(".stknum").val("");
           addnote_txt.stock = "";
           setTimeout(function(){$("#stk_msg").text("")},5000);
        }
     });
  }
});
//-----------------------------------------------------------
$("#admin_adduser").click(function(){
  var user=$("#admin_user").val().trim();
  var pass=$("#admin_pwd").val().trim();
  var p={action:"adduser",uid:uid,newid:user,pass:pass}
  if( p.newid && p.pass ) {
    $.ajax({url:pyurl,data:p,type:'POST',dataType:'json',
    success:function(data) {
         $("#admin_msg").text(data.msg);
         setTimeout(function(){$("#admin_msg").text("")},5000);
      }});
  }
});
//-----------------------------------------------------------
function enable(x) { $("#"+x).removeAttr("disabled"); }
function disable(x) { $("#"+x).attr("disabled","disabled"); }
//-----------------------------------------------------------
$("#recpt_addrow").click(addRecptRow);
$("#recon_addrow").click(addReconRow);
$("#commit_btn").click(commit);
$("#recpt_search").click(function() { search(""); } );
$("#recpt_new").click(function() { putData({});
    $.ajax({url:pyurl,data:{action:'nextRecptNum'},type:'POST',dataType:'json',
    success:function(data) {$("#recpt_no").val(data.num);}});
    enable("recpt_no");disable("recpt_search");
    addRecptRow(); addReconRow(); });
$("#recpt_clear").click(function() { putData({}); 
    enable("recpt_search"); enable("recpt_no"); });
$(".inp_date").datepicker(dpOps);
$(".qty").autoNumeric({aSep:'',vMin:-9999999,mDec:0});
$("#recpt_branch").autocomplete(
   {serviceUrl:pyurl,
    params: { action:'suggbranch' },
    minChars:2,width:300});
$("#recpt_outby").autocomplete(
   {serviceUrl:pyurl,
    params: { action:'suggperson' },
    minChars:2,width:300});
$("#recpt_recvby").autocomplete(
   {serviceUrl:pyurl,
    params: { action:'suggperson' },
    minChars:2,width:300});
$("#rpname").autocomplete(
   {serviceUrl:pyurl,
    params: { action:'suggperson' },
    minChars:2,width:300});
$("#stk_item").autocomplete(
      {serviceUrl:pyurl,
       params : {action : 'suggitem'},
       minChars:2,width:450});
$("#reportOpen").click(function(){rptSimple("rptOpen_g");});
$("#reportByBranch").click(function(){rptSimple("rptBranch_g");});
$("#reportStockLevels").click(function(){rptSimple("rptStock_g");});
$("#reportReorder").click(function(){rptSimple("rptReord_g");});
$("#reportSQL").click(function(){rptSimple("rptSQL",
     {uid:uid,sql:$("#reportText").val()});});
$("#admin_email").click(function() { $("#email_dlg").dialog("open"); } );
$("#admin_rpemail").click(function() { $("#rpemail_dlg").dialog("open"); } );

$("#admin_bkupdb").click(function(){
   $("#admin_msg").text("Trying . . .");
   $.ajax({url:pyurl,data:{action:'backupDB'},type:'POST',dataType:'json',
    success:function(data) {
         $("#admin_msg").text(data.msg);
         setTimeout(function(){$("#admin_msg").text("")},5000);
      }});
    });
    
});
