$( document ).ready(function() 
{
	M.AutoInit();
	var BASE_URL = $(location).attr("origin");
	var csrfmiddlewaretoken=$("input[name=csrfmiddlewaretoken]").val()
   $('.form-globalsearch').submit(function(e)
   		{
			if(this.method == "post")
			{
				hideresults();
				$('.tracker_info tr').remove();
  				e.preventDefault();
				formPOSTHandler(this); return;
			}
	});
   function formPOSTHandler(formData)
   {
		var search_field= $('#searchIDorURL')
		if(search_field.val().length == 6)
		{
			doajax({'access_key':search_field.val()},'http://jsonplaceholder.typicode.com/posts','POST',onNewCreate)
		}
		else
		{
			doajax({'access_key':search_field.val(),'csrfmiddlewaretoken':csrfmiddlewaretoken},BASE_URL+'/create','POST',onLoadExisting,"Creating Logger")
		}
		ResetFields(formData);	
   }
   function onNewCreate(response={})
   {
   			if(response.access_key == "123456")
   			{
   				  M.toast({html: 'Nothing Found',displayLength:1500});
   			}
   			else
   			{
   				appenddummydata(response.access_key);
   				showresults();
   			}
   	}
   function onLoadExisting(response={})
   {
   		appenddummydata(response.access_key);
   		showresults();
   }
   function appendreqData(name,value)
   {
   		$('.tracker_info').append("<tr><td>"+name+"</td><td>"+value+"</td></tr>");
   }
   function ResetFields(form)
   {
   	form.reset();return;
   }
   function doajax(data,url,method,callback=false,message='loading')
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
            		console.log(response);
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

 });
