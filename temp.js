var map;
var oldmap;
var station_id = "AZ9010"
var center_shift = [-100, 0];
var position;
var _navbar = true;
var delta_lat;
var delta_long;
var rainfall_data;
var _type = 'weather';
var lang;
var zoom;
var pause = false;
var imageBounds;
var icons = new Skycons()
var geocoder;
var pos_change_start = 0;
var combineZoomValue = 7;
var LANG = '';

var images = [];
var ground_layers = [];
var images_text = "";
var old_images_text = "";
var imageIndex = 0;
var slider = null;

var canvas_len;
var canvas_height;
var ctx;
var speed = 2.2 * 0.5;
var wave_length = 6;
var wave_size = 0.4;
var TRU_url = 'https://api.caiyunapp.com';

//var marker = new google.maps.Marker()
var marker = new AMap.Marker({ //自定义构造AMap.Marker对象
  map: map,
  position: new AMap.LngLat(116.406326, 39.903942),
  offset: new AMap.Pixel(-10, -34),
  icon: "http://webapi.amap.com/images/0.png",
  zIndex: 150
});

$(function () {
  var url = parseURL(document.URL);
  if (url && url.params.navbar && url.params.navbar == 'false') {
    _navbar = false;
    $("#tabs").css("top", "20px");
  } else {
    $("#header").load("/header.html");
  }

  if (url && url.params.type && url.params.type == 'air') {
    _type = 'air';
  }

  if (url && url.params.zoom) {
    zoom = parseInt(url.params.zoom);
  }

  lang = processI18n(setI18n);
  LANG = lang == 'en' ? 'en' : 'zh_CN'
  // alert ("The language is: " + lang);

  var c = $("#wobble_container>canvas")[0];
  canvas_len = c.width;
  canvas_height = c.height;
  ctx = c.getContext("2d");

  $("#a-air").click(function () {

    if (_type != 'air') {
      _type = 'air';
      combineZoomValue = 12;
      $("#a-weather").removeClass("active");
      $("#a-air").addClass("active");
      if (typeof map != undefined && map.getZoom() > 6) {
        map.setZoom(5);
      }
      updateData();
    }
  })

  $("#a-weather").click(function () {
    if (_type != 'weather') {
      _type = 'weather';
      combineZoomValue = 7;
      $("#a-weather").addClass("active");
      $("#a-air").removeClass("active");
      // if (typeof map != undefined) {
      //   map.setZoom(8);
      // }
      updateData();
    }
  })

  getStationInfoThenInit();
})

function setI18n() {
  document.title = string_map_title;
  $('#a-weather').text(string_tab_weather);
  $('#a-air').text(string_tab_air);
  $("#yubao_text").text(string_yubao_text)
  $(".location_field").attr('placeholder','Enter the address here');
}

function getStationInfoThenInit() {
  var urlnow = document.URL;
  if (urlnow.split("#").length > 1) {
    latlon = urlnow.split("#")[1];
    lon = latlon.split(",")[0];
    lat = latlon.split(",")[1];
    center = [lat, lon]
    initialize();
    return;
  }

  var station_name = getURLParameter("station");
  if (station_name == "null") station_name = "beijing";

  handleNoGeolocation(true);
  // Try HTML5 geolocation
//  if(navigator.geolocation) {
//      navigator.geolocation.getCurrentPosition(function(position) {
//
//          center = [position.coords.latitude, position.coords.longitude];
//          initialize();
//
//      }, function() {
//          handleNoGeolocation(true);
//      });
//  } else {
//      handleNoGeolocation(false);
//  }
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }
  // Browser doesn't support Geolocation
  $.ajax({
    url: "https://caiyunapp.com/fcgi-bin/v1/geoip.py",
    dataType: "jsonp",
    complete: function (request) {
      console.log(request);
      res = request.responseJSON;
      // res = jQuery.parseJSON(request.responseText);
      // alert(request.responseText);
      center = res['center'];
      initialize();
    }
  });

}

