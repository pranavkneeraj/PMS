/**
 * Authentication
 * @namespac pms.authentication.services
 */
(function () {
  'use strict';

  angular
    .module('pms.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$http'];

  /**
   * @namespace Authentication
   * @returns {Factory}
   */
  function Authentication($http) {
    /**
     * @name Authentication
     * @desc The Factory to be returned
     */
    var Authentication = {
      login: login,
      logout: logout,
    };

    return Authentication;

    /**
     * @name login
     * @desc Try to log in with email `email` and password `password`
     * @param {string} email The email entered by the user
     * @param {string} password The password entered by the user
     * @returns {Promise}
     * @memberOf pms.authentication.services.Authentication
     */
    function login(email, password) {
      return $http.post('/user/auth/', {
        email: email, password: password
      });

    }


    /**
     * @name logout
     * @desc Try to log the user out
     * @returns {Promise}
     * @memberOf pms.authentication.services.Authentication
     */
    function logout() {
      return $http.delete('/user/auth/');
    }
  }
})();
