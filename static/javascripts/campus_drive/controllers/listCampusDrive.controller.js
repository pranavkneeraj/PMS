/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.campusdrive.controllers')
    .controller('campusDriveListController', campusDriveListController);
    campusDriveListController.$inject = ['$scope', '$location', '$anchorScroll', '$uibModal', 'UserService'];

  /**
   * @namespace IndexController
   */
    function campusDriveListController($scope, $location, $anchorScroll, $uibModal, UserService) {
        var vm = this;
        vm.campusDrives = [];
        $scope.currentPage = 1;
        vm.itemsPerPage = 10;
        vm.maxSize = 5;
        console.log("dsaas",UserService);
        UserService.campusDriveApi.query().$promise.then(
            function (success) {
                vm.campusDrives = success;
                vm.totalItems = success.length;
                console.log("dasdsadasdsadsad",success.length);
                $anchorScroll('content-area');
                //console.log(angular.element(document).find('#bottom'))
            }, function (error) {
                console.log("error",error);
            }
        );
        vm.editCampusDriveDetail = function (selectedStudent) {
            vm.selectedCampusDrive = selectedCampusDrive;
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_personal_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditPersonalDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    'student':function() {
                        return vm.selectedStudent;
                    }
                }
            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };
        vm.remove = function (selectedCampusDrive) {
               var modalInstance = $uibModal.open({
                   animation: $scope.animationsEnabled,
                   templateUrl: 'static/templates/common/modal_alert.html ',
                   controller:'alertModalController',
                   controllerAs:'vm',
                   resolve:{
                        msg:function(){
                            return "Do you want delete this campus drive?"
                        }
                   }
               });
            console.log(modalInstance)
            modalInstance.result.then(function(success){
                console.log("success",success)
                UserService.campusDriveApi.remove({'id':selectedCampusDrive.id}).$promise.then(
                    function (success) {
                        console.log(angular.element(document).find('#'+selectedCampusDrive.id));
                        angular.element(document).find('#'+selectedCampusDrive.id).remove();
                    }, function (error) {
                        console.log("error",error)
                    }
                );
            },function(error){
                console.log("error",error)
            });
        };

        /*
        vm.editAcademicDetail = function (selectedStudent) {

            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent)
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_academic_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditAcademicDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    'academic_detail_id':function() {
                        return vm.selectedStudent.id;
                    }
                }
            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };
        vm.editPGDetail = function (selectedStudent) {
            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent);
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_pg_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditPGDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    academicDetail: function(){
                        return null;
                    },
                    pgSemDetail:function(UserService){
                        return UserService.academicDetailApi.get({'id':vm.selectedStudent.id, 'include_pg_sem':'t'});
                    }
                }

            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };


        vm.update = function () {
        };
        vm.remove = function (selectedStudent) {
            console.log(selectedStudent);
            UserService.api.remove({'id':selectedStudent.id}).$promise.then(
                function (success) {
                    console.log("deleted");
                    console.log(angular.element(document).find('#'+selectedStudent.id))
                    angular.element(document).find('#'+selectedStudent.id).remove();
                }, function (error) {
                    console.log("error",error)
                }
            );
        };*/
    };
})();