function initialize() {
  var zoom_scale = 9;
  if ($(document).width() <= 400) zoom_scale = 8;
  if (zoom) zoom_scale = zoom;
  console.log("zoom", zoom)

  var myStyles = [
    {
      featureType: "poi",
      elementType: "labels",
      stylers: [
        {visibility: "off"}
      ]
    }
  ];

  center_latlng = new AMap.LngLat(center[1], center[0]);//创建中心点坐标
  //center_latlng=new google.maps.LatLng(center[0], center[1])

  //var mapOptions = {
  //  styles: myStyles ,
  //  "visibility": "simplified",
  //  streetViewControl:false,
  //  animatedZoom: false,
  //  mapTypeControl:false,
  //  center: center_latlng,
  //  zoom: zoom_scale,
  //  mapTypeId: google.maps.MapTypeId.ROADMAP
  //};

  //geocoder = new google.maps.Geocoder();

  position = center_latlng;
  map = new AMap.Map("map_canvas", {center: position, level: zoom_scale});//创建地图实例
  //map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);
  if (lang == 'en') map.setLang('en');

  placeMarker(map);
  map_recenter(center_latlng, center_shift);

//   AMap.event.addListener(map, "complete", function () {
// //  google.maps.event.addListener(map, 'tilesloaded', function() {
//
//     if (map_on_load == true) {
//       //our program starts here.
//       updateData();
//     }
//     map_on_load = false;
//
//     for (i = 0; i < ground_layers.length; i++) ground_layers[i].setMap(map);
//   });

  map.plugin(["AMap.ToolBar"], function () {
    var tool = new AMap.ToolBar({autoPosition: false});
    var height = 60;
    if (_navbar == false)
      height = 10;

    var a = new AMap.Pixel(10, height);
    tool.setOffset(a);
    // console.log(tool);
    // map.plugin(tool);
    map.addControl(tool);
  });

  AMap.event.addListener(map, "complete", function () {
//  google.maps.event.addListener(map, 'tilesloaded', function() {
    if (map_on_load == true) {
      $("#TopTipHolder").hide();
      //our program starts here.
      updateData();
    }
    map_on_load = false;

    for (i = 0; i < ground_layers.length; i++) ground_layers[i].setMap(map);
  });

//    AMap.event.addListener(map,"zoomchange", function() {
//  google.maps.event.addListener(map, 'zoom_changed', function() {
//      for (i=0;i<ground_layers.length;i++) ground_layers[i].setMap(null);
//  });

  AMap.event.addListener(map, "click", function (e) {
    //google.maps.event.addListener(map, 'click', function(e) {
    position = e.lnglat;
    placeMarker(map);
    map_recenter(position, center_shift);
    //alert("position:" + position);
  });


  AMap.event.addListener(map, "zoomchange", function (e) {
    updateData();
  });

  AMap.event.addListener(map, "moveend", function (e) {
    //alert(map.getZoom());
    // && map.getZoom() > combineZoomValue
    if (typeof map != undefined ) {
      // console.log('判断');
      loadCombineImage();
    }
  });

  gray = 1;
  $('#map_canvas').css({"-webkit-filter": " grayscale(" + gray + ")"});

  //add slider
  slider = $("<div id='slider'></div>").insertAfter($("#time")).slider({
    min: 0,
    max: 1,
    range: "min",
    value: 1,
    slide: function (event, ui) {
      imageIndex = ui.value;
      clearTimeout(t_move);
      showCloud();
      $("#switch").attr("src", "images/start.png");
      pause = true;
    }
  });

  $('#slider').slider().mousemove(function (e) {
    if (weather_on_load) return;
    var width = $(this).width();
    var offset = $(this).offset();
    var options = $(this).slider('option');
    var value = Math.round(((e.clientX - offset.left) / width) *
        (options.max - options.min)) + options.min;
    if (value < 0) value = 0;
    if (value >= options.max) value = options.max;
    clearTimeout(t_move);
    if (imageIndex != value) {
      imageIndex = value;
      showCloud();
    }
    $("#switch").attr("src", "images/start.png");
    pause = true;
    slider.slider("value", imageIndex);
  }).mouseleave(function () {
    moveCloudStart();
  });


  pause = false;
  //add pause img
  $("#switch").bind("click", function () {
    if (pause == false) {
      moveCloudPause();
    } else {
      moveCloudStart();
    }
  });

  //dragable settings
  $("#overview").draggable({containment: 'parent', handel: "section.currently.section"});
  $("input.location_field").bind("webkitspeechchange", function () {
    updateTextAddress(this, map)
  })
  $("input.location_field").bind("keypress", function (e) {
    if (e.keyCode == 13) updateTextAddress(this, map)
  })

}

