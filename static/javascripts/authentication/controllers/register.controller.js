/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.authentication.controllers')
    .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', '$state', 'UserService', 'student'];

  /**
   * @namespace RegisterController
   */
    function RegisterController($location, $scope, $state, UserService, student) {
        var vm = this;
        vm.submitInProgress = false;
        vm.student = {};
        if(student){
            student.$promise.then(function (code) {
                vm.student=code.user;
                vm.student['unique_code'] = student.code;
            });
        }
        vm.isJicaStudent = false;
        if(student)
            vm.isJicaStudent=true;
        vm.register = function() {
            vm.submitInProgress = true;
            console.log("inside registration");
            var data = {};
            data['contact'] = vm.student['contact'];
            data['unique_code'] = vm.student['unique_code'];
            data['password'] = vm.student['password'];
            data['address'] = vm.student['address'];
            data['is_active'] = true;
            UserService.student = vm.student;
            if(student) {
                console.log(student.user.id);
                var student_id = student.user.id;
                UserService.api.update({'id':student_id}, data).$promise.then(function(success){
                    console.log("asdsasd");
                    vm.error_msg=null;
                    $state.go('academic_detail',{"student":success.id});
                    vm.submitInProgress = false;
                }, function(error) {
                    vm.error_msg = "Something goes wrong, please try again.";
                    vm.success_msg=null;
                    vm.submitInProgress = false;
                });
            }
            else {
                data['first_name'] = vm.student.first_name;
                data['last_name'] = vm.student.last_name;
                data['email'] = vm.student.email;
                data['code'] = vm.student.code;
                data['roll_no'] = vm.student.roll_no;
                UserService.api.save(data).$promise.then(function(success){
                    vm.success_msg = "Your Personel detail is saved successfullly.";
                    vm.error_msg=null;
                    $state.go('academic_detail',{"student":success.id});
                    vm.submitInProgress = false;
                }, function(error) {
                    console.log(error);
                    if(error.data.email)
                        vm.error_msg = "User with this email already registerd";
                    //$state.go('academic_detail',{"student":4});
                    vm.success_msg=null;
                    vm.submitInProgress = false;
                });
            }
        };
    }
})();