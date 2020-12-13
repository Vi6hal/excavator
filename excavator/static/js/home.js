$( document ).ready(function() 
{
	M.AutoInit();
	var BASE_URL = $(location).attr("origin");
	var csrfmiddlewaretoken=$("input[name=csrfmiddlewaretoken]").val()
	function async_updateinfo()
	{
		var managing_code=$('#track_code').text();
		if(managing_code == undefined |managing_code == ''){}
		else{
			fetchRecords(managing_code)
		}

	}
	$('#refresh_logs').on("click",function(e)
	{
		async_updateinfo();
	});
   function formPOSTHandler(formData)
   {
		var search_field= $('#searchIDorURL')
		if(search_field.val().length == 6)
		{
			DoAjax(
				{'access_key':search_field.val(),'csrfmiddlewaretoken':csrfmiddlewaretoken},
				BASE_URL+'/load',
				'POST',
				onLoadExisting,"Checking existing Logger")

		}
		else
		{
			DoAjax({'access_key':search_field.val(),'csrfmiddlewaretoken':csrfmiddlewaretoken},BASE_URL+'/create','POST',onNewCreate,"Creating Logger")
		}
		ResetFields(formData);	
   }
   function onLoadExisting(response={})
   {
   			if(response.access_key == "123456")
   			{
   				  M.toast({html: 'Umm sorry!',displayLength:1500});
   			}
   			else
   			{	
				appendreqData("Orignal Url",response.origin_url,'origin_url')
				appendreqData("New Url ",BASE_URL+"/"+response.tracking_code,'managing_code')
				appendreqData("Tracking Code ",response.managing_code,'track_code')
				console.log(response);
				fetchRecords(response.managing_code);
				showresults();

   			}
	   }
	function fetchRecords(mcode)
	{
		DoAjax(
			{'access_key':mcode,'csrfmiddlewaretoken':csrfmiddlewaretoken},
			BASE_URL+'/load_results',
			'POST',
			updateRecords,"Loading results")
	}
	function updateRecords(response={})
	{
		$('#result_records tr').remove();
		$.each(response.data, function(key,value) {
			appendRecordData(value)
		});
	}
   function onNewCreate(response={}) 
   {
		appendreqData("Orignal Url",response.origin_url,'origin_url')
		appendreqData("New Url ",BASE_URL+"/"+response.tracking_code,'managing_code')
		appendreqData("Tracking Code ",response.managing_code,'track_code')
		showresults();

   }
   function appendreqData(name,value,rec_id)
   {
   		$('.tracker_info').append("<tr><td>"+name+"</td><td id="+rec_id+">"+value+"</td></tr>");
   }
   function appendRecordData(recordSingle)
   {
		$('#result_records').append("<tr><td>"+recordSingle.timezone+
		"</td><td>"+recordSingle.origin_ip+
		"</td><td>"+recordSingle.origin_country+
		"</td><td>"+recordSingle.origin_ip+
		"</td><td>"+(recordSingle.info == undefined | null ? 'orion':'leo')	+
		"</td><td>"+recordSingle.origin_ip+
		"</td><td>"+recordSingle.origin_ip+
		"</td><td>"+recordSingle.device_gpu+
		"</td></tr>");
   }
   function ResetFields(form)
   {
   	form.reset();return;
   }
   function DoAjax(data,url,method,callback=false,message='loading')
   {
		$.ajax({
			type:method,
			url:url,
			data:data,
            cache: false,
            beforeSend: function(xhr)
            {
				M.toast({html: message,displayLength:1500});
            },
            success: function (response) 
            { 
            		if($.isFunction(callback))
            		{
	            		callback(response);
            		}
            },
            error: function (e)
            {
            	console.log(e);
            	if($.isFunction(callback))
            		{
            			callback(e);
            		}
            }
		});
   }

   function appenddummydata(search_field_dummy="NA")
   {
   			appendreqData('Orignal Url',search_field_dummy);
			appendreqData('New URL ','https://grabify.link/V4PMN1');
			appendreqData('Tracking Code ','JFXZOL');
			appendreqData('Access Link','https://grabify.link/track/JFXZOL');
   }

   function hideresults()
   {
   		if(!$('.result_date').hasClass("hide"))
			{
				$('.result_date').addClass("hide");
			}

   }
   function showresults()
   {
   		if($('.result_date').hasClass("hide"))
			{
				$('.result_date').removeClass("hide");
			}
   }
   $('.form-globalsearch').submit(function(e)
   {
	if(this.method == "post")
	{
		hideresults();
		$('.tracker_info tr').remove();
		$('#result_records tr').remove();
		e.preventDefault();
		formPOSTHandler(this); return;
	}
});
	
 });
