(function () {
  'use strict';

  angular
    .module('pms.accounts', [
      'pms.accounts.controllers',
      'pms.accounts.services'
    ]);

  angular
    .module('pms.accounts.controllers', []);

  angular
    .module('pms.accounts.services', ['ngResource']);

})();
