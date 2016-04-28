/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.layout.controllers')
        .controller('studentListByCampusDriveController',studentListByCampusDriveController);
    studentListByCampusDriveController.$inject = ['$scope', '$location', '$anchorScroll', '$uibModal', 'UserService'];

  /**
   * @namespace IndexController
   */
    function studentListByCampusDriveController($scope, $location, $anchorScroll, $uibModal, UserService) {
        var vm = this;
        $scope.currentPage = 1;
        vm.itemsPerPage = 10;
        vm.maxSize = 5;
        vm.sort_by = '-address';
        console.log("dsaas",UserService);
        UserService.campusDriveApi.query().$promise.then(
            function (success) {
                vm.campusDrives = success;
                $anchorScroll('content-area');
                //console.log(angular.element(document).find('#bottom'))
            }, function (error) {
                console.log("error",error);
            }
        );
        vm.campusDriveSelected = function($item, $model, $label, $event){
            vm.CampusDriveSelected = $item;
        };
        vm.getEligibleStudents = function () {
            console.log(vm.selectedCampusDrive, vm.CampusDriveSelected);
            vm.student = UserService.interestedStudentApi.query({'campus_drive_id':vm.CampusDriveSelected.id}).$promise.then(function (success) {
                vm.students = success;
                console.log(success)
            });
        };
        vm.markStudentAsPlaced = function (selectedStudent) {
            var modalInstance = $uibModal.open({
                animation: $scope.animationsEnabled,
                templateUrl: 'static/templates/common/modal_alert.html ',
                controller:'alertModalController',
                controllerAs:'vm',
                resolve:{
                    msg:function(){
                        return "Do you want to mark this student as placed?";
                    }
                }
            });
            modalInstance.result.then(function(success){
                console.log(selectedStudent, success);
                UserService.placementMail.save({'user':selectedStudent, 'campus_drive':vm.CampusDriveSelected}).$promise.then(
                    function (success) {
                        console.log(success);
                    }, function (error) {
                        console.log("error",error)
                    }
                );
            });
        };
    };

})();
