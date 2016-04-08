(function () {
  'use strict';

  angular
    .module('placement', [
	'ui.router',
        'placement.config',
        'placement.routes',
	'placement.directives',
	'pms.accounts',
        'pms.authentication',
	'pms.layout',
	'ngCookies',	
	'ui.bootstrap',
	'ngFileUpload'
    ]);

  angular
    .module('placement.config', ['ngResource']);

  angular
    .module('placement.routes', ['ngRoute']);
  angular
    .module('placement.directives', ['ngRoute']);

  angular
    .module('placement')
    .run(run);

  run.$inject = ['$http'];
  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }

})();
