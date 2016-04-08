(function () {
  'use strict';

  angular
    .module('pms.layout', [
      'pms.layout.controllers',
      'pms.layout.services',
    ]);

  angular
    .module('pms.layout.controllers', ['ngCookies']);
  angular
    .module('pms.layout.services', []);

})();
