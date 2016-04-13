/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
        .module('pms.accounts.controllers')
        .controller('EditPersonalDetailByUserController', EditPersonalDetailByUserController)
        .controller('EditPersonalDetailByAdminController', EditPersonalDetailByAdminController);


    EditPersonalDetailByUserController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', 'UserService'];

  /**
   * @namespace
   */
    function EditPersonalDetailByUserController($location, $scope, $cookies, $anchorScroll, UserService) {
        var vm = this;
        vm.form_page="static/templates/common/personal_detail_form.html";
        vm.alert_page = "static/templates/common/alert.html";
        vm.title= "Edit Personal Detail";
        vm.isEditForm = true;
        $anchorScroll('content-area');
        vm.student = UserService.user;
        //document.getElementById(hashId).focus();
        vm.edit = function(UserRegistration) {
            if(!$scope.UserRegistration)
                $scope.UserRegistration = UserRegistration;
            var data = {};
            console.log(vm.student, $scope);
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

    EditPersonalDetailByAdminController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', '$uibModalInstance' ,'UserService', 'student'];
    function EditPersonalDetailByAdminController($location, $scope, $cookies, $anchorScroll, $uibModalInstance, UserService, student) {
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html";
        vm.template = "static/templates/common/personal_detail_form.html";
        vm.isEditForm = true;
        $anchorScroll('content-area');
        console.log("Inside personal detail edit controller");
        vm.close = function() {
            $uibModalInstance.close();
        };
        if(!student)
            vm.student = UserService.user;
        else
            vm.student=student;
        //document.getElementById(hashId).focus();
        vm.edit = function(UserRegistration) {
            if(!$scope.UserRegistration)
                $scope.UserRegistration = UserRegistration;
            var data = {};
            console.log(vm.student, $scope);
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
                vm.close();
            }, function (error) {
                console.log(error);
                vm.success_msg = "Unable to update your detail, please try again";
            });
        };
    }
})();