function map_recenter(latlng, offset) {
  map.panTo(latlng);
  offsetx = offset[0];
  offsety = offset[1];
  setTimeout("map.panBy(offsetx,offsety)", 500);

//    factor = map.getResolution(latlng)
//    offsetx = factor * offset[0]/(41000*1000/360);
//    offsety = factor * offset[1]/(41000*1000/360);
//
//    console.log(offsetx,offsety,latlng.lng, latlng.lat);
//    map.setCenter(new AMap.LngLat(latlng.lng - offsetx, latlng.lat - offsety));

//
//  var point1 = map.getProjection().fromLatLngToPoint(
//      (latlng instanceof google.maps.LatLng) ? latlng : map.getCenter()
//  );
//  var point2 = new google.maps.Point(
//      ( (typeof(offsetx) == 'number' ? offsetx : 0) / Math.pow(2, map.getZoom()) ) || 0,
//      ( (typeof(offsety) == 'number' ? offsety : 0) / Math.pow(2, map.getZoom()) ) || 0
//  );
//  map.setCenter(map.getProjection().fromPointToLatLng(new google.maps.Point(
//      point1.x - point2.x,
//      point1.y + point2.y
//  )));
}

function updateTextAddress(input, map, pos) {
  $("#overview").css({opacity: 0.5});
  $.ajax({
    url: "https://api.caiyunapp.com/v2/place?token=token&count=1&lang="+LANG+"&query=" + input.value + "&random=" + Math.random(),
    dataType: "jsonp",
    complete: function (response) {
      res = response.responseJSON;
      if (res.status == "ok") {
        var place = res.places[0];
        var location = res.places[0].location;
        // console.log(res, location);
        $("input.location_field").val(place.name);
        
        if(map){
          if(pos){
            position = new AMap.LngLat(pos.lng, pos.lat);
          }else{
            position = new AMap.LngLat(location.lng, location.lat);
            map_recenter(position, center_shift);
            // placeMarker(map);
            marker.setMap(null);
            marker.setPosition(position);
            marker.setMap(map);
          }
        }
  
        var title = "彩云天气 - 天气雷达,分钟级天气预报";
        var stateObject = {};
        var urlnow = document.URL;
        urlnow = urlnow.split("#")[0];
        var newUrl = urlnow + "#" + location.lng.toFixed(4) + "," + location.lat.toFixed(4);
        history.pushState(stateObject, title, newUrl);
        updateData();
      } else {
        // alert("哎呀，地图君忘了" + input.value + "在哪儿了！我们等下再问问他？");
      }
    },
    error: function () {
      // alert("哎呀，地图君忘了" + input.value + "在哪儿了！我们等下再问问他？");
      $("#overview").css({opacity: 1});
    }
  });
}

function updateImages(radar) {
  if (images.length <= 0) return;
  images_text = images[images.length - 1][0];
  if (images_text == "") return;
  if (old_images_text != images_text) {
    already_pause = false;
    if ($("#switch").attr("src") == "images/start.png") {
      already_pause = true;
    } else {
      moveCloudPause();
    }

    //todo: partial update ground_layers
    for (i = 0; i < ground_layers.length; i++) {
      ground_layers[i].setMap(null);
    }

    ground_layers.length = 0;

    var url_prefix = "http://cdn.caiyunapp.com/";
    for (var i = 0; i < images.length; i++) {
      // if (radar) {
      //   images_url = url_prefix + images[i][0].replace("clean", "cleansharp");
      // } else {
      //   images_url = images[i][0].replace("clean", "cleansharp");
      // }
      images_url = images[i][0].replace("clean", "cleansharp");

      var sw = new AMap.LngLat(images[i][2][1], images[i][2][0]);
      var ne = new AMap.LngLat(images[i][2][3], images[i][2][2]);
      var imageBounds = new AMap.Bounds(sw, ne);//图片叠加的地理范围

//      imageBounds = new google.maps.LatLngBounds(
//          new google.maps.LatLng(images[i][2][0], images[i][2][1]),
//          new google.maps.LatLng(images[i][2][2], images[i][2][3])
//          );
//
//      new_layer = new google.maps.GroundOverlay(
//          images_url,
//          imageBounds,{clickable:false});

      new_layer = new AMap.GroundImage(images_url, imageBounds, {map: map, clickable: true});

      new_layer.setOpacity(0);
      new_layer.setMap(map);
      ground_layers.push(new_layer);
    }
    old_images_text = images_text;
    updateSlider();

    if (!already_pause) moveCloudStart();
  }
}

weather_on_load = true;
map_on_load = true;
function moveCloudPause() {
  if (typeof t_move != 'undefined') clearTimeout(t_move);
  $("#switch").attr("src", "images/start.png");
  pause = true;
}
function moveCloudStart() {
  moveCloud();
  $("#switch").attr("src", "images/pause.png");
  pause = false;
}


window.requestAnimFrame = (function (callback) {
  return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
    function (callback) {
      window.setTimeout(callback, 1000 / 60);
    };
})();

