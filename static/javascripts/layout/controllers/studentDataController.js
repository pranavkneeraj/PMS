/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.layout.controllers')
    .controller('studentController', studentController);
    studentController.$inject = ['$scope', 'UserService', '$location', '$anchorScroll'];

  /**
   * @namespace IndexController
   */

    function studentController($scope, UserService, $location, $anchorScroll) {
        var vm = this;
        vm.data= "sdad";
        vm.submitInProgress = false;
        vm.createFields  = function() {
      //      $location.hash('UserRegistrationForm');
      //      $anchorScroll(['UserRegistrationForm']);
          vm.NoOfStudent>0?vm.showFields=true:vm.showFields=false;
          vm.student_list = new Array(vm.NoOfStudent);
          for(var i=0;i<vm.NoOfStudent;i++)
              vm.student_list[i]={'roll_no':'', 'first_name':'', 'last_name':'', 'email':'', 'is_active':false};
      };
        vm.addStudents = function () {
            vm.submitInProgress = true;
            console.log("sadasd", vm.student_list, UserService);
            UserService.addStudentList.save({'user_list':vm.student_list}).$promise.then(function(success) {
                vm.submitInProgress = false;
                vm.success_msg = success;
                $location.hash('success_alert');
              $anchorScroll();
            }, function(error) {
                vm.submitInProgress = false;
            });
        };
  }
})();
