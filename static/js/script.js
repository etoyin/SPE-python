$(document).ready(function(){
	//var promDiv = $('#promDiv');
	var i = $('#promDiv tr').size() + 1;

	$('#addProm').live('click', function(){
		$("#promDiv").append('<tr><td><label>Date of Promotion/Advancement:</label></td><td><input type="number" name="datePromotion'+i+'" value=""></td><td><label>Level of Promotion.</label></td><td><input type="number" name="levelProm'+i+'" value=""></td><td><a href="#" id="remInput">Remove</a></td></tr>');
		i++;
		
		return false;
	});
	$("#remInput").live('click', function(){
	  if(i > 2){
	    $(this).parents('tr').remove();
	            //i--;
	            //console.log(i);
	   }
	  return false;
	});
});