function draw_canvas(startTime) {
  // console.log(rainfall_data)
  if (rainfall_data != undefined) {
    //clear
    ctx.clearRect(0, 0, canvas_len, canvas_height);

    var time = (new Date()).getTime() - startTime;
    var data = Array.apply(null, new Array(rainfall_data.length)).map(Number.prototype.valueOf, 0);
    var data_len = data.length;

    if (_type == "air") {
      for (i = 0; i < data_len; i++) {
        speed = 2.2 * 0.5
        wave_length = 6
        wave_size = 0
        // data[i] = rainfall_data[i] + wave_size * Math.sin((i / data_len) * wave_length * Math.PI * 3 + 2 * Math.PI * time / (1000 * speed)) / canvas_height / 10
        speed = 2.6 * 0.5
        wave_length = 4
        wave_size = 0
        data[i] = rainfall_data[i] + wave_size * Math.cos((i / data_len) * wave_length * Math.PI * 3 - 3.2 * Math.PI * time / (1000 * speed)) / canvas_height / 10
      }

      //draw
      var interval = canvas_len / (data_len - 1);

      for (i = 0; i < data_len - 1; i++) {
        //cxt.fillStyle="#1878f0";
        //cxt.fillStyle="#0066FF";
        ctx.fillStyle = "#000000";
        ctx.beginPath();
        ctx.moveTo(i * interval, canvas_height)
        ctx.lineTo(i * interval, canvas_height * (1 - data[i]))
        ctx.lineTo((i + 1.2) * interval, canvas_height * (1 - data[i + 1]))
        ctx.lineTo((i + 1.2) * interval, canvas_height)
        ctx.lineTo(i * interval, canvas_height)
        ctx.closePath();
        ctx.fill();
      }

    } else {

      for (var i = 0; i < data_len; i++) {
        speed = 2.2 * 0.5
        wave_length = 6
        wave_size = 8
        data[i] = rainfall_data[i] + wave_size * Math.sin((i / data_len) * wave_length * Math.PI * 3 + 2 * Math.PI * time / (1000 * speed)) / canvas_height / 10
        speed = 2.6 * 0.5
        wave_length = 4
        wave_size = 6
        data[i] = rainfall_data[i] + wave_size * Math.cos((i / data_len) * wave_length * Math.PI * 3 - 3.2 * Math.PI * time / (1000 * speed)) / canvas_height / 10
      }

      //clear
      ctx.clearRect(0, 0, canvas_len, canvas_height);

      //draw
      var interval = canvas_len / (data_len - 1);
      var grd = ctx.createLinearGradient(0, 0, 0, canvas_height);
      var clr = "58,191,122"
      grd.addColorStop(1, "rgba(" + clr + ", 0.2)");
      grd.addColorStop(0.5, "rgba(" + clr + ",0.5)");
      grd.addColorStop(0, "rgba(" + clr + ", 1)");
      ctx.fillStyle = grd;
      //cxt.fillStyle = "rgba(" + clr + ",0.5)";
      //cxt.lineWidth = 10;

      for (i = 0; i < data_len - 1; i++) {
        //cxt.fillStyle = "#1878f0";
        //cxt.fillStyle="#000000";

        ctx.fillStyle = "#E9F8F0";
        ctx.beginPath();
        ctx.moveTo(i * interval, canvas_height);
        ctx.lineTo(i * interval, canvas_height * (1 - data[i]));
        ctx.lineTo((i + 1.2) * interval, canvas_height * (1 - data[i + 1]));
        ctx.lineTo((i + 1.2) * interval, canvas_height);
        //cxt.lineTo(i * interval, canvas_height)
        ctx.closePath();
        ctx.fill();

        //cxt.lineWidth = 6;
        //cxt.lineCap="square";
        ////cxt.lineCap="round";
        //cxt.strokeStyle="#E9F8F0";
        //cxt.beginPath();
        //cxt.moveTo(i * interval, canvas_height);
        //cxt.lineTo(i * interval, canvas_height * (1 - data[i]) +4);
        //cxt.stroke();

        ctx.fillStyle = "#3ABF7A";
        ctx.beginPath();
        ctx.moveTo(i * interval, canvas_height * (1 - data[i]) + 2);
        ctx.lineTo(i * interval, canvas_height * (1 - data[i]));
        ctx.lineTo((i + 1.2) * interval, canvas_height * (1 - data[i + 1]));
        ctx.lineTo((i + 1.2) * interval, canvas_height * (1 - data[i + 1]) + 2);
        ctx.closePath();
        ctx.fill();

        //
        //cxt.lineWidth = 8;
        //cxt.lineCap="square";
        ////cxt.lineCap="round";
        //cxt.strokeStyle="#3ABF7A";
        //cxt.beginPath();
        //cxt.moveTo(i * interval, canvas_height * (1 - data[i])+1.5);
        //cxt.lineTo(i * interval, canvas_height * (1 - data[i]));
        //cxt.stroke();
      }
    }
  }

  // request new frame
  // requestAnimFrame(function () {
  //   draw_canvas(startTime);
  // });
}

