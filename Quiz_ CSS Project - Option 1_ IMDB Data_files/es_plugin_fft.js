window.eesyLaunchConfig = {
    host: 'fft.eesysoft.com',
    key: 'cY9Z33kt',
    supportTab: true
};

(function() {
    var e = document.createElement('script');
    e.src = '//' + window.eesyLaunchConfig.host + "/resources/js/canvas/launch.js?stmp=" + new Date().getTime();
    e.src = '//' + window.eesyLaunchConfig.host + "/resources/js/canvas/launch.js";
    e.async = true;
    e.type = 'text/javascript';

    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(e, s);
} ());
