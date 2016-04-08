/**
 * Account
 * @namespace thinkster.accounts.services
 */
(function () {
  'use strict';

  angular
    .module('thinkster.accounts.services')
    .factory('Account', Account);

    Account.$inject = ['$resource'];

  /**
   * @namespace Account
   */
  function Account($resource) {
    /**
     * @name Account
     * @desc The factory to be returned
     * @memberOf thinkster.accounts.services.Account
     */
      var defaultMethods = {
          'query': { method: 'GET', isArray:false },
          'update': { method: 'PATCH' },
          'put': { method: 'PUT' },
          'options': {method: 'OPTIONS'}
      };
      var factory = {};
      factory.api = $resource('/:id/:action/', {id: '@data.id'}, defaultMethods);
      return factory;
  }
})();
