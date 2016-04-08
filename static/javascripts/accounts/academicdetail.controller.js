/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('AcademicDetailController', AcademicDetailController);
    AcademicDetailController.$inject = ['$location', '$scope', 'UserService', 'student'];

  /**
   * @namespace RegisterController
   */
    function AcademicDetailController($location, $scope, UserService, student) {
        var vm = this;
        vm.student = {};
        vm.error_msg = "";
        vm.success_msg = "";
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
                    vm.success_msg = "Your personal detail is saved successfullly.";
                    vm.error_msg=null;

                    $location.path('register/add_detail');
                }, function(error) {
                    vm.error_msg = "Something goes wrong, please try again.";
                    vm.success_msg=null;
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
                    $location.path('register/add_detail');
                }, function(error) {
                    console.log(error)
                    vm.error_msg = "Something goes wrong, please try again.";
                    vm.success_msg=null;
                });
            }
        };
    }
})();
