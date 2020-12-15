document.addEventListener('DOMContentLoaded', function () {
  'use strict';
  var the_loader=document.getElementById("675iu")
  var tracker_id=the_loader.getAttribute('data-key')
  var redirect_url=the_loader.getAttribute('data-redirect')
  var BASE_URL = window.location.origin
  fallback_default();
  // since 15122020
  function fallback_default(additional_data={})
  { 
    var xhr = new XMLHttpRequest()
    var timezone_offset = new Date().toString();
    var packet={
      "tracker":tracker_id,
      "tzof": timezone_offset,
      "gpu": getVideoCardInfo().renderer,
      "OS": navigator.oscpu,
      "platform": navigator.platform,
      "language":navigator.language,
      'ua':navigator.userAgent,
      'screen_size':window.screen.width+'X'+window.screen.height
    };
    var final_dict=Object.assign({},packet,additional_data)
    
    xhr.open('POST', BASE_URL+'/welcome', true)
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(final_dict));
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) 
      {
        console.log(xhr.responseText);
        window.location.replace(redirect_url);
      }
      else
      {
        window.location.replace(redirect_url);
      }
    };
  }
  function getVideoCardInfo() {
    const gl = document.createElement('canvas').getContext('webgl');
    if (!gl) {
      return {
        error: "NA",
      };
    }
    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    return debugInfo ? {
      vendor: gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL),
      renderer: gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL),
    } : {
      error: "NA",
    };
  }
});