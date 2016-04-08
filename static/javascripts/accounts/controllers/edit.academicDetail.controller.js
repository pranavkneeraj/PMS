/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('EditAcademicDetailController', EditAcademicDetailController);

    EditAcademicDetailController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', 'UserService', 'academic_detail'];

  /**
   * @namespace
   */
    function EditAcademicDetailController($location, $scope, $cookies, $anchorScroll, UserService, academic_detail) {
        $location.hash('academicDetailForm');
        $anchorScroll();
        var vm = this;
        vm.isEditForm = true;
        vm.academic_detail_not_found = true;
        if(academic_detail) {
            vm.studentAcademicDetail = academic_detail;
            vm.academic_detail_not_found = true;
        }
        else {
            UserService.academicDetailApi.get({'id':UserService.user.id}).$promise.then(function (success) {
                vm.studentAcademicDetail = success;
                vm.academic_detail_not_found = false;
                console.log(success);
            }, function(error) {
                console.log(error);
                if(error.status == 404) {
                    vm.studentAcademicDetail = {};
                    vm.error_msg = "Your have  no detail saved, Please enter";
                }
                else
                    vm.error_msg = "Something goes wrong in loading your detail.";
            });
        }
        console.log("Inside academic detail edit controller");
        //document.getElementById(hashId).focus();
        vm.edit = function() {
            console.log("hey academic edit", $scope.StudentAcademicDetail);
            if(vm.academic_detail_not_found) {
                data = vm.studentAcademicDetail;
                if(!data.student)
                    data['student'] = UserService.user.id;
                UserService.academicDetailApi.save(vm.studentAcademicDetail).$promise.then(function (success) {
                    console.log(success);
                    vm.success_msg = "Your Academic Detail Updated Successfully";
                    vm.error_msg=null;
                }, function (error) {
                    console.log(error);
                    vm.error_msg = "Unable to update your academic detail, please try again";
                });
            }
            else {
                var data = {};
                if($scope.StudentAcademicDetail.hsc_marks.$dirty)
                    data['hsc_marks'] = $scope.StudentAcademicDetail.hsc_marks.$viewValue;
                if($scope.StudentAcademicDetail.hsc_percentage.$dirty)
                    data['hsc_percentage'] = $scope.StudentAcademicDetail.hsc_percentage.$viewValue;
                if($scope.StudentAcademicDetail.hsc_passout_year.$dirty)
                    data['hsc_passout_year'] = $scope.StudentAcademicDetail.hsc_passout_year.$viewValue;
                if($scope.StudentAcademicDetail.ssc_marks.$dirty)
                    data['ssc_marks'] = $scope.StudentAcademicDetail.ssc_marks.$viewValue;
                if($scope.StudentAcademicDetail.ssc_percentage.$dirty)
                    data['ssc_percentage'] = $scope.StudentAcademicDetail.ssc_percentage.$viewValue;
                if($scope.StudentAcademicDetail.ssc_passout_year.$dirty)
                    data['ssc_passout_year'] = $scope.StudentAcademicDetail.ssc_passout_year.$viewValue;
                if($scope.StudentAcademicDetail.ug_marks.$dirty)
                    data['ug_marks'] = $scope.StudentAcademicDetail.ug_marks.$viewValue;
                if($scope.StudentAcademicDetail.ug_percentage.$dirty)
                    data['ug_percentage'] = $scope.StudentAcademicDetail.ug_percentage.$viewValue;
                if($scope.StudentAcademicDetail.ug_passout_year.$dirty)
                    data['ug_passout_year'] = $scope.StudentAcademicDetail.ug_passout_year.$viewValue;
                if($scope.StudentAcademicDetail.ug_course.$dirty)
                    data['ug_course'] = $scope.StudentAcademicDetail.ug_course.$viewValue;
                if($scope.StudentAcademicDetail.exprience.$dirty)
                    data['exprience'] = $scope.StudentAcademicDetail.exprience.$viewValue;
                if($scope.StudentAcademicDetail.current_pg_sem.$dirty)
                    data['current_pg_sem'] = $scope.StudentAcademicDetail.current_pg_sem.$viewValue;

                UserService.academicDetailApi.update({'id':vm.studentAcademicDetail.student}, data).$promise.then(function (success) {
                    console.log(success);
                    vm.success_msg = "Your Academic Detail Updated Successfully";
                }, function (error) {
                    console.log(error);
                    vm.error_msg = "Unable to update your academic detail, please try again";
                });
            }
        };
    }
})();