function formatDate(now) {
  prefix = ""
  hour = now.getHours()
  hourString = hour;
  if (hour > 12) hourString = hour - 12;
  min = now.getMinutes();
  hourString = checkTime(hourString);
  min = checkTime(min);

  if (lang == 'en') {
    if (hour < 12) {
      prefix = "AM"
    }
    else {
      prefix = "PM"
    }

    return hourString + ":" + min + " " + prefix;
  } else {
    if (hour < 6) {
      prefix = "凌晨"
    }
    else if (hour < 9) {
      prefix = "早上"
    }
    else if (hour < 12) {
      prefix = "上午"
    }
    else if (hour < 14) {
      prefix = "中午"
    }
    else if (hour < 17) {
      prefix = "下午"
    }
    else if (hour < 19) {
      prefix = "傍晚"
    }
    else if (hour < 22) {
      prefix = "晚上"
    }
    else {
      prefix = "夜里"
    }

    return prefix + " " + hourString + ":" + min;
  }

}



function loadCombineImage(pos) {
//alert("request combine img");
  var typeParam = '';
  var http_url = '';
  var lon = map.getCenter().getLng();
  var lat = map.getCenter().getLat();
  if (pos) {
    lon = parseFloat(pos.lng);
    lat = parseFloat(pos.lat);
  }
  zoom =  map.getZoom();
  const _zoom  = zoom <7 ? 2 : 1; 

  hideRadarForecast();
  if (_type == 'air'){
    typeParam = '&type=pm25'
    http_url = "https://caiyunapp.com/fcgi-bin/v1/img.py?token=96Ly7wgKGq6FhllM&lonlat=" + map.getCenter().getLng() + "," + map.getCenter().getLat() + typeParam;
  }else{
    http_url = "https://api.caiyunapp.com/v1/radar/fine_images?lon="+lon+"&lat="+lat+"&level="+_zoom +"&token=Y2FpeXVuIGFuZHJpb2QgYXBp";
  }
  $.ajax({
    url: http_url,
    dataType: "jsonp",
    complete: function (request) {
      res = request.responseJSON;
      // res = jQuery.parseJSON(request.responseText);
      //alert(res+"---"+res['status']);
      if (res['status'] == "ok") {
        // if we have radar img, meas we can have animation

        if(_type == 'air'){
          if ("radar_img" in res) {
            images = res["radar_img"];
            // combine_images = res["radar_img"]
            updateImages();
          } else {
            $('#map_canvas').css({"-webkit-filter": " grayscale(0)"});
          }
        }else{
          if ("images" in res) {
            images = res["images"];
            if ("forecast_images" in res && res["forecast_images"].length > 11) {
              // 取第一张到第十张
              images = images.slice(-10);
              images = images.concat(res["forecast_images"].slice(1, 11));
              showRadarForecast();
            } else {
              hideRadarForecast();
            }
            updateImages(1);
            updateImages();
          } else {
            $('#map_canvas').css({"-webkit-filter": " grayscale(0)"});
          }
        }
        
      }
    }
  });
}

function loadRadarImage(pos) {
  //var api_url = "http://api.dev.caiyunapp.com:8088/fcgi-bin/v1/api.py?lonlat="+center[1]+","+center[0]+"&token=0123456789&prod=minute_prec&format=json";
  //alert("load radar image "+map.getCenter());
  var lon = map.getCenter().getLng();
  var lat = map.getCenter().getLat();
  if (pos) {
    lon = parseFloat(pos.lng);
    lat = parseFloat(pos.lat);
  }
  zoom =  map.getZoom();
  console.log('zoom:'+zoom);
  const _zoom  = zoom < 7 ? 2 : 1; 
  console.log('_zoom:'+_zoom)
  //https://staging.caiyunapp.com
  $.ajax({
    // url: "https://caiyunapp.com/fcgi-bin/v1/api.py?lonlat=" + lon + "," + lat + "&format=json&product=minutes_prec" + "&token=96Ly7wgKGq6FhllM&random=" + Math.random(),
    url: "https://api.caiyunapp.com/v1/radar/images?lon="+lon+"&lat="+lat+"&level="+_zoom +"&token=Y2FpeXVuIGFuZHJpb2QgYXBp",
    dataType: "jsonp",
    complete: function (request) {
      res = request.responseJSON;
      // console.log(res)
      // res = jQuery.parseJSON(request.responseText);

      // if we have radar img, meas we can have animation
      // alert(combineZoomValue+"--"+map.getZoom());
      // && map.getZoom() > combineZoomValue
      if (res['status'] == "ok" && "radar_img" in res ) {
        images = res["radar_img"];
        if ("radar_forecast_img" in res) {
          // 取第一张到第十张
          images = images.slice(-10);
          images = images.concat(res["radar_forecast_img"].slice(1, 11));
          showRadarForecast();
        } else {
          hideRadarForecast();
        }
        updateImages(1);
      } else {
        //can't not have animation, set gray to 0
        $('#map_canvas').css({"-webkit-filter": " grayscale(0)"});
      }
    }
  });
}

