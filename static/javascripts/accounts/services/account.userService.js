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
          'update': { method:'PATCH' }
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
      var campusDriveApi = $resource('api/academic/campusdrive/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var criteriaApi = $resource('api/academic/criteria/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var specialCriteriaApi = $resource('api/academic/special_criteria/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });

      var interestedstudentApi = $resource('api/academic/interested/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });

      var uploadExcelFile = $resource('api/academic/pgsem/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });
      var placementMail = $resource('student/placement/notification/:id/', {id: '@data.id'}, {
          'update': { method:'PATCH' }
      });

      var  globalAlert = function(alert_body, type) {
          if(type=='danger')
              angular.element('.global-alert').html('<div class="alert alert-danger">'+ alert_body + "</div>");
      };
      var hideGlobalAlert = function() {
          console.log("hide");
          angular.element('.global-alert').html('');
      };
      var userService = {
          isLogin: false,
          user: '',
          addStudentList:addListApi,
          api:api,
          codeApi:codeApi,
          academicDetailApi:academicDetailApi,
          pgDetailApi:pgDetailApi,
          campusDriveApi:campusDriveApi,
          criteriaApi:criteriaApi,
          specialCriteriaApi:specialCriteriaApi,
          interestedStudentApi:interestedstudentApi,
          placementMail:placementMail,
          globalAlert:globalAlert,
          hideGlobalAlert:hideGlobalAlert

          //uploadExcelFile:uploadExcelFile
      };
      return userService;
  }
})();
