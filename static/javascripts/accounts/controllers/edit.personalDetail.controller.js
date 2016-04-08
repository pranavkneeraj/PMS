/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('EditPersonalDetailController', EditPersonalDetailController);

    EditPersonalDetailController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', 'UserService'];

  /**
   * @namespace
   */
    function EditPersonalDetailController($location, $scope, $cookies, $anchorScroll, UserService) {
        var vm = this;
        vm.isEditForm = true;
        console.log("Inside personal detail edit controller");
        var hashId = $location.hash('registration');
        $anchorScroll();
        vm.student = UserService.user;
        //document.getElementById(hashId).focus();
        vm.edit = function() {
            var data = {};
            if($scope.UserRegistration.first_name.$dirty)
                data['first_name']=vm.student.first_name;
            if($scope.UserRegistration.middle_name.$dirty)
                data['middle_name']=vm.student.middle_name;
            if($scope.UserRegistration.last_name.$dirty)
                data['last_name']=vm.student.last_name;
            if($scope.UserRegistration.email.$dirty)
                data['email']=vm.student.email;
            if($scope.UserRegistration.contact.$dirty)
                data['contact']=vm.student.contact;
            if($scope.UserRegistration.address.$dirty)
                data['address']=vm.student.address;
            console.log(data)
            UserService.api.update({'id':vm.student.id}, data).$promise.then(function (success) {
                console.log(success);
                $cookies.putObject('user',success);
                UserService.user=success;
                vm.success_msg = "Your Personal Detail Updated Successfully";
            }, function (error) {
                console.log(error);
                vm.success_msg = "Unable to update your detail, please try again";
            });
        };
    }
})();
