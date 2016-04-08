(function () {
  'use strict';

  angular
    .module('placement.config')
    .config(config);

  config.$inject = ['$locationProvider','$resourceProvider'];

  /**
   * @name config
   * @desc Enable HTML5 routing
   */
  function config($locationProvider, $resourceProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
     $resourceProvider.defaults.stripTrailingSlashes = false;
  }
})();