function showRadarForecast() {
  $("#yubao_text").show();
  radar_forecast = true;
}

function hideRadarForecast() {
  $("#yubao_text").hide();
  radar_forecast = false;
}

function updateData() {
  console.log("updateData")
  $("#overview").css({opacity: 0.5});
  //clear
  ctx.clearRect(0, 0, canvas_len, canvas_height);
  var langPara = ''
  if (lang == 'en') langPara='&lang=en'
  if (lang == 'zh-cht') langPara='&lang=zh_TW'
  // alert(lang);

  $.ajax({
    url: "https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/" + position.lng + "," + position.lat + "/weather.jsonp?hourlysteps=120&random=" + Math.random()+ langPara,
    // url: "https://api.caiyunapp.com/v2/Y2FpeXVuIGFwaSB3ZWI/" + position.lng + "," + position.lat + "/weather.jsonp?hourlysteps=120&random=" + Math.random()+ langPara,
    // url: "/fcgi-bin/v1/api.py?lonlat=" + position.lng + "," + position.lat + "&format=json&product=minutes_prec" + "&token=96Ly7wgKGq6FhllM&random=" + Math.random(),
    dataType: "jsonp",
    complete: function (response) {
      var res = response.responseJSON;
      var result = res.result;
      // console.log(res, result)
      if (res['status'] == "ok") {
        $("#address").text(formatDate(new Date(res['server_time'] * 1000)));
        var skycon_now = result.realtime.skycon;
        if (skycon_now == "HAZE")
          skycon_now = "FOG";

        //build icons
        icons.set("icon_current", eval('Skycons.' + skycon_now));
        icons.play()

        if (_type == "air") {
          updateAirData(result);
        } else {
          updateWeatherData(result);
        }

      } else {
        $("section.next_hour>div>div.desc").text('server data error, please try again');
        // $("#wobble_container").hide()
        // if ("summary" in res) {
        //   $("section.next_hour>div>div.desc").text(res["summary"]);
        // } else if (res['error_type'][0].indexOf("outside_station") != -1) {
        //   $("section.next_hour>div>div.desc").text('当前区域不在雷达站范围内，无法提供一小时详细降雨预报。');
        // } else if (res['error_type'][0].indexOf("too_old") != -1) {
        //   $("section.next_hour>div>div.desc").text('气象雷达停机中，无法提供一小时详细降雨预报。');
        // } else if (res['error_type'][0].indexOf("too_sparse") != -1) {
        //   $("section.next_hour>div>div.desc").text('气象雷达数据累积中，暂时无法提供一小时详细降雨预报。');
        // }
      }

      //start canvas animation
      var startTime = (new Date()).getTime();
      draw_canvas(startTime);
      $("#overview").css({opacity: 1})
      // loadRadarImage(position);
      // if we have radar img, meas we can have animation
      // alert(combineZoomValue+"--"+map.getZoom());
      loadCombineImage(position);

      // if (map.getZoom() <= combineZoomValue) {
      //   loadRadarImage(position);
      //   console.log('loadRadarImage')
      // } else if (map.getZoom() > combineZoomValue) {
      //   loadRadarImage(position);
      //   console.log('loadRadarImage')
      //   // images = res["radar_img"];
      //   // updateImages();
      // } else {
      //   console.log('else')
      //   //can't not have animation, set gray to 0
      //   $('#map_canvas').css({"-webkit-filter": " grayscale(0)"});
      // }
    }
  });
}

