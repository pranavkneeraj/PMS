/**
 * Account
 * @namespace thinkster.accounts.services
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.services')
    .factory('UserService', UserService);
  /**
   * @namespace userServiece
   */
  function UserService($resource) {
    /**
     * @name Account
     * @desc The factory to be returned
     * @memberOf thinkster.accounts.services.Account
     */
      var addListApi = $resource('api/user/add_users/', {id: '@data.id'});
      var api = $resource('api/user/user/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' },
      });
      var codeApi = $resource('api/user/user/registration/code/:code/', {id: '@data.code'}, {
          'update': { method:'PATCH' }
      });
      var academicDetailApi = $resource('api/academic/detail/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var pgDetailApi = $resource('api/academic/pgsem/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var uploadExcelFile = $resource('api/academic/pgsem/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var userService = {
          isLogin: false,
          user: '',
          addStudentList:addListApi,
          api:api,
          codeApi:codeApi,
          academicDetailApi:academicDetailApi,
          pgDetailApi:pgDetailApi
          //uploadExcelFile:uploadExcelFile
      };
      return userService;
  }
})();
