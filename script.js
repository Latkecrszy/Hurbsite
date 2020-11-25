$(document).ready(function() {
 
    setTimeout(function(){
        $('body').addClass('loaded');
    }, 3000);
 
});

anime({
    targets: '.path .lines path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 1500,
    delay: function(el, i) { return i * 250 },
    direction: 'alternate',
    loop: true
});

$(window).scroll(function() {
  $('.animation-test').each(function(){
  var imagePos = $(this).offset().top;

  var topOfWindow = $(window).scrollTop();
    if (imagePos < topOfWindow+400) {
      $(this).addClass("slideRight");
    }
  });
});


$('.element-to-hide').css('visibility', 'hidden');



//const wave1 = "M68.8,-24.1C75.1,-3.2,56.2,24.1,34.5,37.5C12.8,50.9,-11.8,50.5,-28.6,38.5C-45.4,26.5,-54.5,2.9,-48.4,-17.8C-42.4,-38.5,-21.2,-56.3,5.1,-57.9C31.3,-59.6,62.6,-45,68.8,-24.1Z",
  //    wave2 = "M46.6,-21.5C52.4,2.7,43.6,25.3,27.2,37.1C10.9,48.9,-13.1,50,-34.2,37C-55.4,24,-73.7,-2.9,-67.5,-27.7C-61.4,-52.4,-30.7,-74.8,-5.1,-73.2C20.4,-71.5,40.8,-45.7,46.6,-21.5Z",
    //  wave3 = "M52.6,-33.5C63.2,-12,63.4,12.3,52.8,32.3C42.3,52.4,21.2,68.1,1.1,67.5C-18.9,66.8,-37.9,49.8,-45.9,31.2C-53.9,12.6,-51,-7.6,-41.5,-28.4C-32.1,-49.2,-16,-70.6,2.5,-72C21,-73.4,42,-54.9,52.6,-33.5Z",
      //wave4 = "M46.8,-28.2C59.8,-4.7,68.6,20,60.2,40.7C51.7,61.3,25.8,77.8,4.1,75.4C-17.6,73.1,-35.3,51.8,-45.5,30.2C-55.7,8.6,-58.4,-13.4,-49.6,-34.5C-40.8,-55.7,-20.4,-76.1,-1.7,-75.1C17,-74.1,33.9,-51.8,46.8,-28.2Z";

//anime({
  //targets: '.blob-ani > path',
  //easing: 'linear',
  //duration: 7500,
  //loop: true,
  //d: [
    //{ value: [wave1, wave2] },
    //{ value: wave3 },
    //{ value: wave4 },
    //{ value: wave1 },
  //],
//});


anime({
  targets: '.login_prompt .el',
  translateX: 270,
  direction: 'alternate',
  loop: true,
  delay: function(el, i, l) {
    return i * 100;
  },
  endDelay: function(el, i, l) {
    return (l - i) * 100;
  }
});