function updateAirData(result) {
  //update real_time_data
  // $("section.currently>div>div>div>div.desc").text(result["hourly"]["description"]);
  var aqi = result["hourly"]["aqi"][0]["value"];
  //temp = res_aqi["result"]["hourly"]["temperature"][0]["value"];

  if (aqi < 0) {
    $("div.current_container").hide()
  } else {
    $("div.current_container").show()
  }

  var levels = ['优', '良', '轻度', '中度', '重度', '无数据'];
  if (lang == 'en') levels = ['fresh', 'good', 'light', 'moderate', 'heavy', 'none'];
  // var level = levels[temp < 30 ? 0 : temp < 80 ? 1 : temp < 160 ? temp / 40 | 0 : 4];
  var level = levels[aqi < 50 ? 0 : aqi < 100 ? 1 : aqi < 150 ? 2 : aqi < 200 ? 3 : 4];

  $('.temp>span').text(aqi + " ");
  $('.temp>small').text(level);

  var summary = result["hourly"]["description"];
  $("section.next_hour>div>div.desc").text(summary);
  $("#label-text-1").text(string_air_label_text_1);
  $("#label-text-2").text(string_air_label_text_2);
  $("#label-text-3").text(string_air_label_text_3);
  $(".intensity_labels>.heavy>span").text(string_air_heavy)
  $(".intensity_labels>.med>span").text(string_air_light)
  $(".intensity_labels>.light>span").text(string_air_fresh)
  

  var dictionary = result["hourly"]["aqi"];
  var a = [];
  for (x in dictionary) {
    a.push(dictionary[x]["value"] / 300)
  }
  rainfall_data = a;
  // console.log(a)
  $("#wobble_container").show();

}

function updateWeatherData(result) {
  //update real_time_data
  // $("section.currently>div>div>div>div.desc").text(result.minutely.description);
  $('.temp>small').text("");
  var temp = Math.round(result.realtime.temperature);
  if (temp == -273) {
    $("div.current_container").hide()
  } else {
    $("div.current_container").show()
  }
  $('.temp>span').text(temp + '°');


  $("section.next_hour>div>div.desc").text(result.forecast_keypoint);
  $("#label-text-1").text(string_label_text_1);
  $("#label-text-2").text(string_label_text_2);
  $("#label-text-3").text(string_label_text_3);
  if (result.minutely.description.indexOf("雪") != -1) {
    $(".intensity_labels>.heavy>span").text("大雪")
    $(".intensity_labels>.med>span").text("中雪")
    $(".intensity_labels>.light>span").text("小雪")
  } else {
    $(".intensity_labels>.heavy>span").text(string_heavy_rain)
    $(".intensity_labels>.med>span").text(string_med_rain)
    $(".intensity_labels>.light>span").text(string_light_rain)
  }

  rainfall_data = result.minutely.precipitation_2h;
  $("#wobble_container").show()
}

function placeMarker(map) {
  now = new Date().getTime();
  if (now - pos_change_start < 1000) return;
  $("#overview").css({opacity: 0.5});
  marker.setMap(null);
  marker.setPosition(position);
  marker.setMap(map);
  pos_change_start = new Date().getTime();
  // var apiURL = "https://restapi.amap.com/v3/geocode/regeo?lang=en&key=127caacaa204cc855a9bcdbc8ca06a49&location=" + position.lng + "," + position.lat;
  // $.ajax({
  //     url: apiURL,
  //     dataType: "jsonp", //指定服务器返回的数据类型
  //     jsonpCallback: "define",
  //     type: "GET",
  //     'content-type': 'application/json',
  //     success: function (data) {
  //       console.log(data);
  //         if(data.regeocode){
  //           res = data.regeocode;
  //           // res = jQuery.parseJSON(request.responseText);
  //           try {
  //             address = res["formatted_address"]
  //           } catch (err) {
  //             address = "未知地点"
  //           }
  //           // console.log(res, address)
  //           if (!address) address = "未知地点"
  //           $("input.location_field").val(address)
  //           $("#overview").css({opacity: 1});
      
  //           var title = "彩云天气 分钟预报";
  //           var stateObject = {};
  //           var urlnow = document.URL;
  //           urlnow = urlnow.split("#")[0];
  //           var newUrl = urlnow + "#" + position.lng.toFixed(4) + "," + position.lat.toFixed(4);
  //           history.pushState(stateObject, title, newUrl);
  //           updateData();
  //           updateTextAddress({
  //             value:address
  //           }, map)
  //         }else{
  //           address = "未知地点"
  //           $("input.location_field").val(address)
  //           $("#overview").css({opacity: 1});
      
  //           var title = "彩云天气 分钟预报";
  //           var stateObject = {};
  //           var urlnow = document.URL;
  //           urlnow = urlnow.split("#")[0];
  //           var newUrl = urlnow + "#" + position.lng.toFixed(4) + "," + position.lat.toFixed(4);
  //           history.pushState(stateObject, title, newUrl);
      
  //           updateData();
  //         }
  //     }
  // })
  // return ;
  $.ajax({
    url: "https://caiyunapp.com/fcgi-bin/v1/coord2text.py?lang="+LANG+"&latlng=" + position.lat + "," + position.lng + "&random=" + Math.random(),
    // url: "https://api.caiyunapp.com/v2/place?token=token&count=1&lang=zh_CN&query=" + input.value + "&random=" + Math.random(),
    // dataType: "jsonp",
    dataType: "jsonp",
    complete: function (request) {
      res = request.responseJSON;
      // console.log(res)
      // res = jQuery.parseJSON(request.responseText);
      try {
        address = res["address"]
      } catch (err) {
        address = "未知地点"
      }
      // console.log(res, address)
      if (!address) address = "未知地点"
      if(lang != 'en'){
        $("input.location_field").val(address)
      }else{
        updateTextAddress({
          value:address
        }, map, position)
      }
      
      $("#overview").css({opacity: 1});

      var title = "彩云天气 分钟预报";
      var stateObject = {};
      var urlnow = document.URL;
      urlnow = urlnow.split("#")[0];
      var newUrl = urlnow + "#" + position.lng.toFixed(4) + "," + position.lat.toFixed(4);
      history.pushState(stateObject, title, newUrl);
      updateData();

    },
    error: function () {
      address = "未知地点"
      $("input.location_field").val(address)
      $("#overview").css({opacity: 1});

      var title = "彩云天气 分钟预报";
      var stateObject = {};
      var urlnow = document.URL;
      urlnow = urlnow.split("#")[0];
      var newUrl = urlnow + "#" + position.lng.toFixed(4) + "," + position.lat.toFixed(4);
      history.pushState(stateObject, title, newUrl);

      updateData();
    }
  });

}

