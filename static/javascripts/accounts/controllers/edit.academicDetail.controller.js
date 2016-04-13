/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
        .controller('EditAcademicDetailByUserController', EditAcademicDetailByUserController)
        .controller('EditAcademicDetailByAdminController', EditAcademicDetailByAdminController);

    EditAcademicDetailByUserController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', 'UserService'];
    EditAcademicDetailByAdminController.$inject = ['$location', '$scope', '$cookies', '$anchorScroll', '$uibModalInstance', 'UserService', 'academic_detail_id'];
  /**
   * @namespace
   */
    function EditAcademicDetailByUserController($location, $scope, $cookies, $anchorScroll, UserService) {
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html";
        vm.form_page = "static/templates/common/academic_detail_form.html";
        $location.hash('bottom');
        $anchorScroll();
        vm.isEditForm = true;
        vm.academic_detail_not_found = true;
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
        console.log("Inside academic detail edit controller");
        //document.getElementById(hashId).focus();
        vm.edit = function(StudentAcademicDetail) {
            $scope.StudentAcademicDetail = StudentAcademicDetail;
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

    function EditAcademicDetailByAdminController($location, $scope, $cookies, $anchorScroll, $uibModalInstance, UserService, academic_detail_id) {
        $location.hash('academicDetailForm');
        $anchorScroll();
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html";
        vm.template = "static/templates/common/academic_detail_form.html";
        vm.isEditForm = true;
        vm.academic_detail_not_found = true;
        vm.close = function() {
            $uibModalInstance.close();
        };
        UserService.academicDetailApi.get({'id':academic_detail_id}).$promise.then(function (success) {
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
        console.log("Inside academic detail edit controller");
        //document.getElementById(hashId).focus();
        vm.edit = function(StudentAcademicDetail) {
            if(!$scope.StudentAcademicDetail)
                $scope.StudentAcademicDetail = StudentAcademicDetail;
            console.log("hey academic edit", $scope.StudentAcademicDetail);
            if(vm.academic_detail_not_found) {
                var data = vm.studentAcademicDetail;
                if(!data.student)
                    data['student'] = academic_detail_id;
                UserService.academicDetailApi.save(data).$promise.then(function (success) {
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
                    vm.close();
                }, function (error) {
                    console.log(error);
                    vm.error_msg = "Unable to update your academic detail, please try again";
                });
            }
        };
    }
})();