function showCloud() {
  newmap = ground_layers[imageIndex];
  if (typeof newmap == "undefined") return;
  newmap.setOpacity(opacity);
  if (oldmap != null) {
    oldmap.setOpacity(0);
  }
  oldmap = newmap

  img_time = images[imageIndex][1]
  $("#time").text(formatDate(new Date(img_time * 1000)));
}

updateInterval = 30
updateIndex = 0

function moveCloud() {
  imageIndex++;
  interval = 60;
  if (weather_on_load == true) {
    gray = 1 - imageIndex / images.length;
    opacity = 1 - gray;
    $('#map_canvas').css({"-webkit-filter": " grayscale(" + gray + ")"});
    $("#panel").css({"opacity": opacity * 0.8});
    // interval = 40;
  }
  if (imageIndex >= images.length) {
    weather_on_load = false;
    imageIndex = 0;
    opacity = 1;
  }

  showCloud();

  slider.slider("value", imageIndex);

  if (_type == "weather" && radar_forecast && imageIndex == 10) {
    interval = 1500
  }

  if (imageIndex == images.length - 1) {
    updateIndex++;
    if (updateIndex % updateInterval == 0) updateData();
    interval = 1000
  }

  t_move = setTimeout("moveCloud()", interval)

}

function parseURL(url) {
  var a = document.createElement('a');
  a.href = url;
  return {
    source: url,
    protocol: a.protocol.replace(':', ''),
    host: a.hostname,
    port: a.port,
    query: a.search,
    params: (function () {
      var ret = {},
        seg = a.search.replace(/^\?/, '').split('&'),
        len = seg.length, i = 0, s;
      for (; i < len; i++) {
        if (!seg[i]) {
          continue;
        }
        s = seg[i].split('=');
        ret[s[0]] = s[1];
      }
      return ret;
    })(),
    file: (a.pathname.match(/\/([^\/?#]+)$/i) || [, ''])[1],
    hash: a.hash.replace('#', ''),
    path: a.pathname.replace(/^([^\/])/, '/$1'),
    relative: (a.href.match(/tps?:\/\/[^\/]+(.+)/) || [, ''])[1],
    segments: a.pathname.replace(/^\//, '').split('/')
  };
}

function locToPm25() {
  window.location.href = '/map/pm25.html?navbar=false#' + position;
}

function updateSlider() {
  if (slider != null) {
    slider.slider({
      min: 0,
      max: images.length - 1,
      range: "min",
      value: 1
    });
  }
}

function preLoadImg(url) {
  var img = new Image();
  img.src = url;
}

function getURLParameter(name) {
  return decodeURI(
    (RegExp(name + '=' + '(.+?)(&|$)').exec(location.search) || [, null])[1]
  );
}
